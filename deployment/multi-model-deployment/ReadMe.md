Task:
Build a Multi Model Server using TorchServe KServe, Knative and deploy in Kubernetes

#Steps

1. Create model and processor files
```
Run the download_all.py file to download all the model and processor artifacts. This contains downloading 5 model artifacts. 
cd multi-model-deployment
python3 download_all.py
```

2. Create MAR files 
```
Run torchserve docker container 
docker run -it --platform linux/amd64 --rm  --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 -v $(pwd):/opt/src pytorch/torchserve:0.8.1-cpu bash

#create mar files
torch-model-archiver --model-name cat-classifier --handler hf_image_classification_handler.py --extra-files models/cat-classifier/ -r requirements.txt --version 1.0
torch-model-archiver --model-name dog-classifier --handler hf_image_classification_handler.py --extra-files models/dog-classifier/ -r requirements.txt --version 1.0
torch-model-archiver --model-name food-classifier --handler hf_image_classification_handler.py --extra-files models/food-classifier/ -r requirements.txt --version 1.0
torch-model-archiver --model-name imagenet-vit --handler hf_image_classification_handler.py --extra-files models/imagenet-vit/ -r requirements.txt --version 1.0
torch-model-archiver --model-name indian-food-classifier --handler hf_image_classification_handler.py --extra-files models/indian-food-classifier/ -r requirements.txt --version 1.0
```
3. Run TorchServe Model
```
cd deployment

#start torchserve docker container
docker run --platform linux/amd64 -it --rm -p8080:8080         -p8081:8081         -p8082:8082         -p7070:7070         -p7071:7071 -v /Users/uv/Documents/work/gitrepos/dl-package/deployment/multi-model-deployment/config.properties:/home/model-server/config.properties -v /Users/uv/Documents/work/gitrepos/dl-package/deployment/:/models pytorch/torchserve:0.8.1-cpu bash

or 
inside the torchserve docker
cd /opt
torchserve --ts-config src/config.properties --model-store src/

#start torchserve server
torchserve --ts-config /home/model-server/config.properties --model-store /models/multi-model-deployment/
```



