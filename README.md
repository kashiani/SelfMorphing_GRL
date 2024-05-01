# Self Morphing 

This repository contains python implementation of Self_morphing with OpenCV using FERET and FRGC datasets in the GRL (Generalizable Representation Learning) paper.

## Table of Contents
- [GRL](#table-of-contents)
    - [Installation](#installation)
    - [Self-Morphing on FERET dataset](#self-morphing-on-feret-dataset)
    - [Self-Morphing on FRGC dataset](#self-morphing-on-frgc-dataset)
    - [Citing GRL](#citing-grl)
    - [Reference](#reference)

    



## Installation
1. First clone the repository
   ```
   git clone https://github.com/kashiani/SelfMorphing_landmarks.git
   ```
2. Create the virtual environment via conda
    ```
    conda create -n SelfMorphing python=3.7
    ```
3. Activate the virtual environment.
    ```
    conda activate SelfMorphing
    ```
4. Install the dependencies.
   ```
   pip install -r requirements.txt
   ```



## Self-Morphing on FERET dataset
run the following command:

``` 
python Create_self_morphing_FERET.py  --source_images './src_images/FERET_MTCNN'  --output './out_images/self_FERET' --proportion_morphing 0.5 
```



## Self-Morphing on FRGC dataset
run the following command:

``` 
python Create_self_morphing_FRGC.py  --source_images './src_images/FRGC_MTCNN'  --output './out_images/self_FRGC' --proportion_morphing 0.5 
```

## Citing GRL
If you use this repository or would like to refer the paper, please use the following BibTeX entry
```
@inproceedings{kashiani2023towards,
  title={Towards Generalizable Morph Attack Detection with Consistency Regularization},
  booktitle={2023 IEEE International Joint Conference on Biometrics (IJCB)},
  pages={1--10},
  year={2023},
  organization={IEEE}
}
```

## Reference
[1]  Kashiani, Hossein, et al. "Towards Generalizable Morph Attack Detection with Consistency Regularization." 2023 IEEE International Joint Conference on Biometrics (IJCB). IEEE, 2023.
