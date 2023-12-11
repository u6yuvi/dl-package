# Using Deployment Manifests

```
cd deployment
kubectl apply -f .
minikube tunnel
```

Go to fastapi.localhost to try the model inference FastApi Docs

# Using Helm Package Manager

1. Install Helm package 
```
brew install helm
```

2. Create new helm package for fastai-gpt2-release

```
helm create fastapi-gpt2-release

```
3. Remove all the files inside the template and clear all the values from values.yaml file

4. Copy all the Deployment Manifest into the template folder

5. Add the configuration values in the values.yaml file.

5. Deploy using helm
```
#helm install helm package <path to the package>
helm install fastapi-gpt2-release fastapi-gpt2-helm 
```
Go to fastapi.localhost to try the Inference using FastApi Docs
![](images/gpt2-k8-fastapi.png)

Refer gpt-2-k8.md file for more details on the deployment specs.