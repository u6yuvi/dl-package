# Pytorch Ligtning Model Experimentation Template using Hydra

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)![hydra](https://img.shields.io/badge/Config-Hydra_1.3-89b8cd)![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)


# Key Features

1. Supports Pytorch Bring you own Model , Huggingface Models and Timm Models.
2. Model Training using Pytorch Lightning Framework
3. Experiments Configuration using Hydra Template
4. Logging using Tensorboard.


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

#install packages
make pip-tools

#Train Model
python3 copper/train.py data=cifar.yaml model=timm.yaml

Experiment Artifacts stored at path: outputs/
Refer config/hydra/default.yaml for more information on configuring output dir.

#Evaluate Model
Add the model checkpoint filename at config/eval.yaml
    ckpt_file: xxx.ckpt
or  
pass the model checkpoint filename in the command line duirng evaluation
python3 copper/eval.py data=cifar.yaml model=timm.yaml ckpt_file=2023-06-15/00-46-28/checkpoints/last.ckpt
```


# Lightning Template

```
copper_train --help
```

examples

- `copper_train data.num_workers=16`
- `copper_train data.num_workers=16 trainer.deterministic=True +trainer.fast_dev_run=True`

## Development

Install in dev mode

```
pip install -e .
```

### Docker

<docker-usage-instructions-here>


## Getting Started

```
Run cifar model training
python3 copper/train.py data = cifar.yaml model= cifar10.yaml
```
