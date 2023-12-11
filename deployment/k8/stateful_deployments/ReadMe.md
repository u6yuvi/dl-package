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

2. Create new helm package for fastai-release

```
helm create fastapi-helm
```
3. Remove all the files inside the template and clear all the values from values.yaml file

4. Copy all the Deployment Manifest into the template folder

5. Deploy using helm
```
#helm install helm package <path to the package>
helm install fastapi-release fastapi-helm
```
