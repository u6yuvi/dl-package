# Pytorch Ligtning Model Experimentation Template

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)![hydra](https://img.shields.io/badge/Config-Hydra_1.3-89b8cd)![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)


# Key Features

1. Supports [Pytorch Custom Models](https://pytorch.org/vision/stable/models.html), [Huggingface Models](https://huggingface.co/models) and [Timm Models](https://github.com/huggingface/pytorch-image-models).
2. Model Training and Evaluation using [Pytorch Lightning Framework](https://lightning.ai/).
3. [Docker Container Based Model Training and Evaluation](https://github.com/u6yuvi/dl-package/tree/main#using-docker-containers)
3. Experiments Configuration using [Hydra Template](https://hydra.cc/).
4. Experiment Logging using:
    1. [Tensorboard](https://www.tensorflow.org/tensorboard/get_started).
    2. [Mlflow](https://github.com/mlflow/mlflow/)
    3. [Aim](https://github.com/aimhubio/aim)
5. [Run Hyperaparameter Search using Lightning, Optuna and Hydra](https://github.com/u6yuvi/dl-package/tree/main#run-hyperparameter-tuning-with-pytorch-lightning-hydra-and-optuna)
6. Data Versioning using Data Version Control
7. Serializable and optimizable Pytorch models using TorchScript
8. [Build & Share Model Demos using Gradio](https://github.com/u6yuvi/dl-package#build--share-model-demos-using-gradio)
9. Deployment using AWS ECR + ECS
10. [Build Model Endpoints using FastAPI](https://github.com/u6yuvi/dl-package#build-model-endpoints-using-fastapi)


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

## Run Multi-Run Experiments using Hydra 

### Without Docker Container
1. Run experiment
```
dl_pkg_train -m hydra/launcher=joblib hydra.launcher.n_jobs=4 experiment=cifar_vit model.net.patch_size=1,2,4,8,16 data.num_workers=4
```
#experiment logs are saved under logs/ folder.

2. Run AIM UI
```
aim up
```

3. Run Tensorboard
```
tensorboard --logdir=logs/tensorboard
```
4. Run MLFlow
```
mlflow ui
```

## Run Hyperparameter Tuning with Pytorch Lightning Hydra and Optuna

Refer [colab notebook](https://colab.research.google.com/drive/17HWH-pTgcsTJOX8X5XGGLTCuVQ1Zwi0l?usp=sharing)

1. LR Finder and Batch Size Finder using Pytorch Ligthning Callback

    - Refer train.py for lr-finder and batch size finder callbacks

    - Enable or disable using flag **tuner**  in train.yaml file

![](images/lr_finder.png)

2. Create hyperparameter search config file for model parameters
![](images/hparam_optuna.png)


3. Run Hyperparameter Search using Optuna and Hydra
```
dl_pkg_train hparams_search=gpt_optuna logger=many_loggers
```

4. Results of Hyperparameter Search 

![](images/best_h_param.png)

5. Compare the Hyperparameter Experiment results on AIM, Tensorboard or MLFlow

```
Hyperparameter Results saved under logs/
```

**AIM Dashboard**

![](images/aim_h_search.png)


**Tensorboard Dashboard**

![](images/tensorboard_hparam.png)


### Using Docker Containers

1. Refer docker-compose.yml for more reference
    Services Created 
    1. train - Running Multiple experiments with different hyperparameters
    2. mlrun - MLFlow UI
    3. tensorboard - Tensorboard UI
    4. aim - AIM UI

2. Run experiment 
```
docker-compose  -f .devcontainer/docker-compose_copy.yml  up --build
```

3. View Experiment Results
    1. Tensorboard UI - http://localhost:6007/ 
    2. AIM UI - http://localhost:43801
    3. MLFLOW UI - http://localhost:5001

Eg: cifar10_vit experiment on VIT model patch_size= 1,2,4,8,16
![](images/aim_experiment.png)

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


## Build & Share Model Demos using Gradio

## Steps to reproduce
1. Train and serialise your choice of model using Pytorch Lightning and Torch Script
```
dl_pkg_train experiment=cifar_vit
```
Refer `configs/experiment/cifar_vit` for setting experiment parameters
When using TorchScript : ensure `jit:True` and provide a model path name under `jit_model_path`

Torch Script model will be saved under the given path
![](images/torchscript.png)

2. Run Demo in Local

    1. add the torchscript checkpoint path in `demo_ckpt_path` under `configs/demo_traced.yaml`
    2. Update the `demo.py` to configure Gradio UI, Loading model checkpoint and Model Inference Code
```
#run the gradio app 
dl_pkg_demo
```
Gradio App running at - **0.0.0.0:8080** 
![](images/gradio_local.png)

3. Run Demo in Docker Container

```
#Build the docker image
docker compose  -f .devcontainer/docker-compose.yml up --build demo
#provide the model-checkpoint path in the Dockerfile.demo
#run the gradio demo in docker
docker run -p 8080:8080 <image_name>:latest 

#Docker command to run Gradio Demo for Cifar VIT Experiment
docker run -p 8080:8080 u6yuvi/demo_cpu:latest
```
![](images/docker_demo.png)

## Build Model Endpoints using FastAPI

1. Write FastAPI Endpoints
```
Refer deployment/gpt.fastapi.py && deployment/vit_fastapi.py
```

2. Build Docker Container with FastAPI
```
Refer .devcontainer/Dockerfile.gpt_fastApi && .devcontainer/Dockerfile.vit_fastApi
```
3. Interact with the Model Endpoint using Swagger UI
```
Go to https://<ip_address:80/docs>
```
![](images/swagger_ui.png)

4. Interact with the Model Endpoint using Python request module

Refer deployment/test_endpoint.py
### Testing GPT Endpoint 
![](images/gpt_pytest.png)

### Testing VIT Endpoint
![](images/vit_pytest.png)


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




# Misc Commands

```
#create and run service
docker-compose  -f .devcontainer/docker-compose_copy.yml  up --build
#create and run specific service
docker compose  -f .devcontainer/docker-compose.yml up --build demo
#mount volumne
docker compose run -v ${pwd}/logs <image_name> bash
#run experiment
dl_pkg_train -m hydra/launcher=joblib hydra.launcher.n_jobs=4 experiment=cifar_vit model.net.patch_size=1,2,4,8,16 data.num_workers=0
#pushing to docker hub
docker login -u NAME
docker image tag trtest USER/trtest:latest
docker image push USER/trtest:latest
```
