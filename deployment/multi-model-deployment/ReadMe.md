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

minikube start --driver=docker --memory 6745 --cpus 4 --disk-size 100g

#Delete istio 
istio-1.9.0/bin/istioctl x uninstall --purge

#Using PV Volume

https://github.com/idiap/pytorch-serve/tree/master/kubernetes/kserve

kubectl apply -f pv-deployments/pv.yaml -n kserve

#create pod
kubectl apply -f pv-deployments/pv_pod.yaml -n kserve 

#create directories
kubectl exec -it model-store-pod -c model-store -n kserve -- mkdir /pv/model-store/
kubectl exec -it model-store-pod -c model-store -n kserve -- mkdir /pv/config/

#copy files
kubectl cp cat-classifier.mar model-store-pod:/pv/model-store/ -c model-store -n kserve
kubectl cp config.properties model-store-pod:/pv/config/ -c model-store -n kserve

kubectl -n kserve apply -f all-classifier.yaml

#Reference to look for
https://github.com/kserve/kserve/tree/master/docs/samples/v1beta1/torchserve

#Developer 
https://github.com/kserve/website/blob/main/docs/developer/developer.md

Debug
https://github.com/kserve/website/blob/main/docs/developer/debug.md

