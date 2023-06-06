# DynaCam
| **[[Paper]](http://arxiv.org/abs/2306.02850)**  | **[[Video]](https://youtu.be/PX-7cuZuxJs)** | **[[Project Page]](http://www.yusun.work/TRACE/TRACE.html)** |

DynaCam contains **in-the-wild** RGB videos captured by dynamic cameras, including annotations:  
 - **3D human trajectories in world coordinates**

For the details, please refer to our [project page](http://www.yusun.work/TRACE/TRACE.html).

## Download

[[Google drive]](https://drive.google.com/drive/folders/12zJYkTlKPn_3tlh96BQ6zuyEr3vTxqRw?usp=sharing) 

[[Baidu drive (百度网盘)]](https://pan.baidu.com/s/1wttz00Y5JZkHrpNOXor5Og?pwd=55f7) 

The structure of dataset is supposed to be:
```
|-- DynaCam
| --|-- video_frames
|   |   |-- panorama_test
|   |   |-- panorama_train
|   |   |-- panorama_val
|   |   |-- translation_test
|   |   |-- translation_train
|   |   |-- translation_val
|   |-- annotations
|   |   |-- *.npz
```

## Visualization

To visualize each video sequences and corresponding annotations, like 3D human trajectory, please download the [SMPL_NEUTRAL.pkl](https://github.com/Arthur151/DynaCam/releases/download/predictions/SMPL_NEUTRAL.pkl) and put it into 'assets/'
, then run
```
sh install.sh
# set the path to dynacam_folder in show_examples.py 
python show_examples.py 
```
<p float="center">
  <img src="https://github.com/Arthur151/DynaCam/releases/download/predictions/dynacam_vis_examples.gif" width="50%" />
</p>
</p>
Press `stop` to stop the animation, draw the `slider` to sellect the frame, press `ESC` on your keyboard to go next. 


## Evaluation
To re-implement all results on DynaCam in our paper, please download [predictions](https://github.com/Arthur151/DynaCam/releases/tag/predictions), set the path in evaluation.py to ensure the structure like
```
|-- predictions
| --|-- TRACE
| --|-- GLAMR
| --|-- bev_dpvo
```
, then run:
```
sh install.sh
python evaluation.py
```

## Citation
Please cite our paper if you use DynaCam in your research. 
```bibtex
@InProceedings{TRACE,
    author = {Sun, Yu and Bao, Qian and Liu, Wu and Mei, Tao and Black, Michael J.},
    title = {{TRACE: 5D Temporal Regression of Avatars with Dynamic Cameras in 3D Environments}}, 
    booktitle = {IEEE/CVF Conf.~on Computer Vision and Pattern Recognition (CVPR)}, 
    month = June, 
    year = {2023}}
```