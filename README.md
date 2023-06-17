# Pytorch Ligtning Model Experimentation Template

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)![hydra](https://img.shields.io/badge/Config-Hydra_1.3-89b8cd)![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)


# Key Features

1. Supports [Pytorch Custom Models](https://pytorch.org/vision/stable/models.html), [Huggingface Models](https://huggingface.co/models) and [Timm Models](https://github.com/huggingface/pytorch-image-models).
2. Model Training and Evaluation using [Pytorch Lightning Framework](https://lightning.ai/).
3. Experiments Configuration using [Hydra Template](https://hydra.cc/).
4. Experiment Logging using [Tensorboard](https://www.tensorflow.org/tensorboard/get_started).


## Getting Started

### Run in Conda Environment 

#### Install Dependencies 

```
# clone project 
git clone https://github.com/u6yuvi/dl-package.git dl-project
cd dl-project/

# create conda environment [dl-project]
conda env create -f conda_env.yml 
conda activate dl-project

#install dl_pkg package
pip3 install -e .

#Train Model through command line
- `dl_pkg_train data.num_workers=16`
or 
- `dl_pkg_train data.num_workers=16 trainer.deterministic=True +trainer.fast_dev_run=True`

Experiment Artifacts stored at path: outputs/
Refer- configs/hydra/default.yaml for more information on configuring output dir.

#Evaluate Model
Add the model checkpoint filename at configs/eval.yaml
    ckpt_file: xxx.ckpt
or  pass it through command line while running evaluation

- `dl_pkg_eval ckpt_file=2023-06-17/20-23-38/checkpoints/last.ckpt`
or 
- `python3 dl_pkg/eval.py data=cifar.yaml model=timm.yaml ckpt_file=2023-06-15/00-46-28/checkpoints/last.ckpt`
```


### Run in DevContainer with VS Code
#### Install Dependencies 

1. Clone project 
```
git clone https://github.com/u6yuvi/dl-package.git dl-project
cd dl-project/
```

2. Rebuild the dev container using the .devcontainer-> devcontainer.json file
Read about DevContainers here - [Developing inside a container](https://code.visualstudio.com/docs/devcontainers/containers)
![Dev Container](images/dev-container.png)

Dev Container will start and install the python packages from requirements.txt
![Installing the project python package dependencies](images/dev-container-requirements.png)

3. Install dl_pkg package
```
pip3 install -e .
```
4. Train Model through command line
```
dl_pkg_train data.num_workers=16
or 
dl_pkg_train data.num_workers=16 trainer.deterministic=True +trainer.fast_dev_run=True
```

Experiment Artifacts stored at path: outputs/

Refer- configs/hydra/default.yaml for more information on configuring output dir.

5. Evaluate Model

Add the model checkpoint filename at configs/eval.yaml
    - `ckpt_file: xxx.ckpt`

or  pass it through command line while running evaluation
```
dl_pkg_eval ckpt_file=2023-06-17/20-23-38/checkpoints/last.ckpt
or 
python3 dl_pkg/eval.py data=cifar.yaml model=timm.yaml ckpt_file=2023-06-15/00-46-28/checkpoints/last.ckpt
```


# Hydra Template 

Lists all the configurable parameters for this project during:
1. Training
```
dl_pkg_train --help
```
2. Evaluation
```
dl_pkg_evaluate --help
```

# Run Tensorboard 
```
tensorboard --logdir='outputs/path_to_tensorboard_logs' --port=xxxx
```
![](images/tensorboard.png)

![Tensorboard logs Directory](images/tensorboard_logs.png)


# Maintainers

1. [Utkarsh Vardhan](https://github.com/u6yuvi)

