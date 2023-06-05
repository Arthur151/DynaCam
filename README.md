# DynaCam

DynaCam contains **in-the-wild** RGB videos captured by dynamic cameras, including annotations:  
 - **3D human trajectories in world coordinates**
 - **Camera poses**  

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