# Pytorch Ligtning Model Experimentation Template

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)![hydra](https://img.shields.io/badge/Config-Hydra_1.3-89b8cd)![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)


# Key Features

1. Supports [Pytorch Custom Models](https://pytorch.org/vision/stable/models.html), [Huggingface Models](https://huggingface.co/models) and [Timm Models](https://github.com/huggingface/pytorch-image-models).
2. Model Training and Evaluation using [Pytorch Lightning Framework](https://lightning.ai/).
3. Experiments Configuration using [Hydra Template](https://hydra.cc/).
4. Experiment Logging using [Tensorboard](https://www.tensorflow.org/tensorboard/get_started).
5. Data Versioning using Data Version Control


## Getting Started


## Training 
1. Clone project 
```
git clone https://github.com/u6yuvi/dl-package.git dl-package
cd dl-package/
```
2.  Run Training
```
docker run --name dl_container --rm u6yuvi/dl-package:latest dl_pkg_train
```
![](images/training.png)

## Run Experiments using Hydra 

1. Create an experiment hydra file overiding train.yaml file
![](images/experiment_cofig.png)


2. Run training and evaluation with experiment config

```
If "experiment : null added in the train.yaml file which will overide the configuration
dl_pkg_trian experiment=cat_dog

If "experiment:null" not added in train.yaml.Override the train.yaml using
dl_pkg_train +experiment=cat_dog
```

3. Run Evaluation using experiment config
```
dl_pkg_eval +experiment=cat_dog
```
![](images/eval.png)

4. Run Prediction using experiment config
```
Load an image from data/predict/test
dl_pkg_predict +experiment=cat_dog
```
![](images/predict.png)

## Evaluation
1. Clone project 
```
git clone https://github.com/u6yuvi/dl-package.git dl-package
cd dl-package/
```
2.  Run Evaluation
```
docker run --name dl_container --rm u6yuvi/dl-package:latest dl_pkg_eval ckpt_file=2023-06-17/20-23-38/checkpoints/last.ckpt
```
![](images/evaluation.png)



### Development in DEV Container with VS Code
#### Install Dependencies 

1. Clone project 
```
git clone https://github.com/u6yuvi/dl-package.git dl-package
cd dl-package/
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


### Run in Conda Environment 

#### Install Dependencies 

```
# clone project 
git clone https://github.com/u6yuvi/dl-package.git dl-package
cd dl-package/

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

# Docker Commands
1. Build Docker Image
```
docker build -t dl-package -f .devcontainer/Dockerfile .
```

# Download Dataset
1. DogvsCat
```
wget https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip
unzip kagglecatsanddogs_5340.zip

#split dataset in train and test
scripts/split_dataset.py
#Delete empty files
find . -type f -empty -print -delete
```

# DVC Configuration
```
#Set remote storage for storing data and model artifacts
dvc remote add -d local <path_to_local_directory>

#Push data to remote directory
dvc push data outputs

#Pull data from remote directory
dvc pull
```

Read more about [DVC](https://dvc.org/doc)

# Maintainers

1. [Utkarsh Vardhan](https://github.com/u6yuvi)
2. [Utkarsh Mittal](https://github.com/mittalutkarsh)
3. [Ramkumar M](https://github.com/voldy12)

