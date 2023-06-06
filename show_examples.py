import os
import numpy as np
import cv2
from visualization.open3d_gui import visualize_world_annots

import torch
from smplx import SMPL

dynacam_folder = '/Volumes/NTFS/DynaCam'
smpl_model_folder = 'assets'


def obtain_smpl_verts(smpl_thetas, smpl_betas, smpl_model):
    # smpl_thetas is in shape N x 24 x 3 x 3
    world_grot_mat = smpl_thetas[:,0]
    body_pose = smpl_thetas[:,1:]
    #print(smpl_betas.shape, body_pose.shape, world_grot_mat.shape)
    smpl_output = smpl_model(global_orient=world_grot_mat, body_pose=body_pose, betas=smpl_betas)
    #verts = smpl_output.vertices.cpu().numpy()
    
    return smpl_output.joints.cpu().numpy(), world_grot_mat.cpu().numpy()

def visualize_subject_world_results(seq_name, annots, seq_frame_dir, img_ext='jpg'):
    print(f'Annotation keys include: ', list(annots.keys()))
    smpl_model = SMPL(smpl_model_folder, gender='neutral').eval()

    # ['person_id', 'poses', 'betas', 'world_grots', 'world_trans', 'kp3ds', 'kp2ds', 'frame_ids', \
    #  'camera_intrinsics', 'camera_extrinsics', 'camera_extrinsics_aligned', 'world_grots_aligned', 'world_trans_aligned']
    smpl_thetas = annots['poses']
    subject_num, frame_num = smpl_thetas.shape[:2]
    body_pose = torch.from_numpy(smpl_thetas[:, :, 1:].reshape(subject_num, frame_num, 23*3)).float()
    smpl_betas = torch.from_numpy(annots['betas']).float()
    if 'world_grots_aligned' in annots:
        world_grots = torch.from_numpy(annots['world_grots_aligned']).float()
        world_trans = annots['world_trans_aligned']
        camera_intrinsics = annots['camera_intrinsics']
        camera_extrinsics = annots['camera_extrinsics_aligned']
    else:
        world_grots = torch.from_numpy(annots['world_grots']).float()
        world_trans = annots['world_trans']
        camera_intrinsics = annots['camera_intrinsics']
        camera_extrinsics = annots['camera_extrinsics']
        camera_extrinsics = np.concatenate([camera_extrinsics, np.repeat(np.array([[[0,0,0,1]]]),len(camera_extrinsics), axis=0)], axis=1)

    vertices = []
    for subject_id in range(subject_num):
        vertex = smpl_model(global_orient=world_grots[subject_id], body_pose=body_pose[subject_id], betas=smpl_betas[subject_id]).vertices.detach().cpu().numpy()
        vertices.append(vertex)
    
    frame_paths = [os.path.join(seq_frame_dir, '{:06d}.{}'.format(frame_id, img_ext)) for frame_id in annots['frame_ids']]
    
    visualize_world_annots(seq_name, vertices, world_trans, camera_intrinsics, camera_extrinsics, frame_paths, np.asarray(smpl_model.faces))

if __name__ == '__main__':
    split_name = ['panorama_test', 'panorama_train', 'panorama_val', 'translation_test', 'translation_train', 'translation_val'][3]
    annots_path = os.path.join(dynacam_folder, 'annotations', f'{split_name}.npz')
    annots = np.load(annots_path, allow_pickle=True)['annots'][()]

    seq_names = list(annots.keys())
    seq_names.remove('sequence_dict')
    seq_names.remove('ID_num')
    print(f'All sequences in {split_name}:',seq_names)
    for seq_name in seq_names:
        print(f'Visualizing sequence {seq_name} in {split_name}')
        seq_frame_dir = os.path.join(dynacam_folder, 'video_frames', split_name, seq_name)
        img_ext = 'jpg' if 'panorama' in split_name else 'png'
        visualize_subject_world_results(seq_name, annots[seq_name], seq_frame_dir, img_ext=img_ext)