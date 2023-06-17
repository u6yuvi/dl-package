# Pytorch Ligtning Model Experimentation Template using Hydra

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)![hydra](https://img.shields.io/badge/Config-Hydra_1.3-89b8cd)![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)


# Key Features

1. Supports Pytorch Custom Models, Huggingface Models and Timm Models.
2. Model Training and Evaluation using Pytorch Lightning Framework
3. Experiments Configuration using Hydra Template
4. Experiment Logging using Tensorboard.


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

```
# clone project 
git clone https://github.com/u6yuvi/dl-package.git dl-project
cd dl-project/

#Rebuild the dev container using the .devcontainer config files
Read about DevContainers here - [Developing inside a container](https://code.visualstudio.com/docs/devcontainers/containers)
![](images/dev-container.png)
```

# Lightning Template

```
dl_pkg_train --help
```

examples

## Development

Install in dev mode

```
pip install -e .
```

### Docker

<docker-usage-instructions-here>

