# Deployment Describe
* kubectl describe deployment.apps/model-server 

```
Name:                   model-server
Namespace:              default
CreationTimestamp:      Fri, 06 Oct 2023 23:35:11 -0700
Labels:                 app.kubernetes.io/managed-by=Helm
Annotations:            deployment.kubernetes.io/revision: 1
                        meta.helm.sh/release-name: fastapi-gpt2-release
                        meta.helm.sh/release-namespace: default
Selector:               app=model-server
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=model-server
  Containers:
   model-server:
    Image:      model_server:latest
    Port:       80/TCP
    Host Port:  0/TCP
    Environment:
      REDIS_HOST:      <set to the key 'hostname' of config map 'redis-config'>           Optional: false
      REDIS_PORT:      <set to the key 'port' of config map 'redis-config'>               Optional: false
      REDIS_PASSWORD:  <set to the key 'db_password' in secret 'redis-secret'>            Optional: false
      TIMM_MODEL:      <set to the key 'timm_model' of config map 'model-server-config'>  Optional: false
    Mounts:            <none>
  Volumes:             <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   model-server-b884894f4 (1/1 replicas created)
Events:
  Type    Reason             Age    From                   Message
  ----    ------             ----   ----                   -------
  Normal  ScalingReplicaSet  3m17s  deployment-controller  Scaled up replica set model-server-b884894f4 to 1  
```
* kubectl describe deployment.apps/web-server 

```
Name:                   web-server
Namespace:              default
CreationTimestamp:      Fri, 06 Oct 2023 23:35:11 -0700
Labels:                 app=web-server
                        app.kubernetes.io/managed-by=Helm
Annotations:            deployment.kubernetes.io/revision: 1
                        meta.helm.sh/release-name: fastapi-gpt2-release
                        meta.helm.sh/release-namespace: default
Selector:               app=web-server
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=web-server
  Containers:
   web-server:
    Image:      web_server:latest
    Port:       80/TCP
    Host Port:  0/TCP
    Environment:
      REDIS_HOST:        <set to the key 'hostname' of config map 'redis-config'>                 Optional: false
      REDIS_PORT:        <set to the key 'port' of config map 'redis-config'>                     Optional: false
      REDIS_PASSWORD:    <set to the key 'db_password' in secret 'redis-secret'>                  Optional: false
      MODEL_SERVER_URL:  <set to the key 'model_server_url' of config map 'model-server-config'>  Optional: false
    Mounts:              <none>
  Volumes:               <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   web-server-5775b4b6bc (1/1 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  12m   deployment-controller  Scaled up replica set web-server-5775b4b6bc to 1
```
* kubectl describe deployment.apps/redis-db

```
Name:                   redis-db
Namespace:              default
CreationTimestamp:      Fri, 06 Oct 2023 23:35:11 -0700
Labels:                 app.kubernetes.io/managed-by=Helm
Annotations:            deployment.kubernetes.io/revision: 1
                        meta.helm.sh/release-name: fastapi-gpt2-release
                        meta.helm.sh/release-namespace: default
Selector:               app=redis,role=master
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=redis
           role=master
  Containers:
   redis-master:
    Image:      redis:7.2.1
    Port:       6379/TCP
    Host Port:  0/TCP
    Command:
      redis-server
    Args:
      --requirepass
      $(REDIS_PASSWORD)
    Limits:
      cpu:     200m
      memory:  200Mi
    Environment:
      REDIS_PASSWORD:  <set to the key 'db_password' in secret 'redis-secret'>  Optional: false
    Mounts:
      /data from redis-storage (rw)
  Volumes:
   redis-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  redis-pvc
    ReadOnly:   false
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   redis-db-96b87bcb6 (1/1 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  13m   deployment-controller  Scaled up replica set redis-db-96b87bcb6 to 1
```
# Pod Description

* kubectl describe pod/web-server-5775b4b6bc-75hr4 

```
Name:             web-server-5775b4b6bc-75hr4
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Fri, 06 Oct 2023 23:35:11 -0700
Labels:           app=web-server
                  pod-template-hash=5775b4b6bc
Annotations:      <none>
Status:           Running
IP:               10.244.0.17
IPs:
  IP:           10.244.0.17
Controlled By:  ReplicaSet/web-server-5775b4b6bc
Containers:
  web-server:
    Container ID:   docker://1038963f882257d497a47b16ef2d5ee1b9109f6cdd8b2273fa8266734d9ab0c3
    Image:          web_server:latest
    Image ID:       docker://sha256:b1eeaac712d6f2566bfa65b73bc67f303f4675fe2a00728ce5ea9f22728fa146
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Fri, 06 Oct 2023 23:35:12 -0700
    Ready:          True
    Restart Count:  0
    Environment:
      REDIS_HOST:        <set to the key 'hostname' of config map 'redis-config'>                 Optional: false
      REDIS_PORT:        <set to the key 'port' of config map 'redis-config'>                     Optional: false
      REDIS_PASSWORD:    <set to the key 'db_password' in secret 'redis-secret'>                  Optional: false
      MODEL_SERVER_URL:  <set to the key 'model_server_url' of config map 'model-server-config'>  Optional: false
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-6cxxq (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-6cxxq:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  5m36s  default-scheduler  Successfully assigned default/web-server-5775b4b6bc-75hr4 to minikube
  Normal  Pulled     5m35s  kubelet            Container image "web_server:latest" already present on machine
  Normal  Created    5m35s  kubelet            Created container web-server
  Normal  Started    5m35s  kubelet            Started container web-server
```

* kubectl describe pod/redis-db-96b87bcb6-gkwfx

```

Name:             redis-db-96b87bcb6-gkwfx
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Fri, 06 Oct 2023 23:35:11 -0700
Labels:           app=redis
                  pod-template-hash=96b87bcb6
                  role=master
Annotations:      <none>
Status:           Running
IP:               10.244.0.18
IPs:
  IP:           10.244.0.18
Controlled By:  ReplicaSet/redis-db-96b87bcb6
Containers:
  redis-master:
    Container ID:  docker://e76352ffc7961b6d5903d2aa4fe7300667c53ae3515f1a4ac474e9ab6ba0b75d
    Image:         redis:7.2.1
    Image ID:      docker-pullable://redis@sha256:b68c6efe2c5f2d7d7d14a2749f66d6d81645ec0cacb92572b2fb7d5c42c82031
    Port:          6379/TCP
    Host Port:     0/TCP
    Command:
      redis-server
    Args:
      --requirepass
      $(REDIS_PASSWORD)
    State:          Running
      Started:      Fri, 06 Oct 2023 23:35:12 -0700
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     200m
      memory:  200Mi
    Requests:
      cpu:     200m
      memory:  200Mi
    Environment:
      REDIS_PASSWORD:  <set to the key 'db_password' in secret 'redis-secret'>  Optional: false
    Mounts:
      /data from redis-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-ndq4v (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  redis-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  redis-pvc
    ReadOnly:   false
  kube-api-access-ndq4v:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Guaranteed
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  6m33s  default-scheduler  Successfully assigned default/redis-db-96b87bcb6-gkwfx to minikube
  Normal  Pulled     6m32s  kubelet            Container image "redis:7.2.1" already present on machine
  Normal  Created    6m32s  kubelet            Created container redis-master
  Normal  Started    6m32s  kubelet            Started container redis-master
```

* kubectl descibe ingress

```
Name:             web-server
Labels:           app.kubernetes.io/managed-by=Helm
Namespace:        default
Address:          192.168.49.2
Ingress Class:    nginx
Default backend:  <default>
Rules:
  Host               Path  Backends
  ----               ----  --------
  fastapi.localhost  
                     /   web-server:8000 (10.244.0.17:80)
Annotations:         meta.helm.sh/release-name: fastapi-gpt2-release
                     meta.helm.sh/release-namespace: default
Events:
  Type    Reason  Age                From                      Message
  ----    ------  ----               ----                      -------
  Normal  Sync    14m (x2 over 15m)  nginx-ingress-controller  Scheduled for sync
```

* kubectl top pod

```
NAME                           CPU(cores)   MEMORY(bytes)   
model-server-b884894f4-p8qqg   5m           1437Mi          
redis-db-96b87bcb6-gkwfx       5m           2Mi             
web-server-5775b4b6bc-75hr4    5m           43Mi   
```
* kubectl top node

```
NAME       CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
minikube   277m         6%     2512Mi          25%  
```

* kubectl get all -A -o yaml

```
Last login: Fri Oct  6 23:55:17 on ttys004
➜  ~ kubectl get all -A -o yaml
apiVersion: v1
items:
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-07T17:39:30Z"
    generateName: model-server-b884894f4-
    labels:
      app: model-server
      pod-template-hash: b884894f4
    name: model-server-b884894f4-h2zkf
    namespace: default
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: model-server-b884894f4
      uid: ddde6321-ed1f-4e6c-945f-124bbd770503
    resourceVersion: "14048"
    uid: 36d3691f-122c-4510-8c9c-a6e122ab75df
  spec:
    containers:
    - env:
      - name: REDIS_HOST
        valueFrom:
          configMapKeyRef:
            key: hostname
            name: redis-config
      - name: REDIS_PORT
        valueFrom:
          configMapKeyRef:
            key: port
            name: redis-config
      - name: REDIS_PASSWORD
        valueFrom:
          secretKeyRef:
            key: db_password
            name: redis-secret
      - name: TIMM_MODEL
        valueFrom:
          configMapKeyRef:
            key: timm_model
            name: model-server-config
      image: model_server:latest
      imagePullPolicy: Never
      name: model-server
      ports:
      - containerPort: 80
        protocol: TCP
      resources: {}
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-4fjr4
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: default
    serviceAccountName: default
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - name: kube-api-access-4fjr4
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T17:39:30Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T17:39:30Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T17:39:30Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T17:39:30Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://eebba8c1ad717cfbf8ef2cd20eafc051e29c7ba9757c48bb0dc10339ad60cbe4
      image: model_server:latest
      imageID: docker://sha256:2b4d6804a64af35187a0cd553a20d683b79f831f4fce425f856744bab2fbdb81
      lastState: {}
      name: model-server
      ready: true
      restartCount: 0
      started: true
      state:
        running:
          startedAt: "2023-10-07T17:39:30Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 10.244.0.27
    podIPs:
    - ip: 10.244.0.27
    qosClass: BestEffort
    startTime: "2023-10-07T17:39:30Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-07T17:39:30Z"
    generateName: redis-db-96b87bcb6-
    labels:
      app: redis
      pod-template-hash: 96b87bcb6
      role: master
    name: redis-db-96b87bcb6-qbfsg
    namespace: default
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: redis-db-96b87bcb6
      uid: 662b487b-877d-4799-bb2b-2048da2452e9
    resourceVersion: "14081"
    uid: 9fbc079c-1f50-4ef2-b7b2-b662f53d6142
  spec:
    containers:
    - args:
      - --requirepass
      - $(REDIS_PASSWORD)
      command:
      - redis-server
      env:
      - name: REDIS_PASSWORD
        valueFrom:
          secretKeyRef:
            key: db_password
            name: redis-secret
      image: redis:7.2.1
      imagePullPolicy: IfNotPresent
      name: redis-master
      ports:
      - containerPort: 6379
        protocol: TCP
      resources:
        limits:
          cpu: 200m
          memory: 200Mi
        requests:
          cpu: 200m
          memory: 200Mi
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /data
        name: redis-storage
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-w4n4j
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: default
    serviceAccountName: default
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - name: redis-storage
      persistentVolumeClaim:
        claimName: redis-pvc
    - name: kube-api-access-w4n4j
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T17:39:43Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T17:39:45Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T17:39:45Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T17:39:43Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://1f13e540e20deb214c45a20d03de7c6cea47ca84a1615ce3ed98234ce8e071c0
      image: redis:7.2.1
      imageID: docker-pullable://redis@sha256:b68c6efe2c5f2d7d7d14a2749f66d6d81645ec0cacb92572b2fb7d5c42c82031
      lastState: {}
      name: redis-master
      ready: true
      restartCount: 0
      started: true
      state:
        running:
          startedAt: "2023-10-07T17:39:44Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 10.244.0.29
    podIPs:
    - ip: 10.244.0.29
    qosClass: Guaranteed
    startTime: "2023-10-07T17:39:43Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-07T17:39:30Z"
    generateName: web-server-5775b4b6bc-
    labels:
      app: web-server
      pod-template-hash: 5775b4b6bc
    name: web-server-5775b4b6bc-gzpk9
    namespace: default
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: web-server-5775b4b6bc
      uid: f4ec843e-4310-4641-8bc7-8fc54942f324
    resourceVersion: "14053"
    uid: 4e15404c-cdb0-4969-9660-f0d80f125b5a
  spec:
    containers:
    - env:
      - name: REDIS_HOST
        valueFrom:
          configMapKeyRef:
            key: hostname
            name: redis-config
      - name: REDIS_PORT
        valueFrom:
          configMapKeyRef:
            key: port
            name: redis-config
      - name: REDIS_PASSWORD
        valueFrom:
          secretKeyRef:
            key: db_password
            name: redis-secret
      - name: MODEL_SERVER_URL
        valueFrom:
          configMapKeyRef:
            key: model_server_url
            name: model-server-config
      image: web_server:latest
      imagePullPolicy: Never
      name: web-server
      ports:
      - containerPort: 80
        protocol: TCP
      resources: {}
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-vkl6c
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: default
    serviceAccountName: default
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - name: kube-api-access-vkl6c
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T17:39:30Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T17:39:30Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T17:39:30Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T17:39:30Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://e3fdf6c0c31fb6c1da6ff9640dd372319652209e5fb6a1292cdee94a842f028f
      image: web_server:latest
      imageID: docker://sha256:b1eeaac712d6f2566bfa65b73bc67f303f4675fe2a00728ce5ea9f22728fa146
      lastState: {}
      name: web-server
      ready: true
      restartCount: 0
      started: true
      state:
        running:
          startedAt: "2023-10-07T17:39:30Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 10.244.0.28
    podIPs:
    - ip: 10.244.0.28
    qosClass: BestEffort
    startTime: "2023-10-07T17:39:30Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-07T05:01:33Z"
    generateName: ingress-nginx-admission-create-
    labels:
      app.kubernetes.io/component: admission-webhook
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
      batch.kubernetes.io/controller-uid: a2b9aa48-ccae-4428-a61a-d5bf41f99b4d
      batch.kubernetes.io/job-name: ingress-nginx-admission-create
      controller-uid: a2b9aa48-ccae-4428-a61a-d5bf41f99b4d
      job-name: ingress-nginx-admission-create
    name: ingress-nginx-admission-create-9njdn
    namespace: ingress-nginx
    ownerReferences:
    - apiVersion: batch/v1
      blockOwnerDeletion: true
      controller: true
      kind: Job
      name: ingress-nginx-admission-create
      uid: a2b9aa48-ccae-4428-a61a-d5bf41f99b4d
    resourceVersion: "872"
    uid: 121a3c53-291c-4e10-a912-55d762172ba4
  spec:
    containers:
    - args:
      - create
      - --host=ingress-nginx-controller-admission,ingress-nginx-controller-admission.$(POD_NAMESPACE).svc
      - --namespace=$(POD_NAMESPACE)
      - --secret-name=ingress-nginx-admission
      env:
      - name: POD_NAMESPACE
        valueFrom:
          fieldRef:
            apiVersion: v1
            fieldPath: metadata.namespace
      image: registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
      imagePullPolicy: IfNotPresent
      name: create
      resources: {}
      securityContext:
        allowPrivilegeEscalation: false
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-2r6gm
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    nodeSelector:
      kubernetes.io/os: linux
      minikube.k8s.io/primary: "true"
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: OnFailure
    schedulerName: default-scheduler
    securityContext:
      runAsNonRoot: true
      runAsUser: 2000
    serviceAccount: ingress-nginx-admission
    serviceAccountName: ingress-nginx-admission
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - name: kube-api-access-2r6gm
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T05:01:33Z"
      reason: PodCompleted
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T05:01:38Z"
      reason: PodCompleted
      status: "False"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T05:01:38Z"
      reason: PodCompleted
      status: "False"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T05:01:33Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://5801e1736c4fb3bf0fc570023dbbb8dfd663f09ee81ddc0ff3af40a072a3a5b7
      image: registry.k8s.io/ingress-nginx/kube-webhook-certgen@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
      imageID: docker-pullable://registry.k8s.io/ingress-nginx/kube-webhook-certgen@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
      lastState: {}
      name: create
      ready: false
      restartCount: 0
      started: false
      state:
        terminated:
          containerID: docker://5801e1736c4fb3bf0fc570023dbbb8dfd663f09ee81ddc0ff3af40a072a3a5b7
          exitCode: 0
          finishedAt: "2023-10-07T05:01:37Z"
          reason: Completed
          startedAt: "2023-10-07T05:01:37Z"
    hostIP: 192.168.49.2
    phase: Succeeded
    podIP: 10.244.0.5
    podIPs:
    - ip: 10.244.0.5
    qosClass: BestEffort
    startTime: "2023-10-07T05:01:33Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-07T05:01:33Z"
    generateName: ingress-nginx-admission-patch-
    labels:
      app.kubernetes.io/component: admission-webhook
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
      batch.kubernetes.io/controller-uid: eefc7d96-ec82-40ba-8743-e6c8850df2a6
      batch.kubernetes.io/job-name: ingress-nginx-admission-patch
      controller-uid: eefc7d96-ec82-40ba-8743-e6c8850df2a6
      job-name: ingress-nginx-admission-patch
    name: ingress-nginx-admission-patch-v2q8l
    namespace: ingress-nginx
    ownerReferences:
    - apiVersion: batch/v1
      blockOwnerDeletion: true
      controller: true
      kind: Job
      name: ingress-nginx-admission-patch
      uid: eefc7d96-ec82-40ba-8743-e6c8850df2a6
    resourceVersion: "871"
    uid: c8da6ab5-82ec-4b56-ad88-1c46e84f24a7
  spec:
    containers:
    - args:
      - patch
      - --webhook-name=ingress-nginx-admission
      - --namespace=$(POD_NAMESPACE)
      - --patch-mutating=false
      - --secret-name=ingress-nginx-admission
      - --patch-failure-policy=Fail
      env:
      - name: POD_NAMESPACE
        valueFrom:
          fieldRef:
            apiVersion: v1
            fieldPath: metadata.namespace
      image: registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
      imagePullPolicy: IfNotPresent
      name: patch
      resources: {}
      securityContext:
        allowPrivilegeEscalation: false
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-7fh8b
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    nodeSelector:
      kubernetes.io/os: linux
      minikube.k8s.io/primary: "true"
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: OnFailure
    schedulerName: default-scheduler
    securityContext:
      runAsNonRoot: true
      runAsUser: 2000
    serviceAccount: ingress-nginx-admission
    serviceAccountName: ingress-nginx-admission
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - name: kube-api-access-7fh8b
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T05:01:33Z"
      reason: PodCompleted
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T05:01:33Z"
      reason: PodCompleted
      status: "False"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T05:01:33Z"
      reason: PodCompleted
      status: "False"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T05:01:33Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://28ea55b83533a39b4bed007e2da01fc5e2c6f6e8270aba001ba0a76767e48563
      image: registry.k8s.io/ingress-nginx/kube-webhook-certgen@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
      imageID: docker-pullable://registry.k8s.io/ingress-nginx/kube-webhook-certgen@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
      lastState: {}
      name: patch
      ready: false
      restartCount: 0
      started: false
      state:
        terminated:
          containerID: docker://28ea55b83533a39b4bed007e2da01fc5e2c6f6e8270aba001ba0a76767e48563
          exitCode: 0
          finishedAt: "2023-10-07T05:01:37Z"
          reason: Completed
          startedAt: "2023-10-07T05:01:37Z"
    hostIP: 192.168.49.2
    phase: Succeeded
    podIP: 10.244.0.6
    podIPs:
    - ip: 10.244.0.6
    qosClass: BestEffort
    startTime: "2023-10-07T05:01:33Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-07T05:01:33Z"
    generateName: ingress-nginx-controller-7799c6795f-
    labels:
      app.kubernetes.io/component: controller
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
      gcp-auth-skip-secret: "true"
      pod-template-hash: 7799c6795f
    name: ingress-nginx-controller-7799c6795f-gs6bm
    namespace: ingress-nginx
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: ingress-nginx-controller-7799c6795f
      uid: 0a626897-98b5-423a-9738-5ef4ed967f01
    resourceVersion: "942"
    uid: 8c831b86-2f0f-48ae-bf9b-777eededeeda
  spec:
    containers:
    - args:
      - /nginx-ingress-controller
      - --election-id=ingress-nginx-leader
      - --controller-class=k8s.io/ingress-nginx
      - --watch-ingress-without-class=true
      - --configmap=$(POD_NAMESPACE)/ingress-nginx-controller
      - --tcp-services-configmap=$(POD_NAMESPACE)/tcp-services
      - --udp-services-configmap=$(POD_NAMESPACE)/udp-services
      - --validating-webhook=:8443
      - --validating-webhook-certificate=/usr/local/certificates/cert
      - --validating-webhook-key=/usr/local/certificates/key
      env:
      - name: POD_NAME
        valueFrom:
          fieldRef:
            apiVersion: v1
            fieldPath: metadata.name
      - name: POD_NAMESPACE
        valueFrom:
          fieldRef:
            apiVersion: v1
            fieldPath: metadata.namespace
      - name: LD_PRELOAD
        value: /usr/local/lib/libmimalloc.so
      image: registry.k8s.io/ingress-nginx/controller:v1.8.1@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd
      imagePullPolicy: IfNotPresent
      lifecycle:
        preStop:
          exec:
            command:
            - /wait-shutdown
      livenessProbe:
        failureThreshold: 5
        httpGet:
          path: /healthz
          port: 10254
          scheme: HTTP
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 1
      name: controller
      ports:
      - containerPort: 80
        hostPort: 80
        name: http
        protocol: TCP
      - containerPort: 443
        hostPort: 443
        name: https
        protocol: TCP
      - containerPort: 8443
        name: webhook
        protocol: TCP
      readinessProbe:
        failureThreshold: 3
        httpGet:
          path: /healthz
          port: 10254
          scheme: HTTP
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 1
      resources:
        requests:
          cpu: 100m
          memory: 90Mi
      securityContext:
        allowPrivilegeEscalation: true
        capabilities:
          add:
          - NET_BIND_SERVICE
          drop:
          - ALL
        runAsUser: 101
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /usr/local/certificates/
        name: webhook-cert
        readOnly: true
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-bpfsd
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    nodeSelector:
      kubernetes.io/os: linux
      minikube.k8s.io/primary: "true"
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: ingress-nginx
    serviceAccountName: ingress-nginx
    terminationGracePeriodSeconds: 0
    tolerations:
    - effect: NoSchedule
      key: node-role.kubernetes.io/master
      operator: Equal
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - name: webhook-cert
      secret:
        defaultMode: 420
        secretName: ingress-nginx-admission
    - name: kube-api-access-bpfsd
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T05:01:33Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T05:02:11Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T05:02:11Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T05:01:33Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://219a35e5e260bbfff6d36d9fe8c47e0f664e7700400ed1b55fa27a4116547489
      image: registry.k8s.io/ingress-nginx/controller@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd
      imageID: docker-pullable://registry.k8s.io/ingress-nginx/controller@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd
      lastState: {}
      name: controller
      ready: true
      restartCount: 0
      started: true
      state:
        running:
          startedAt: "2023-10-07T05:01:52Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 10.244.0.8
    podIPs:
    - ip: 10.244.0.8
    qosClass: Burstable
    startTime: "2023-10-07T05:01:33Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-07T04:55:35Z"
    generateName: coredns-5d78c9869d-
    labels:
      k8s-app: kube-dns
      pod-template-hash: 5d78c9869d
    name: coredns-5d78c9869d-hn7kp
    namespace: kube-system
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: coredns-5d78c9869d
      uid: a94b335b-d802-40e3-918c-9528f8ed5010
    resourceVersion: "405"
    uid: bfdd60b5-c2c8-4cf1-98c7-83700ae3a6cd
  spec:
    affinity:
      podAntiAffinity:
        preferredDuringSchedulingIgnoredDuringExecution:
        - podAffinityTerm:
            labelSelector:
              matchExpressions:
              - key: k8s-app
                operator: In
                values:
                - kube-dns
            topologyKey: kubernetes.io/hostname
          weight: 100
    containers:
    - args:
      - -conf
      - /etc/coredns/Corefile
      image: registry.k8s.io/coredns/coredns:v1.10.1
      imagePullPolicy: IfNotPresent
      livenessProbe:
        failureThreshold: 5
        httpGet:
          path: /health
          port: 8080
          scheme: HTTP
        initialDelaySeconds: 60
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 5
      name: coredns
      ports:
      - containerPort: 53
        name: dns
        protocol: UDP
      - containerPort: 53
        name: dns-tcp
        protocol: TCP
      - containerPort: 9153
        name: metrics
        protocol: TCP
      readinessProbe:
        failureThreshold: 3
        httpGet:
          path: /ready
          port: 8181
          scheme: HTTP
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 1
      resources:
        limits:
          memory: 170Mi
        requests:
          cpu: 100m
          memory: 70Mi
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          add:
          - NET_BIND_SERVICE
          drop:
          - all
        readOnlyRootFilesystem: true
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /etc/coredns
        name: config-volume
        readOnly: true
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-lwgzn
        readOnly: true
    dnsPolicy: Default
    enableServiceLinks: true
    nodeName: minikube
    nodeSelector:
      kubernetes.io/os: linux
    preemptionPolicy: PreemptLowerPriority
    priority: 2000000000
    priorityClassName: system-cluster-critical
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: coredns
    serviceAccountName: coredns
    terminationGracePeriodSeconds: 30
    tolerations:
    - key: CriticalAddonsOnly
      operator: Exists
    - effect: NoSchedule
      key: node-role.kubernetes.io/control-plane
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - configMap:
        defaultMode: 420
        items:
        - key: Corefile
          path: Corefile
        name: coredns
      name: config-volume
    - name: kube-api-access-lwgzn
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:35Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:36Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:36Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:35Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://664a6a20ac3a0b8ea2c6cf143b59c934e0d9f06e374b354329d5abca0b6e1797
      image: registry.k8s.io/coredns/coredns:v1.10.1
      imageID: docker-pullable://registry.k8s.io/coredns/coredns@sha256:a0ead06651cf580044aeb0a0feba63591858fb2e43ade8c9dea45a6a89ae7e5e
      lastState: {}
      name: coredns
      ready: true
      restartCount: 0
      started: true
      state:
        running:
          startedAt: "2023-10-07T04:55:35Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 10.244.0.2
    podIPs:
    - ip: 10.244.0.2
    qosClass: Burstable
    startTime: "2023-10-07T04:55:35Z"
- apiVersion: v1
  kind: Pod
  metadata:
    annotations:
      kubeadm.kubernetes.io/etcd.advertise-client-urls: https://192.168.49.2:2379
      kubernetes.io/config.hash: 8af0e85a28544808d52bb7c47ad824ed
      kubernetes.io/config.mirror: 8af0e85a28544808d52bb7c47ad824ed
      kubernetes.io/config.seen: "2023-10-07T04:55:22.216774375Z"
      kubernetes.io/config.source: file
    creationTimestamp: "2023-10-07T04:55:22Z"
    labels:
      component: etcd
      tier: control-plane
    name: etcd-minikube
    namespace: kube-system
    ownerReferences:
    - apiVersion: v1
      controller: true
      kind: Node
      name: minikube
      uid: 91f85c45-7c4e-4dc7-870f-0a255d59f79d
    resourceVersion: "324"
    uid: 51b6cd0f-4b45-43f8-8c49-166241e03eb0
  spec:
    containers:
    - command:
      - etcd
      - --advertise-client-urls=https://192.168.49.2:2379
      - --cert-file=/var/lib/minikube/certs/etcd/server.crt
      - --client-cert-auth=true
      - --data-dir=/var/lib/minikube/etcd
      - --experimental-initial-corrupt-check=true
      - --experimental-watch-progress-notify-interval=5s
      - --initial-advertise-peer-urls=https://192.168.49.2:2380
      - --initial-cluster=minikube=https://192.168.49.2:2380
      - --key-file=/var/lib/minikube/certs/etcd/server.key
      - --listen-client-urls=https://127.0.0.1:2379,https://192.168.49.2:2379
      - --listen-metrics-urls=http://127.0.0.1:2381
      - --listen-peer-urls=https://192.168.49.2:2380
      - --name=minikube
      - --peer-cert-file=/var/lib/minikube/certs/etcd/peer.crt
      - --peer-client-cert-auth=true
      - --peer-key-file=/var/lib/minikube/certs/etcd/peer.key
      - --peer-trusted-ca-file=/var/lib/minikube/certs/etcd/ca.crt
      - --proxy-refresh-interval=70000
      - --snapshot-count=10000
      - --trusted-ca-file=/var/lib/minikube/certs/etcd/ca.crt
      image: registry.k8s.io/etcd:3.5.7-0
      imagePullPolicy: IfNotPresent
      livenessProbe:
        failureThreshold: 8
        httpGet:
          host: 127.0.0.1
          path: /health?exclude=NOSPACE&serializable=true
          port: 2381
          scheme: HTTP
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 15
      name: etcd
      resources:
        requests:
          cpu: 100m
          memory: 100Mi
      startupProbe:
        failureThreshold: 24
        httpGet:
          host: 127.0.0.1
          path: /health?serializable=false
          port: 2381
          scheme: HTTP
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 15
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /var/lib/minikube/etcd
        name: etcd-data
      - mountPath: /var/lib/minikube/certs/etcd
        name: etcd-certs
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    hostNetwork: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 2000001000
    priorityClassName: system-node-critical
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext:
      seccompProfile:
        type: RuntimeDefault
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      operator: Exists
    volumes:
    - hostPath:
        path: /var/lib/minikube/certs/etcd
        type: DirectoryOrCreate
      name: etcd-certs
    - hostPath:
        path: /var/lib/minikube/etcd
        type: DirectoryOrCreate
      name: etcd-data
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:22Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:33Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:33Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:22Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://7170b8a5665111665ad4130d55d2c13cd9e34d4120c041d40d5eb1699dfc99d4
      image: registry.k8s.io/etcd:3.5.7-0
      imageID: docker-pullable://registry.k8s.io/etcd@sha256:51eae8381dcb1078289fa7b4f3df2630cdc18d09fb56f8e56b41c40e191d6c83
      lastState: {}
      name: etcd
      ready: true
      restartCount: 0
      started: true
      state:
        running:
          startedAt: "2023-10-07T04:55:17Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 192.168.49.2
    podIPs:
    - ip: 192.168.49.2
    qosClass: Burstable
    startTime: "2023-10-07T04:55:22Z"
- apiVersion: v1
  kind: Pod
  metadata:
    annotations:
      kubeadm.kubernetes.io/kube-apiserver.advertise-address.endpoint: 192.168.49.2:8443
      kubernetes.io/config.hash: f241819aff4d77a34fc71bea1fac9af8
      kubernetes.io/config.mirror: f241819aff4d77a34fc71bea1fac9af8
      kubernetes.io/config.seen: "2023-10-07T04:55:22.216777458Z"
      kubernetes.io/config.source: file
    creationTimestamp: "2023-10-07T04:55:22Z"
    labels:
      component: kube-apiserver
      tier: control-plane
    name: kube-apiserver-minikube
    namespace: kube-system
    ownerReferences:
    - apiVersion: v1
      controller: true
      kind: Node
      name: minikube
      uid: 91f85c45-7c4e-4dc7-870f-0a255d59f79d
    resourceVersion: "396"
    uid: 70f5f515-d17b-426d-ac17-e9d4c02b3bdc
  spec:
    containers:
    - command:
      - kube-apiserver
      - --advertise-address=192.168.49.2
      - --allow-privileged=true
      - --authorization-mode=Node,RBAC
      - --client-ca-file=/var/lib/minikube/certs/ca.crt
      - --enable-admission-plugins=NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,DefaultTolerationSeconds,NodeRestriction,MutatingAdmissionWebhook,ValidatingAdmissionWebhook,ResourceQuota
      - --enable-bootstrap-token-auth=true
      - --etcd-cafile=/var/lib/minikube/certs/etcd/ca.crt
      - --etcd-certfile=/var/lib/minikube/certs/apiserver-etcd-client.crt
      - --etcd-keyfile=/var/lib/minikube/certs/apiserver-etcd-client.key
      - --etcd-servers=https://127.0.0.1:2379
      - --kubelet-client-certificate=/var/lib/minikube/certs/apiserver-kubelet-client.crt
      - --kubelet-client-key=/var/lib/minikube/certs/apiserver-kubelet-client.key
      - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
      - --proxy-client-cert-file=/var/lib/minikube/certs/front-proxy-client.crt
      - --proxy-client-key-file=/var/lib/minikube/certs/front-proxy-client.key
      - --requestheader-allowed-names=front-proxy-client
      - --requestheader-client-ca-file=/var/lib/minikube/certs/front-proxy-ca.crt
      - --requestheader-extra-headers-prefix=X-Remote-Extra-
      - --requestheader-group-headers=X-Remote-Group
      - --requestheader-username-headers=X-Remote-User
      - --secure-port=8443
      - --service-account-issuer=https://kubernetes.default.svc.cluster.local
      - --service-account-key-file=/var/lib/minikube/certs/sa.pub
      - --service-account-signing-key-file=/var/lib/minikube/certs/sa.key
      - --service-cluster-ip-range=10.96.0.0/12
      - --tls-cert-file=/var/lib/minikube/certs/apiserver.crt
      - --tls-private-key-file=/var/lib/minikube/certs/apiserver.key
      image: registry.k8s.io/kube-apiserver:v1.27.4
      imagePullPolicy: IfNotPresent
      livenessProbe:
        failureThreshold: 8
        httpGet:
          host: 192.168.49.2
          path: /livez
          port: 8443
          scheme: HTTPS
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 15
      name: kube-apiserver
      readinessProbe:
        failureThreshold: 3
        httpGet:
          host: 192.168.49.2
          path: /readyz
          port: 8443
          scheme: HTTPS
        periodSeconds: 1
        successThreshold: 1
        timeoutSeconds: 15
      resources:
        requests:
          cpu: 250m
      startupProbe:
        failureThreshold: 24
        httpGet:
          host: 192.168.49.2
          path: /livez
          port: 8443
          scheme: HTTPS
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 15
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /etc/ssl/certs
        name: ca-certs
        readOnly: true
      - mountPath: /etc/ca-certificates
        name: etc-ca-certificates
        readOnly: true
      - mountPath: /var/lib/minikube/certs
        name: k8s-certs
        readOnly: true
      - mountPath: /usr/local/share/ca-certificates
        name: usr-local-share-ca-certificates
        readOnly: true
      - mountPath: /usr/share/ca-certificates
        name: usr-share-ca-certificates
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    hostNetwork: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 2000001000
    priorityClassName: system-node-critical
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext:
      seccompProfile:
        type: RuntimeDefault
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      operator: Exists
    volumes:
    - hostPath:
        path: /etc/ssl/certs
        type: DirectoryOrCreate
      name: ca-certs
    - hostPath:
        path: /etc/ca-certificates
        type: DirectoryOrCreate
      name: etc-ca-certificates
    - hostPath:
        path: /var/lib/minikube/certs
        type: DirectoryOrCreate
      name: k8s-certs
    - hostPath:
        path: /usr/local/share/ca-certificates
        type: DirectoryOrCreate
      name: usr-local-share-ca-certificates
    - hostPath:
        path: /usr/share/ca-certificates
        type: DirectoryOrCreate
      name: usr-share-ca-certificates
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:22Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:36Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:36Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:22Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://f316396f48f3dec57ed0c0b7fba8e031795b321c9ca09d2ebf8ca09380b786d9
      image: registry.k8s.io/kube-apiserver:v1.27.4
      imageID: docker-pullable://registry.k8s.io/kube-apiserver@sha256:697cd88d94f7f2ef42144cb3072b016dcb2e9251f0e7d41a7fede557e555452d
      lastState: {}
      name: kube-apiserver
      ready: true
      restartCount: 0
      started: true
      state:
        running:
          startedAt: "2023-10-07T04:55:18Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 192.168.49.2
    podIPs:
    - ip: 192.168.49.2
    qosClass: Burstable
    startTime: "2023-10-07T04:55:22Z"
- apiVersion: v1
  kind: Pod
  metadata:
    annotations:
      kubernetes.io/config.hash: b3702ceb912504d37098b922ccdcfa41
      kubernetes.io/config.mirror: b3702ceb912504d37098b922ccdcfa41
      kubernetes.io/config.seen: "2023-10-07T04:55:22.216778083Z"
      kubernetes.io/config.source: file
    creationTimestamp: "2023-10-07T04:55:22Z"
    labels:
      component: kube-controller-manager
      tier: control-plane
    name: kube-controller-manager-minikube
    namespace: kube-system
    ownerReferences:
    - apiVersion: v1
      controller: true
      kind: Node
      name: minikube
      uid: 91f85c45-7c4e-4dc7-870f-0a255d59f79d
    resourceVersion: "326"
    uid: 0980fe06-48a9-4afa-ab3d-cf443cca8302
  spec:
    containers:
    - command:
      - kube-controller-manager
      - --allocate-node-cidrs=true
      - --authentication-kubeconfig=/etc/kubernetes/controller-manager.conf
      - --authorization-kubeconfig=/etc/kubernetes/controller-manager.conf
      - --bind-address=127.0.0.1
      - --client-ca-file=/var/lib/minikube/certs/ca.crt
      - --cluster-cidr=10.244.0.0/16
      - --cluster-name=mk
      - --cluster-signing-cert-file=/var/lib/minikube/certs/ca.crt
      - --cluster-signing-key-file=/var/lib/minikube/certs/ca.key
      - --controllers=*,bootstrapsigner,tokencleaner
      - --kubeconfig=/etc/kubernetes/controller-manager.conf
      - --leader-elect=false
      - --requestheader-client-ca-file=/var/lib/minikube/certs/front-proxy-ca.crt
      - --root-ca-file=/var/lib/minikube/certs/ca.crt
      - --service-account-private-key-file=/var/lib/minikube/certs/sa.key
      - --service-cluster-ip-range=10.96.0.0/12
      - --use-service-account-credentials=true
      image: registry.k8s.io/kube-controller-manager:v1.27.4
      imagePullPolicy: IfNotPresent
      livenessProbe:
        failureThreshold: 8
        httpGet:
          host: 127.0.0.1
          path: /healthz
          port: 10257
          scheme: HTTPS
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 15
      name: kube-controller-manager
      resources:
        requests:
          cpu: 200m
      startupProbe:
        failureThreshold: 24
        httpGet:
          host: 127.0.0.1
          path: /healthz
          port: 10257
          scheme: HTTPS
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 15
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /etc/ssl/certs
        name: ca-certs
        readOnly: true
      - mountPath: /etc/ca-certificates
        name: etc-ca-certificates
        readOnly: true
      - mountPath: /usr/libexec/kubernetes/kubelet-plugins/volume/exec
        name: flexvolume-dir
      - mountPath: /var/lib/minikube/certs
        name: k8s-certs
        readOnly: true
      - mountPath: /etc/kubernetes/controller-manager.conf
        name: kubeconfig
        readOnly: true
      - mountPath: /usr/local/share/ca-certificates
        name: usr-local-share-ca-certificates
        readOnly: true
      - mountPath: /usr/share/ca-certificates
        name: usr-share-ca-certificates
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    hostNetwork: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 2000001000
    priorityClassName: system-node-critical
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext:
      seccompProfile:
        type: RuntimeDefault
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      operator: Exists
    volumes:
    - hostPath:
        path: /etc/ssl/certs
        type: DirectoryOrCreate
      name: ca-certs
    - hostPath:
        path: /etc/ca-certificates
        type: DirectoryOrCreate
      name: etc-ca-certificates
    - hostPath:
        path: /usr/libexec/kubernetes/kubelet-plugins/volume/exec
        type: DirectoryOrCreate
      name: flexvolume-dir
    - hostPath:
        path: /var/lib/minikube/certs
        type: DirectoryOrCreate
      name: k8s-certs
    - hostPath:
        path: /etc/kubernetes/controller-manager.conf
        type: FileOrCreate
      name: kubeconfig
    - hostPath:
        path: /usr/local/share/ca-certificates
        type: DirectoryOrCreate
      name: usr-local-share-ca-certificates
    - hostPath:
        path: /usr/share/ca-certificates
        type: DirectoryOrCreate
      name: usr-share-ca-certificates
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:22Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:33Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:33Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:22Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://d26e4550ee2acec133e088c9436cfc9bc53be26393b06f3a3aaf276ce1c74579
      image: registry.k8s.io/kube-controller-manager:v1.27.4
      imageID: docker-pullable://registry.k8s.io/kube-controller-manager@sha256:6286e500782ad6d0b37a1b8be57fc73f597dc931dfc73ff18ce534059803b265
      lastState: {}
      name: kube-controller-manager
      ready: true
      restartCount: 0
      started: true
      state:
        running:
          startedAt: "2023-10-07T04:55:17Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 192.168.49.2
    podIPs:
    - ip: 192.168.49.2
    qosClass: Burstable
    startTime: "2023-10-07T04:55:22Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-07T04:55:35Z"
    generateName: kube-proxy-
    labels:
      controller-revision-hash: 86cc8bcbf7
      k8s-app: kube-proxy
      pod-template-generation: "1"
    name: kube-proxy-n29nc
    namespace: kube-system
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: DaemonSet
      name: kube-proxy
      uid: 1c875214-7431-4829-99b4-5502a1a02072
    resourceVersion: "402"
    uid: 556a3e41-df02-4c2c-8aa3-68f2429c47d3
  spec:
    affinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchFields:
            - key: metadata.name
              operator: In
              values:
              - minikube
    containers:
    - command:
      - /usr/local/bin/kube-proxy
      - --config=/var/lib/kube-proxy/config.conf
      - --hostname-override=$(NODE_NAME)
      env:
      - name: NODE_NAME
        valueFrom:
          fieldRef:
            apiVersion: v1
            fieldPath: spec.nodeName
      image: registry.k8s.io/kube-proxy:v1.27.4
      imagePullPolicy: IfNotPresent
      name: kube-proxy
      resources: {}
      securityContext:
        privileged: true
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /var/lib/kube-proxy
        name: kube-proxy
      - mountPath: /run/xtables.lock
        name: xtables-lock
      - mountPath: /lib/modules
        name: lib-modules
        readOnly: true
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-l8bk2
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    hostNetwork: true
    nodeName: minikube
    nodeSelector:
      kubernetes.io/os: linux
    preemptionPolicy: PreemptLowerPriority
    priority: 2000001000
    priorityClassName: system-node-critical
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: kube-proxy
    serviceAccountName: kube-proxy
    terminationGracePeriodSeconds: 30
    tolerations:
    - operator: Exists
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
    - effect: NoSchedule
      key: node.kubernetes.io/disk-pressure
      operator: Exists
    - effect: NoSchedule
      key: node.kubernetes.io/memory-pressure
      operator: Exists
    - effect: NoSchedule
      key: node.kubernetes.io/pid-pressure
      operator: Exists
    - effect: NoSchedule
      key: node.kubernetes.io/unschedulable
      operator: Exists
    - effect: NoSchedule
      key: node.kubernetes.io/network-unavailable
      operator: Exists
    volumes:
    - configMap:
        defaultMode: 420
        name: kube-proxy
      name: kube-proxy
    - hostPath:
        path: /run/xtables.lock
        type: FileOrCreate
      name: xtables-lock
    - hostPath:
        path: /lib/modules
        type: ""
      name: lib-modules
    - name: kube-api-access-l8bk2
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:35Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:36Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:36Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:35Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://5d5f3888c739b39677ebdcc4e02bb490a47f13869286f1ebf881456224535646
      image: registry.k8s.io/kube-proxy:v1.27.4
      imageID: docker-pullable://registry.k8s.io/kube-proxy@sha256:4bcb707da9898d2625f5d4edc6d0c96519a24f16db914fc673aa8f97e41dbabf
      lastState: {}
      name: kube-proxy
      ready: true
      restartCount: 0
      started: true
      state:
        running:
          startedAt: "2023-10-07T04:55:35Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 192.168.49.2
    podIPs:
    - ip: 192.168.49.2
    qosClass: BestEffort
    startTime: "2023-10-07T04:55:35Z"
- apiVersion: v1
  kind: Pod
  metadata:
    annotations:
      kubernetes.io/config.hash: eb675835e10503c79265cf0e2983f93c
      kubernetes.io/config.mirror: eb675835e10503c79265cf0e2983f93c
      kubernetes.io/config.seen: "2023-10-07T04:55:22.216778500Z"
      kubernetes.io/config.source: file
    creationTimestamp: "2023-10-07T04:55:22Z"
    labels:
      component: kube-scheduler
      tier: control-plane
    name: kube-scheduler-minikube
    namespace: kube-system
    ownerReferences:
    - apiVersion: v1
      controller: true
      kind: Node
      name: minikube
      uid: 91f85c45-7c4e-4dc7-870f-0a255d59f79d
    resourceVersion: "319"
    uid: 4ebec80a-9dd4-4a1f-9bf1-bafca2621f63
  spec:
    containers:
    - command:
      - kube-scheduler
      - --authentication-kubeconfig=/etc/kubernetes/scheduler.conf
      - --authorization-kubeconfig=/etc/kubernetes/scheduler.conf
      - --bind-address=127.0.0.1
      - --kubeconfig=/etc/kubernetes/scheduler.conf
      - --leader-elect=false
      image: registry.k8s.io/kube-scheduler:v1.27.4
      imagePullPolicy: IfNotPresent
      livenessProbe:
        failureThreshold: 8
        httpGet:
          host: 127.0.0.1
          path: /healthz
          port: 10259
          scheme: HTTPS
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 15
      name: kube-scheduler
      resources:
        requests:
          cpu: 100m
      startupProbe:
        failureThreshold: 24
        httpGet:
          host: 127.0.0.1
          path: /healthz
          port: 10259
          scheme: HTTPS
        initialDelaySeconds: 10
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 15
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /etc/kubernetes/scheduler.conf
        name: kubeconfig
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    hostNetwork: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 2000001000
    priorityClassName: system-node-critical
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext:
      seccompProfile:
        type: RuntimeDefault
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      operator: Exists
    volumes:
    - hostPath:
        path: /etc/kubernetes/scheduler.conf
        type: FileOrCreate
      name: kubeconfig
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:22Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:29Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:29Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:22Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://16913bd26b35840132d4928295fb527d6a7dedb358df1c4b8c2ac582fa88262b
      image: registry.k8s.io/kube-scheduler:v1.27.4
      imageID: docker-pullable://registry.k8s.io/kube-scheduler@sha256:5897d7a97d23dce25cbf36fcd6e919180a8ef904bf5156583ffdb6a733ab04af
      lastState: {}
      name: kube-scheduler
      ready: true
      restartCount: 0
      started: true
      state:
        running:
          startedAt: "2023-10-07T04:55:17Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 192.168.49.2
    podIPs:
    - ip: 192.168.49.2
    qosClass: Burstable
    startTime: "2023-10-07T04:55:22Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-07T06:51:55Z"
    generateName: metrics-server-7746886d4f-
    labels:
      k8s-app: metrics-server
      pod-template-hash: 7746886d4f
    name: metrics-server-7746886d4f-jzhhf
    namespace: kube-system
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: metrics-server-7746886d4f
      uid: 18d938ae-24c4-4a00-98cd-1fb20d3764a6
    resourceVersion: "7738"
    uid: 7dfc0cae-94e4-4f2c-8f02-f62624027855
  spec:
    containers:
    - args:
      - --cert-dir=/tmp
      - --secure-port=4443
      - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
      - --kubelet-use-node-status-port
      - --metric-resolution=60s
      - --kubelet-insecure-tls
      image: registry.k8s.io/metrics-server/metrics-server:v0.6.4@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e
      imagePullPolicy: IfNotPresent
      livenessProbe:
        failureThreshold: 3
        httpGet:
          path: /livez
          port: https
          scheme: HTTPS
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 1
      name: metrics-server
      ports:
      - containerPort: 4443
        name: https
        protocol: TCP
      readinessProbe:
        failureThreshold: 3
        httpGet:
          path: /readyz
          port: https
          scheme: HTTPS
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 1
      resources:
        requests:
          cpu: 100m
          memory: 200Mi
      securityContext:
        readOnlyRootFilesystem: true
        runAsNonRoot: true
        runAsUser: 1000
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /tmp
        name: tmp-dir
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-bfc9x
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 2000000000
    priorityClassName: system-cluster-critical
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: metrics-server
    serviceAccountName: metrics-server
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - emptyDir: {}
      name: tmp-dir
    - name: kube-api-access-bfc9x
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T06:51:55Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T06:53:05Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T06:53:05Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T06:51:55Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://a1b732c9511f0f210c67a79bc3c53d1da9068bd1e6847eda3014ace71fc9cc77
      image: registry.k8s.io/metrics-server/metrics-server@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e
      imageID: docker-pullable://registry.k8s.io/metrics-server/metrics-server@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e
      lastState: {}
      name: metrics-server
      ready: true
      restartCount: 0
      started: true
      state:
        running:
          startedAt: "2023-10-07T06:51:58Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 10.244.0.19
    podIPs:
    - ip: 10.244.0.19
    qosClass: Burstable
    startTime: "2023-10-07T06:51:55Z"
- apiVersion: v1
  kind: Pod
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"v1","kind":"Pod","metadata":{"annotations":{},"labels":{"addonmanager.kubernetes.io/mode":"Reconcile","integration-test":"storage-provisioner"},"name":"storage-provisioner","namespace":"kube-system"},"spec":{"containers":[{"command":["/storage-provisioner"],"image":"gcr.io/k8s-minikube/storage-provisioner:v5","imagePullPolicy":"IfNotPresent","name":"storage-provisioner","volumeMounts":[{"mountPath":"/tmp","name":"tmp"}]}],"hostNetwork":true,"serviceAccountName":"storage-provisioner","volumes":[{"hostPath":{"path":"/tmp","type":"Directory"},"name":"tmp"}]}}
    creationTimestamp: "2023-10-07T04:55:23Z"
    labels:
      addonmanager.kubernetes.io/mode: Reconcile
      integration-test: storage-provisioner
    name: storage-provisioner
    namespace: kube-system
    resourceVersion: "413"
    uid: 2482c78a-7832-4d53-9342-f77bd89f2dd0
  spec:
    containers:
    - command:
      - /storage-provisioner
      image: gcr.io/k8s-minikube/storage-provisioner:v5
      imagePullPolicy: IfNotPresent
      name: storage-provisioner
      resources: {}
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /tmp
        name: tmp
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-wtplt
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    hostNetwork: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: storage-provisioner
    serviceAccountName: storage-provisioner
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - hostPath:
        path: /tmp
        type: Directory
      name: tmp
    - name: kube-api-access-wtplt
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:34Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:37Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:37Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2023-10-07T04:55:34Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://a7a559e16a32c9c7cd3c79c29ea54d9651258693c6d2db2ab9b76ba4fe30450b
      image: gcr.io/k8s-minikube/storage-provisioner:v5
      imageID: docker-pullable://gcr.io/k8s-minikube/storage-provisioner@sha256:18eb69d1418e854ad5a19e399310e52808a8321e4c441c1dddad8977a0d7a944
      lastState:
        terminated:
          containerID: docker://da5b1a32499678f9ca1674a626e7f10295b80ea3c2b6e124756d99e97a228ead
          exitCode: 1
          finishedAt: "2023-10-07T04:55:35Z"
          reason: Error
          startedAt: "2023-10-07T04:55:35Z"
      name: storage-provisioner
      ready: true
      restartCount: 1
      started: true
      state:
        running:
          startedAt: "2023-10-07T04:55:36Z"
    hostIP: 192.168.49.2
    phase: Running
    podIP: 192.168.49.2
    podIPs:
    - ip: 192.168.49.2
    qosClass: BestEffort
    startTime: "2023-10-07T04:55:34Z"
- apiVersion: v1
  kind: Service
  metadata:
    creationTimestamp: "2023-10-07T04:55:20Z"
    labels:
      component: apiserver
      provider: kubernetes
    name: kubernetes
    namespace: default
    resourceVersion: "231"
    uid: 6e2173cd-487d-4905-bbfc-a942144c6c3d
  spec:
    clusterIP: 10.96.0.1
    clusterIPs:
    - 10.96.0.1
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - name: https
      port: 443
      protocol: TCP
      targetPort: 8443
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      meta.helm.sh/release-name: fastapi-gpt2-release
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-07T17:39:30Z"
    labels:
      app.kubernetes.io/managed-by: Helm
    name: model-server-service
    namespace: default
    resourceVersion: "13997"
    uid: 5b2b8dcf-796a-4f95-8aeb-1842639046ce
  spec:
    clusterIP: 10.108.118.219
    clusterIPs:
    - 10.108.118.219
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - port: 9000
      protocol: TCP
      targetPort: 80
    selector:
      app: model-server
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      meta.helm.sh/release-name: fastapi-gpt2-release
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-07T17:39:30Z"
    labels:
      app: redis
      app.kubernetes.io/managed-by: Helm
      role: master
    name: redis-db-service
    namespace: default
    resourceVersion: "13989"
    uid: 085f3cca-23a8-4ea1-9676-3ee66ef6209c
  spec:
    clusterIP: 10.105.10.109
    clusterIPs:
    - 10.105.10.109
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - port: 6379
      protocol: TCP
      targetPort: 6379
    selector:
      app: redis
      role: master
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      meta.helm.sh/release-name: fastapi-gpt2-release
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-07T17:39:30Z"
    labels:
      app.kubernetes.io/managed-by: Helm
    name: web-server
    namespace: default
    resourceVersion: "13993"
    uid: d6458903-3576-4349-b58c-7e104d98c5db
  spec:
    clusterIP: 10.102.168.14
    clusterIPs:
    - 10.102.168.14
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - port: 8000
      protocol: TCP
      targetPort: 80
    selector:
      app: web-server
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-controller","namespace":"ingress-nginx"},"spec":{"ipFamilies":["IPv4"],"ipFamilyPolicy":"SingleStack","ports":[{"appProtocol":"http","name":"http","port":80,"protocol":"TCP","targetPort":"http"},{"appProtocol":"https","name":"https","port":443,"protocol":"TCP","targetPort":"https"}],"selector":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"type":"NodePort"}}
    creationTimestamp: "2023-10-07T05:01:33Z"
    labels:
      app.kubernetes.io/component: controller
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
    name: ingress-nginx-controller
    namespace: ingress-nginx
    resourceVersion: "798"
    uid: 8c941b03-c074-4dbe-bd12-ffab91344e3a
  spec:
    clusterIP: 10.108.93.69
    clusterIPs:
    - 10.108.93.69
    externalTrafficPolicy: Cluster
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - appProtocol: http
      name: http
      nodePort: 31705
      port: 80
      protocol: TCP
      targetPort: http
    - appProtocol: https
      name: https
      nodePort: 31226
      port: 443
      protocol: TCP
      targetPort: https
    selector:
      app.kubernetes.io/component: controller
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
    sessionAffinity: None
    type: NodePort
  status:
    loadBalancer: {}
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-controller-admission","namespace":"ingress-nginx"},"spec":{"ports":[{"appProtocol":"https","name":"https-webhook","port":443,"targetPort":"webhook"}],"selector":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"type":"ClusterIP"}}
    creationTimestamp: "2023-10-07T05:01:33Z"
    labels:
      app.kubernetes.io/component: controller
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
    name: ingress-nginx-controller-admission
    namespace: ingress-nginx
    resourceVersion: "802"
    uid: 577aeef0-6e53-4618-9a7d-939aa864c71e
  spec:
    clusterIP: 10.110.76.86
    clusterIPs:
    - 10.110.76.86
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - appProtocol: https
      name: https-webhook
      port: 443
      protocol: TCP
      targetPort: webhook
    selector:
      app.kubernetes.io/component: controller
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      prometheus.io/port: "9153"
      prometheus.io/scrape: "true"
    creationTimestamp: "2023-10-07T04:55:22Z"
    labels:
      k8s-app: kube-dns
      kubernetes.io/cluster-service: "true"
      kubernetes.io/name: CoreDNS
    name: kube-dns
    namespace: kube-system
    resourceVersion: "270"
    uid: e1fce9cc-e1a4-4c00-8ff3-ee07bbdd0c74
  spec:
    clusterIP: 10.96.0.10
    clusterIPs:
    - 10.96.0.10
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - name: dns
      port: 53
      protocol: UDP
      targetPort: 53
    - name: dns-tcp
      port: 53
      protocol: TCP
      targetPort: 53
    - name: metrics
      port: 9153
      protocol: TCP
      targetPort: 9153
    selector:
      k8s-app: kube-dns
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"labels":{"addonmanager.kubernetes.io/mode":"Reconcile","k8s-app":"metrics-server","kubernetes.io/minikube-addons":"metrics-server","kubernetes.io/minikube-addons-endpoint":"metrics-server","kubernetes.io/name":"Metrics-server"},"name":"metrics-server","namespace":"kube-system"},"spec":{"ports":[{"name":"https","port":443,"protocol":"TCP","targetPort":"https"}],"selector":{"k8s-app":"metrics-server"}}}
    creationTimestamp: "2023-10-07T06:51:55Z"
    labels:
      addonmanager.kubernetes.io/mode: Reconcile
      k8s-app: metrics-server
      kubernetes.io/minikube-addons: metrics-server
      kubernetes.io/minikube-addons-endpoint: metrics-server
      kubernetes.io/name: Metrics-server
    name: metrics-server
    namespace: kube-system
    resourceVersion: "7652"
    uid: d55aa6e2-cba6-467f-aeb2-dfb7e2144d2f
  spec:
    clusterIP: 10.107.194.147
    clusterIPs:
    - 10.107.194.147
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - name: https
      port: 443
      protocol: TCP
      targetPort: https
    selector:
      k8s-app: metrics-server
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
- apiVersion: apps/v1
  kind: DaemonSet
  metadata:
    annotations:
      deprecated.daemonset.template.generation: "1"
    creationTimestamp: "2023-10-07T04:55:22Z"
    generation: 1
    labels:
      k8s-app: kube-proxy
    name: kube-proxy
    namespace: kube-system
    resourceVersion: "404"
    uid: 1c875214-7431-4829-99b4-5502a1a02072
  spec:
    revisionHistoryLimit: 10
    selector:
      matchLabels:
        k8s-app: kube-proxy
    template:
      metadata:
        creationTimestamp: null
        labels:
          k8s-app: kube-proxy
      spec:
        containers:
        - command:
          - /usr/local/bin/kube-proxy
          - --config=/var/lib/kube-proxy/config.conf
          - --hostname-override=$(NODE_NAME)
          env:
          - name: NODE_NAME
            valueFrom:
              fieldRef:
                apiVersion: v1
                fieldPath: spec.nodeName
          image: registry.k8s.io/kube-proxy:v1.27.4
          imagePullPolicy: IfNotPresent
          name: kube-proxy
          resources: {}
          securityContext:
            privileged: true
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
          - mountPath: /var/lib/kube-proxy
            name: kube-proxy
          - mountPath: /run/xtables.lock
            name: xtables-lock
          - mountPath: /lib/modules
            name: lib-modules
            readOnly: true
        dnsPolicy: ClusterFirst
        hostNetwork: true
        nodeSelector:
          kubernetes.io/os: linux
        priorityClassName: system-node-critical
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        serviceAccount: kube-proxy
        serviceAccountName: kube-proxy
        terminationGracePeriodSeconds: 30
        tolerations:
        - operator: Exists
        volumes:
        - configMap:
            defaultMode: 420
            name: kube-proxy
          name: kube-proxy
        - hostPath:
            path: /run/xtables.lock
            type: FileOrCreate
          name: xtables-lock
        - hostPath:
            path: /lib/modules
            type: ""
          name: lib-modules
    updateStrategy:
      rollingUpdate:
        maxSurge: 0
        maxUnavailable: 1
      type: RollingUpdate
  status:
    currentNumberScheduled: 1
    desiredNumberScheduled: 1
    numberAvailable: 1
    numberMisscheduled: 0
    numberReady: 1
    observedGeneration: 1
    updatedNumberScheduled: 1
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    annotations:
      deployment.kubernetes.io/revision: "1"
      meta.helm.sh/release-name: fastapi-gpt2-release
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-07T17:39:30Z"
    generation: 1
    labels:
      app.kubernetes.io/managed-by: Helm
    name: model-server
    namespace: default
    resourceVersion: "14052"
    uid: c247a8d7-4df3-4aca-b459-0ce0bdf79ed8
  spec:
    progressDeadlineSeconds: 600
    replicas: 1
    revisionHistoryLimit: 10
    selector:
      matchLabels:
        app: model-server
    strategy:
      rollingUpdate:
        maxSurge: 25%
        maxUnavailable: 25%
      type: RollingUpdate
    template:
      metadata:
        creationTimestamp: null
        labels:
          app: model-server
      spec:
        containers:
        - env:
          - name: REDIS_HOST
            valueFrom:
              configMapKeyRef:
                key: hostname
                name: redis-config
          - name: REDIS_PORT
            valueFrom:
              configMapKeyRef:
                key: port
                name: redis-config
          - name: REDIS_PASSWORD
            valueFrom:
              secretKeyRef:
                key: db_password
                name: redis-secret
          - name: TIMM_MODEL
            valueFrom:
              configMapKeyRef:
                key: timm_model
                name: model-server-config
          image: model_server:latest
          imagePullPolicy: Never
          name: model-server
          ports:
          - containerPort: 80
            protocol: TCP
          resources: {}
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        terminationGracePeriodSeconds: 30
  status:
    availableReplicas: 1
    conditions:
    - lastTransitionTime: "2023-10-07T17:39:30Z"
      lastUpdateTime: "2023-10-07T17:39:30Z"
      message: Deployment has minimum availability.
      reason: MinimumReplicasAvailable
      status: "True"
      type: Available
    - lastTransitionTime: "2023-10-07T17:39:30Z"
      lastUpdateTime: "2023-10-07T17:39:30Z"
      message: ReplicaSet "model-server-b884894f4" has successfully progressed.
      reason: NewReplicaSetAvailable
      status: "True"
      type: Progressing
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
    updatedReplicas: 1
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    annotations:
      deployment.kubernetes.io/revision: "1"
      meta.helm.sh/release-name: fastapi-gpt2-release
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-07T17:39:30Z"
    generation: 1
    labels:
      app.kubernetes.io/managed-by: Helm
    name: redis-db
    namespace: default
    resourceVersion: "14085"
    uid: dbe00d53-bea7-4f9e-8863-a355e3cc43fc
  spec:
    progressDeadlineSeconds: 600
    replicas: 1
    revisionHistoryLimit: 10
    selector:
      matchLabels:
        app: redis
        role: master
    strategy:
      rollingUpdate:
        maxSurge: 25%
        maxUnavailable: 25%
      type: RollingUpdate
    template:
      metadata:
        creationTimestamp: null
        labels:
          app: redis
          role: master
      spec:
        containers:
        - args:
          - --requirepass
          - $(REDIS_PASSWORD)
          command:
          - redis-server
          env:
          - name: REDIS_PASSWORD
            valueFrom:
              secretKeyRef:
                key: db_password
                name: redis-secret
          image: redis:7.2.1
          imagePullPolicy: IfNotPresent
          name: redis-master
          ports:
          - containerPort: 6379
            protocol: TCP
          resources:
            limits:
              cpu: 200m
              memory: 200Mi
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
          - mountPath: /data
            name: redis-storage
        dnsPolicy: ClusterFirst
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        terminationGracePeriodSeconds: 30
        volumes:
        - name: redis-storage
          persistentVolumeClaim:
            claimName: redis-pvc
  status:
    availableReplicas: 1
    conditions:
    - lastTransitionTime: "2023-10-07T17:39:45Z"
      lastUpdateTime: "2023-10-07T17:39:45Z"
      message: Deployment has minimum availability.
      reason: MinimumReplicasAvailable
      status: "True"
      type: Available
    - lastTransitionTime: "2023-10-07T17:39:30Z"
      lastUpdateTime: "2023-10-07T17:39:45Z"
      message: ReplicaSet "redis-db-96b87bcb6" has successfully progressed.
      reason: NewReplicaSetAvailable
      status: "True"
      type: Progressing
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
    updatedReplicas: 1
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    annotations:
      deployment.kubernetes.io/revision: "1"
      meta.helm.sh/release-name: fastapi-gpt2-release
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-07T17:39:30Z"
    generation: 1
    labels:
      app: web-server
      app.kubernetes.io/managed-by: Helm
    name: web-server
    namespace: default
    resourceVersion: "14058"
    uid: 2a3467e1-979d-4f57-b486-43cdb0d56b81
  spec:
    progressDeadlineSeconds: 600
    replicas: 1
    revisionHistoryLimit: 10
    selector:
      matchLabels:
        app: web-server
    strategy:
      rollingUpdate:
        maxSurge: 25%
        maxUnavailable: 25%
      type: RollingUpdate
    template:
      metadata:
        creationTimestamp: null
        labels:
          app: web-server
      spec:
        containers:
        - env:
          - name: REDIS_HOST
            valueFrom:
              configMapKeyRef:
                key: hostname
                name: redis-config
          - name: REDIS_PORT
            valueFrom:
              configMapKeyRef:
                key: port
                name: redis-config
          - name: REDIS_PASSWORD
            valueFrom:
              secretKeyRef:
                key: db_password
                name: redis-secret
          - name: MODEL_SERVER_URL
            valueFrom:
              configMapKeyRef:
                key: model_server_url
                name: model-server-config
          image: web_server:latest
          imagePullPolicy: Never
          name: web-server
          ports:
          - containerPort: 80
            protocol: TCP
          resources: {}
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        terminationGracePeriodSeconds: 30
  status:
    availableReplicas: 1
    conditions:
    - lastTransitionTime: "2023-10-07T17:39:30Z"
      lastUpdateTime: "2023-10-07T17:39:30Z"
      message: Deployment has minimum availability.
      reason: MinimumReplicasAvailable
      status: "True"
      type: Available
    - lastTransitionTime: "2023-10-07T17:39:30Z"
      lastUpdateTime: "2023-10-07T17:39:30Z"
      message: ReplicaSet "web-server-5775b4b6bc" has successfully progressed.
      reason: NewReplicaSetAvailable
      status: "True"
      type: Progressing
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
    updatedReplicas: 1
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    annotations:
      deployment.kubernetes.io/revision: "1"
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-controller","namespace":"ingress-nginx"},"spec":{"minReadySeconds":0,"revisionHistoryLimit":10,"selector":{"matchLabels":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"}},"strategy":{"rollingUpdate":{"maxUnavailable":1},"type":"RollingUpdate"},"template":{"metadata":{"labels":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx","gcp-auth-skip-secret":"true"}},"spec":{"containers":[{"args":["/nginx-ingress-controller","--election-id=ingress-nginx-leader","--controller-class=k8s.io/ingress-nginx","--watch-ingress-without-class=true","--configmap=$(POD_NAMESPACE)/ingress-nginx-controller","--tcp-services-configmap=$(POD_NAMESPACE)/tcp-services","--udp-services-configmap=$(POD_NAMESPACE)/udp-services","--validating-webhook=:8443","--validating-webhook-certificate=/usr/local/certificates/cert","--validating-webhook-key=/usr/local/certificates/key"],"env":[{"name":"POD_NAME","valueFrom":{"fieldRef":{"fieldPath":"metadata.name"}}},{"name":"POD_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}},{"name":"LD_PRELOAD","value":"/usr/local/lib/libmimalloc.so"}],"image":"registry.k8s.io/ingress-nginx/controller:v1.8.1@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd","imagePullPolicy":"IfNotPresent","lifecycle":{"preStop":{"exec":{"command":["/wait-shutdown"]}}},"livenessProbe":{"failureThreshold":5,"httpGet":{"path":"/healthz","port":10254,"scheme":"HTTP"},"initialDelaySeconds":10,"periodSeconds":10,"successThreshold":1,"timeoutSeconds":1},"name":"controller","ports":[{"containerPort":80,"hostPort":80,"name":"http","protocol":"TCP"},{"containerPort":443,"hostPort":443,"name":"https","protocol":"TCP"},{"containerPort":8443,"name":"webhook","protocol":"TCP"}],"readinessProbe":{"failureThreshold":3,"httpGet":{"path":"/healthz","port":10254,"scheme":"HTTP"},"initialDelaySeconds":10,"periodSeconds":10,"successThreshold":1,"timeoutSeconds":1},"resources":{"requests":{"cpu":"100m","memory":"90Mi"}},"securityContext":{"allowPrivilegeEscalation":true,"capabilities":{"add":["NET_BIND_SERVICE"],"drop":["ALL"]},"runAsUser":101},"volumeMounts":[{"mountPath":"/usr/local/certificates/","name":"webhook-cert","readOnly":true}]}],"dnsPolicy":"ClusterFirst","nodeSelector":{"kubernetes.io/os":"linux","minikube.k8s.io/primary":"true"},"serviceAccountName":"ingress-nginx","terminationGracePeriodSeconds":0,"tolerations":[{"effect":"NoSchedule","key":"node-role.kubernetes.io/master","operator":"Equal"}],"volumes":[{"name":"webhook-cert","secret":{"secretName":"ingress-nginx-admission"}}]}}}}
    creationTimestamp: "2023-10-07T05:01:33Z"
    generation: 1
    labels:
      app.kubernetes.io/component: controller
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
    name: ingress-nginx-controller
    namespace: ingress-nginx
    resourceVersion: "948"
    uid: d5d55b4b-e455-418e-b654-a9b88b1978ef
  spec:
    progressDeadlineSeconds: 600
    replicas: 1
    revisionHistoryLimit: 10
    selector:
      matchLabels:
        app.kubernetes.io/component: controller
        app.kubernetes.io/instance: ingress-nginx
        app.kubernetes.io/name: ingress-nginx
    strategy:
      rollingUpdate:
        maxSurge: 25%
        maxUnavailable: 1
      type: RollingUpdate
    template:
      metadata:
        creationTimestamp: null
        labels:
          app.kubernetes.io/component: controller
          app.kubernetes.io/instance: ingress-nginx
          app.kubernetes.io/name: ingress-nginx
          gcp-auth-skip-secret: "true"
      spec:
        containers:
        - args:
          - /nginx-ingress-controller
          - --election-id=ingress-nginx-leader
          - --controller-class=k8s.io/ingress-nginx
          - --watch-ingress-without-class=true
          - --configmap=$(POD_NAMESPACE)/ingress-nginx-controller
          - --tcp-services-configmap=$(POD_NAMESPACE)/tcp-services
          - --udp-services-configmap=$(POD_NAMESPACE)/udp-services
          - --validating-webhook=:8443
          - --validating-webhook-certificate=/usr/local/certificates/cert
          - --validating-webhook-key=/usr/local/certificates/key
          env:
          - name: POD_NAME
            valueFrom:
              fieldRef:
                apiVersion: v1
                fieldPath: metadata.name
          - name: POD_NAMESPACE
            valueFrom:
              fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
          - name: LD_PRELOAD
            value: /usr/local/lib/libmimalloc.so
          image: registry.k8s.io/ingress-nginx/controller:v1.8.1@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd
          imagePullPolicy: IfNotPresent
          lifecycle:
            preStop:
              exec:
                command:
                - /wait-shutdown
          livenessProbe:
            failureThreshold: 5
            httpGet:
              path: /healthz
              port: 10254
              scheme: HTTP
            initialDelaySeconds: 10
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          name: controller
          ports:
          - containerPort: 80
            hostPort: 80
            name: http
            protocol: TCP
          - containerPort: 443
            hostPort: 443
            name: https
            protocol: TCP
          - containerPort: 8443
            name: webhook
            protocol: TCP
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: /healthz
              port: 10254
              scheme: HTTP
            initialDelaySeconds: 10
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          resources:
            requests:
              cpu: 100m
              memory: 90Mi
          securityContext:
            allowPrivilegeEscalation: true
            capabilities:
              add:
              - NET_BIND_SERVICE
              drop:
              - ALL
            runAsUser: 101
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
          - mountPath: /usr/local/certificates/
            name: webhook-cert
            readOnly: true
        dnsPolicy: ClusterFirst
        nodeSelector:
          kubernetes.io/os: linux
          minikube.k8s.io/primary: "true"
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        serviceAccount: ingress-nginx
        serviceAccountName: ingress-nginx
        terminationGracePeriodSeconds: 0
        tolerations:
        - effect: NoSchedule
          key: node-role.kubernetes.io/master
          operator: Equal
        volumes:
        - name: webhook-cert
          secret:
            defaultMode: 420
            secretName: ingress-nginx-admission
  status:
    availableReplicas: 1
    conditions:
    - lastTransitionTime: "2023-10-07T05:01:33Z"
      lastUpdateTime: "2023-10-07T05:01:33Z"
      message: Deployment has minimum availability.
      reason: MinimumReplicasAvailable
      status: "True"
      type: Available
    - lastTransitionTime: "2023-10-07T05:01:33Z"
      lastUpdateTime: "2023-10-07T05:02:11Z"
      message: ReplicaSet "ingress-nginx-controller-7799c6795f" has successfully progressed.
      reason: NewReplicaSetAvailable
      status: "True"
      type: Progressing
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
    updatedReplicas: 1
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    annotations:
      deployment.kubernetes.io/revision: "1"
    creationTimestamp: "2023-10-07T04:55:22Z"
    generation: 2
    labels:
      k8s-app: kube-dns
    name: coredns
    namespace: kube-system
    resourceVersion: "409"
    uid: 948b5592-0a5b-4db3-ae9e-57d2bac67441
  spec:
    progressDeadlineSeconds: 600
    replicas: 1
    revisionHistoryLimit: 10
    selector:
      matchLabels:
        k8s-app: kube-dns
    strategy:
      rollingUpdate:
        maxSurge: 25%
        maxUnavailable: 1
      type: RollingUpdate
    template:
      metadata:
        creationTimestamp: null
        labels:
          k8s-app: kube-dns
      spec:
        affinity:
          podAntiAffinity:
            preferredDuringSchedulingIgnoredDuringExecution:
            - podAffinityTerm:
                labelSelector:
                  matchExpressions:
                  - key: k8s-app
                    operator: In
                    values:
                    - kube-dns
                topologyKey: kubernetes.io/hostname
              weight: 100
        containers:
        - args:
          - -conf
          - /etc/coredns/Corefile
          image: registry.k8s.io/coredns/coredns:v1.10.1
          imagePullPolicy: IfNotPresent
          livenessProbe:
            failureThreshold: 5
            httpGet:
              path: /health
              port: 8080
              scheme: HTTP
            initialDelaySeconds: 60
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 5
          name: coredns
          ports:
          - containerPort: 53
            name: dns
            protocol: UDP
          - containerPort: 53
            name: dns-tcp
            protocol: TCP
          - containerPort: 9153
            name: metrics
            protocol: TCP
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: /ready
              port: 8181
              scheme: HTTP
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          resources:
            limits:
              memory: 170Mi
            requests:
              cpu: 100m
              memory: 70Mi
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              add:
              - NET_BIND_SERVICE
              drop:
              - all
            readOnlyRootFilesystem: true
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
          - mountPath: /etc/coredns
            name: config-volume
            readOnly: true
        dnsPolicy: Default
        nodeSelector:
          kubernetes.io/os: linux
        priorityClassName: system-cluster-critical
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        serviceAccount: coredns
        serviceAccountName: coredns
        terminationGracePeriodSeconds: 30
        tolerations:
        - key: CriticalAddonsOnly
          operator: Exists
        - effect: NoSchedule
          key: node-role.kubernetes.io/control-plane
        volumes:
        - configMap:
            defaultMode: 420
            items:
            - key: Corefile
              path: Corefile
            name: coredns
          name: config-volume
  status:
    availableReplicas: 1
    conditions:
    - lastTransitionTime: "2023-10-07T04:55:35Z"
      lastUpdateTime: "2023-10-07T04:55:35Z"
      message: Deployment has minimum availability.
      reason: MinimumReplicasAvailable
      status: "True"
      type: Available
    - lastTransitionTime: "2023-10-07T04:55:35Z"
      lastUpdateTime: "2023-10-07T04:55:36Z"
      message: ReplicaSet "coredns-5d78c9869d" has successfully progressed.
      reason: NewReplicaSetAvailable
      status: "True"
      type: Progressing
    observedGeneration: 2
    readyReplicas: 1
    replicas: 1
    updatedReplicas: 1
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    annotations:
      deployment.kubernetes.io/revision: "1"
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{},"labels":{"addonmanager.kubernetes.io/mode":"Reconcile","k8s-app":"metrics-server","kubernetes.io/minikube-addons":"metrics-server"},"name":"metrics-server","namespace":"kube-system"},"spec":{"selector":{"matchLabels":{"k8s-app":"metrics-server"}},"strategy":{"rollingUpdate":{"maxUnavailable":0}},"template":{"metadata":{"labels":{"k8s-app":"metrics-server"},"name":"metrics-server"},"spec":{"containers":[{"args":["--cert-dir=/tmp","--secure-port=4443","--kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname","--kubelet-use-node-status-port","--metric-resolution=60s","--kubelet-insecure-tls"],"image":"registry.k8s.io/metrics-server/metrics-server:v0.6.4@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e","imagePullPolicy":"IfNotPresent","livenessProbe":{"failureThreshold":3,"httpGet":{"path":"/livez","port":"https","scheme":"HTTPS"},"periodSeconds":10},"name":"metrics-server","ports":[{"containerPort":4443,"name":"https","protocol":"TCP"}],"readinessProbe":{"failureThreshold":3,"httpGet":{"path":"/readyz","port":"https","scheme":"HTTPS"},"periodSeconds":10},"resources":{"requests":{"cpu":"100m","memory":"200Mi"}},"securityContext":{"readOnlyRootFilesystem":true,"runAsNonRoot":true,"runAsUser":1000},"volumeMounts":[{"mountPath":"/tmp","name":"tmp-dir"}]}],"priorityClassName":"system-cluster-critical","serviceAccountName":"metrics-server","volumes":[{"emptyDir":{},"name":"tmp-dir"}]}}}}
    creationTimestamp: "2023-10-07T06:51:55Z"
    generation: 1
    labels:
      addonmanager.kubernetes.io/mode: Reconcile
      k8s-app: metrics-server
      kubernetes.io/minikube-addons: metrics-server
    name: metrics-server
    namespace: kube-system
    resourceVersion: "7743"
    uid: b41830f2-979a-4ae7-98c8-81e121159088
  spec:
    progressDeadlineSeconds: 600
    replicas: 1
    revisionHistoryLimit: 10
    selector:
      matchLabels:
        k8s-app: metrics-server
    strategy:
      rollingUpdate:
        maxSurge: 25%
        maxUnavailable: 0
      type: RollingUpdate
    template:
      metadata:
        creationTimestamp: null
        labels:
          k8s-app: metrics-server
        name: metrics-server
      spec:
        containers:
        - args:
          - --cert-dir=/tmp
          - --secure-port=4443
          - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
          - --kubelet-use-node-status-port
          - --metric-resolution=60s
          - --kubelet-insecure-tls
          image: registry.k8s.io/metrics-server/metrics-server:v0.6.4@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e
          imagePullPolicy: IfNotPresent
          livenessProbe:
            failureThreshold: 3
            httpGet:
              path: /livez
              port: https
              scheme: HTTPS
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          name: metrics-server
          ports:
          - containerPort: 4443
            name: https
            protocol: TCP
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: /readyz
              port: https
              scheme: HTTPS
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          resources:
            requests:
              cpu: 100m
              memory: 200Mi
          securityContext:
            readOnlyRootFilesystem: true
            runAsNonRoot: true
            runAsUser: 1000
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
          - mountPath: /tmp
            name: tmp-dir
        dnsPolicy: ClusterFirst
        priorityClassName: system-cluster-critical
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        serviceAccount: metrics-server
        serviceAccountName: metrics-server
        terminationGracePeriodSeconds: 30
        volumes:
        - emptyDir: {}
          name: tmp-dir
  status:
    availableReplicas: 1
    conditions:
    - lastTransitionTime: "2023-10-07T06:53:05Z"
      lastUpdateTime: "2023-10-07T06:53:05Z"
      message: Deployment has minimum availability.
      reason: MinimumReplicasAvailable
      status: "True"
      type: Available
    - lastTransitionTime: "2023-10-07T06:51:55Z"
      lastUpdateTime: "2023-10-07T06:53:05Z"
      message: ReplicaSet "metrics-server-7746886d4f" has successfully progressed.
      reason: NewReplicaSetAvailable
      status: "True"
      type: Progressing
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
    updatedReplicas: 1
- apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    annotations:
      deployment.kubernetes.io/desired-replicas: "1"
      deployment.kubernetes.io/max-replicas: "2"
      deployment.kubernetes.io/revision: "1"
      meta.helm.sh/release-name: fastapi-gpt2-release
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-07T17:39:30Z"
    generation: 1
    labels:
      app: model-server
      pod-template-hash: b884894f4
    name: model-server-b884894f4
    namespace: default
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: Deployment
      name: model-server
      uid: c247a8d7-4df3-4aca-b459-0ce0bdf79ed8
    resourceVersion: "14049"
    uid: ddde6321-ed1f-4e6c-945f-124bbd770503
  spec:
    replicas: 1
    selector:
      matchLabels:
        app: model-server
        pod-template-hash: b884894f4
    template:
      metadata:
        creationTimestamp: null
        labels:
          app: model-server
          pod-template-hash: b884894f4
      spec:
        containers:
        - env:
          - name: REDIS_HOST
            valueFrom:
              configMapKeyRef:
                key: hostname
                name: redis-config
          - name: REDIS_PORT
            valueFrom:
              configMapKeyRef:
                key: port
                name: redis-config
          - name: REDIS_PASSWORD
            valueFrom:
              secretKeyRef:
                key: db_password
                name: redis-secret
          - name: TIMM_MODEL
            valueFrom:
              configMapKeyRef:
                key: timm_model
                name: model-server-config
          image: model_server:latest
          imagePullPolicy: Never
          name: model-server
          ports:
          - containerPort: 80
            protocol: TCP
          resources: {}
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        terminationGracePeriodSeconds: 30
  status:
    availableReplicas: 1
    fullyLabeledReplicas: 1
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
- apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    annotations:
      deployment.kubernetes.io/desired-replicas: "1"
      deployment.kubernetes.io/max-replicas: "2"
      deployment.kubernetes.io/revision: "1"
      meta.helm.sh/release-name: fastapi-gpt2-release
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-07T17:39:30Z"
    generation: 1
    labels:
      app: redis
      pod-template-hash: 96b87bcb6
      role: master
    name: redis-db-96b87bcb6
    namespace: default
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: Deployment
      name: redis-db
      uid: dbe00d53-bea7-4f9e-8863-a355e3cc43fc
    resourceVersion: "14084"
    uid: 662b487b-877d-4799-bb2b-2048da2452e9
  spec:
    replicas: 1
    selector:
      matchLabels:
        app: redis
        pod-template-hash: 96b87bcb6
        role: master
    template:
      metadata:
        creationTimestamp: null
        labels:
          app: redis
          pod-template-hash: 96b87bcb6
          role: master
      spec:
        containers:
        - args:
          - --requirepass
          - $(REDIS_PASSWORD)
          command:
          - redis-server
          env:
          - name: REDIS_PASSWORD
            valueFrom:
              secretKeyRef:
                key: db_password
                name: redis-secret
          image: redis:7.2.1
          imagePullPolicy: IfNotPresent
          name: redis-master
          ports:
          - containerPort: 6379
            protocol: TCP
          resources:
            limits:
              cpu: 200m
              memory: 200Mi
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
          - mountPath: /data
            name: redis-storage
        dnsPolicy: ClusterFirst
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        terminationGracePeriodSeconds: 30
        volumes:
        - name: redis-storage
          persistentVolumeClaim:
            claimName: redis-pvc
  status:
    availableReplicas: 1
    fullyLabeledReplicas: 1
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
- apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    annotations:
      deployment.kubernetes.io/desired-replicas: "1"
      deployment.kubernetes.io/max-replicas: "2"
      deployment.kubernetes.io/revision: "1"
      meta.helm.sh/release-name: fastapi-gpt2-release
      meta.helm.sh/release-namespace: default
    creationTimestamp: "2023-10-07T17:39:30Z"
    generation: 1
    labels:
      app: web-server
      pod-template-hash: 5775b4b6bc
    name: web-server-5775b4b6bc
    namespace: default
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: Deployment
      name: web-server
      uid: 2a3467e1-979d-4f57-b486-43cdb0d56b81
    resourceVersion: "14056"
    uid: f4ec843e-4310-4641-8bc7-8fc54942f324
  spec:
    replicas: 1
    selector:
      matchLabels:
        app: web-server
        pod-template-hash: 5775b4b6bc
    template:
      metadata:
        creationTimestamp: null
        labels:
          app: web-server
          pod-template-hash: 5775b4b6bc
      spec:
        containers:
        - env:
          - name: REDIS_HOST
            valueFrom:
              configMapKeyRef:
                key: hostname
                name: redis-config
          - name: REDIS_PORT
            valueFrom:
              configMapKeyRef:
                key: port
                name: redis-config
          - name: REDIS_PASSWORD
            valueFrom:
              secretKeyRef:
                key: db_password
                name: redis-secret
          - name: MODEL_SERVER_URL
            valueFrom:
              configMapKeyRef:
                key: model_server_url
                name: model-server-config
          image: web_server:latest
          imagePullPolicy: Never
          name: web-server
          ports:
          - containerPort: 80
            protocol: TCP
          resources: {}
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        terminationGracePeriodSeconds: 30
  status:
    availableReplicas: 1
    fullyLabeledReplicas: 1
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
- apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    annotations:
      deployment.kubernetes.io/desired-replicas: "1"
      deployment.kubernetes.io/max-replicas: "2"
      deployment.kubernetes.io/revision: "1"
    creationTimestamp: "2023-10-07T05:01:33Z"
    generation: 1
    labels:
      app.kubernetes.io/component: controller
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
      gcp-auth-skip-secret: "true"
      pod-template-hash: 7799c6795f
    name: ingress-nginx-controller-7799c6795f
    namespace: ingress-nginx
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: Deployment
      name: ingress-nginx-controller
      uid: d5d55b4b-e455-418e-b654-a9b88b1978ef
    resourceVersion: "946"
    uid: 0a626897-98b5-423a-9738-5ef4ed967f01
  spec:
    replicas: 1
    selector:
      matchLabels:
        app.kubernetes.io/component: controller
        app.kubernetes.io/instance: ingress-nginx
        app.kubernetes.io/name: ingress-nginx
        pod-template-hash: 7799c6795f
    template:
      metadata:
        creationTimestamp: null
        labels:
          app.kubernetes.io/component: controller
          app.kubernetes.io/instance: ingress-nginx
          app.kubernetes.io/name: ingress-nginx
          gcp-auth-skip-secret: "true"
          pod-template-hash: 7799c6795f
      spec:
        containers:
        - args:
          - /nginx-ingress-controller
          - --election-id=ingress-nginx-leader
          - --controller-class=k8s.io/ingress-nginx
          - --watch-ingress-without-class=true
          - --configmap=$(POD_NAMESPACE)/ingress-nginx-controller
          - --tcp-services-configmap=$(POD_NAMESPACE)/tcp-services
          - --udp-services-configmap=$(POD_NAMESPACE)/udp-services
          - --validating-webhook=:8443
          - --validating-webhook-certificate=/usr/local/certificates/cert
          - --validating-webhook-key=/usr/local/certificates/key
          env:
          - name: POD_NAME
            valueFrom:
              fieldRef:
                apiVersion: v1
                fieldPath: metadata.name
          - name: POD_NAMESPACE
            valueFrom:
              fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
          - name: LD_PRELOAD
            value: /usr/local/lib/libmimalloc.so
          image: registry.k8s.io/ingress-nginx/controller:v1.8.1@sha256:e5c4824e7375fcf2a393e1c03c293b69759af37a9ca6abdb91b13d78a93da8bd
          imagePullPolicy: IfNotPresent
          lifecycle:
            preStop:
              exec:
                command:
                - /wait-shutdown
          livenessProbe:
            failureThreshold: 5
            httpGet:
              path: /healthz
              port: 10254
              scheme: HTTP
            initialDelaySeconds: 10
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          name: controller
          ports:
          - containerPort: 80
            hostPort: 80
            name: http
            protocol: TCP
          - containerPort: 443
            hostPort: 443
            name: https
            protocol: TCP
          - containerPort: 8443
            name: webhook
            protocol: TCP
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: /healthz
              port: 10254
              scheme: HTTP
            initialDelaySeconds: 10
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          resources:
            requests:
              cpu: 100m
              memory: 90Mi
          securityContext:
            allowPrivilegeEscalation: true
            capabilities:
              add:
              - NET_BIND_SERVICE
              drop:
              - ALL
            runAsUser: 101
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
          - mountPath: /usr/local/certificates/
            name: webhook-cert
            readOnly: true
        dnsPolicy: ClusterFirst
        nodeSelector:
          kubernetes.io/os: linux
          minikube.k8s.io/primary: "true"
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        serviceAccount: ingress-nginx
        serviceAccountName: ingress-nginx
        terminationGracePeriodSeconds: 0
        tolerations:
        - effect: NoSchedule
          key: node-role.kubernetes.io/master
          operator: Equal
        volumes:
        - name: webhook-cert
          secret:
            defaultMode: 420
            secretName: ingress-nginx-admission
  status:
    availableReplicas: 1
    fullyLabeledReplicas: 1
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
- apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    annotations:
      deployment.kubernetes.io/desired-replicas: "1"
      deployment.kubernetes.io/max-replicas: "2"
      deployment.kubernetes.io/revision: "1"
    creationTimestamp: "2023-10-07T04:55:35Z"
    generation: 1
    labels:
      k8s-app: kube-dns
      pod-template-hash: 5d78c9869d
    name: coredns-5d78c9869d
    namespace: kube-system
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: Deployment
      name: coredns
      uid: 948b5592-0a5b-4db3-ae9e-57d2bac67441
    resourceVersion: "406"
    uid: a94b335b-d802-40e3-918c-9528f8ed5010
  spec:
    replicas: 1
    selector:
      matchLabels:
        k8s-app: kube-dns
        pod-template-hash: 5d78c9869d
    template:
      metadata:
        creationTimestamp: null
        labels:
          k8s-app: kube-dns
          pod-template-hash: 5d78c9869d
      spec:
        affinity:
          podAntiAffinity:
            preferredDuringSchedulingIgnoredDuringExecution:
            - podAffinityTerm:
                labelSelector:
                  matchExpressions:
                  - key: k8s-app
                    operator: In
                    values:
                    - kube-dns
                topologyKey: kubernetes.io/hostname
              weight: 100
        containers:
        - args:
          - -conf
          - /etc/coredns/Corefile
          image: registry.k8s.io/coredns/coredns:v1.10.1
          imagePullPolicy: IfNotPresent
          livenessProbe:
            failureThreshold: 5
            httpGet:
              path: /health
              port: 8080
              scheme: HTTP
            initialDelaySeconds: 60
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 5
          name: coredns
          ports:
          - containerPort: 53
            name: dns
            protocol: UDP
          - containerPort: 53
            name: dns-tcp
            protocol: TCP
          - containerPort: 9153
            name: metrics
            protocol: TCP
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: /ready
              port: 8181
              scheme: HTTP
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          resources:
            limits:
              memory: 170Mi
            requests:
              cpu: 100m
              memory: 70Mi
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              add:
              - NET_BIND_SERVICE
              drop:
              - all
            readOnlyRootFilesystem: true
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
          - mountPath: /etc/coredns
            name: config-volume
            readOnly: true
        dnsPolicy: Default
        nodeSelector:
          kubernetes.io/os: linux
        priorityClassName: system-cluster-critical
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        serviceAccount: coredns
        serviceAccountName: coredns
        terminationGracePeriodSeconds: 30
        tolerations:
        - key: CriticalAddonsOnly
          operator: Exists
        - effect: NoSchedule
          key: node-role.kubernetes.io/control-plane
        volumes:
        - configMap:
            defaultMode: 420
            items:
            - key: Corefile
              path: Corefile
            name: coredns
          name: config-volume
  status:
    availableReplicas: 1
    fullyLabeledReplicas: 1
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
- apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    annotations:
      deployment.kubernetes.io/desired-replicas: "1"
      deployment.kubernetes.io/max-replicas: "2"
      deployment.kubernetes.io/revision: "1"
    creationTimestamp: "2023-10-07T06:51:55Z"
    generation: 1
    labels:
      k8s-app: metrics-server
      pod-template-hash: 7746886d4f
    name: metrics-server-7746886d4f
    namespace: kube-system
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: Deployment
      name: metrics-server
      uid: b41830f2-979a-4ae7-98c8-81e121159088
    resourceVersion: "7741"
    uid: 18d938ae-24c4-4a00-98cd-1fb20d3764a6
  spec:
    replicas: 1
    selector:
      matchLabels:
        k8s-app: metrics-server
        pod-template-hash: 7746886d4f
    template:
      metadata:
        creationTimestamp: null
        labels:
          k8s-app: metrics-server
          pod-template-hash: 7746886d4f
        name: metrics-server
      spec:
        containers:
        - args:
          - --cert-dir=/tmp
          - --secure-port=4443
          - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
          - --kubelet-use-node-status-port
          - --metric-resolution=60s
          - --kubelet-insecure-tls
          image: registry.k8s.io/metrics-server/metrics-server:v0.6.4@sha256:ee4304963fb035239bb5c5e8c10f2f38ee80efc16ecbdb9feb7213c17ae2e86e
          imagePullPolicy: IfNotPresent
          livenessProbe:
            failureThreshold: 3
            httpGet:
              path: /livez
              port: https
              scheme: HTTPS
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          name: metrics-server
          ports:
          - containerPort: 4443
            name: https
            protocol: TCP
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: /readyz
              port: https
              scheme: HTTPS
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          resources:
            requests:
              cpu: 100m
              memory: 200Mi
          securityContext:
            readOnlyRootFilesystem: true
            runAsNonRoot: true
            runAsUser: 1000
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
          - mountPath: /tmp
            name: tmp-dir
        dnsPolicy: ClusterFirst
        priorityClassName: system-cluster-critical
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        serviceAccount: metrics-server
        serviceAccountName: metrics-server
        terminationGracePeriodSeconds: 30
        volumes:
        - emptyDir: {}
          name: tmp-dir
  status:
    availableReplicas: 1
    fullyLabeledReplicas: 1
    observedGeneration: 1
    readyReplicas: 1
    replicas: 1
- apiVersion: batch/v1
  kind: Job
  metadata:
    annotations:
      batch.kubernetes.io/job-tracking: ""
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"batch/v1","kind":"Job","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"admission-webhook","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-admission-create","namespace":"ingress-nginx"},"spec":{"template":{"metadata":{"labels":{"app.kubernetes.io/component":"admission-webhook","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-admission-create"},"spec":{"containers":[{"args":["create","--host=ingress-nginx-controller-admission,ingress-nginx-controller-admission.$(POD_NAMESPACE).svc","--namespace=$(POD_NAMESPACE)","--secret-name=ingress-nginx-admission"],"env":[{"name":"POD_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}}],"image":"registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b","imagePullPolicy":"IfNotPresent","name":"create","securityContext":{"allowPrivilegeEscalation":false}}],"nodeSelector":{"kubernetes.io/os":"linux","minikube.k8s.io/primary":"true"},"restartPolicy":"OnFailure","securityContext":{"runAsNonRoot":true,"runAsUser":2000},"serviceAccountName":"ingress-nginx-admission"}}}}
    creationTimestamp: "2023-10-07T05:01:33Z"
    generation: 1
    labels:
      app.kubernetes.io/component: admission-webhook
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
    name: ingress-nginx-admission-create
    namespace: ingress-nginx
    resourceVersion: "874"
    uid: a2b9aa48-ccae-4428-a61a-d5bf41f99b4d
  spec:
    backoffLimit: 6
    completionMode: NonIndexed
    completions: 1
    parallelism: 1
    selector:
      matchLabels:
        batch.kubernetes.io/controller-uid: a2b9aa48-ccae-4428-a61a-d5bf41f99b4d
    suspend: false
    template:
      metadata:
        creationTimestamp: null
        labels:
          app.kubernetes.io/component: admission-webhook
          app.kubernetes.io/instance: ingress-nginx
          app.kubernetes.io/name: ingress-nginx
          batch.kubernetes.io/controller-uid: a2b9aa48-ccae-4428-a61a-d5bf41f99b4d
          batch.kubernetes.io/job-name: ingress-nginx-admission-create
          controller-uid: a2b9aa48-ccae-4428-a61a-d5bf41f99b4d
          job-name: ingress-nginx-admission-create
        name: ingress-nginx-admission-create
      spec:
        containers:
        - args:
          - create
          - --host=ingress-nginx-controller-admission,ingress-nginx-controller-admission.$(POD_NAMESPACE).svc
          - --namespace=$(POD_NAMESPACE)
          - --secret-name=ingress-nginx-admission
          env:
          - name: POD_NAMESPACE
            valueFrom:
              fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
          image: registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
          imagePullPolicy: IfNotPresent
          name: create
          resources: {}
          securityContext:
            allowPrivilegeEscalation: false
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        nodeSelector:
          kubernetes.io/os: linux
          minikube.k8s.io/primary: "true"
        restartPolicy: OnFailure
        schedulerName: default-scheduler
        securityContext:
          runAsNonRoot: true
          runAsUser: 2000
        serviceAccount: ingress-nginx-admission
        serviceAccountName: ingress-nginx-admission
        terminationGracePeriodSeconds: 30
  status:
    completionTime: "2023-10-07T05:01:40Z"
    conditions:
    - lastProbeTime: "2023-10-07T05:01:40Z"
      lastTransitionTime: "2023-10-07T05:01:40Z"
      status: "True"
      type: Complete
    ready: 0
    startTime: "2023-10-07T05:01:33Z"
    succeeded: 1
    uncountedTerminatedPods: {}
- apiVersion: batch/v1
  kind: Job
  metadata:
    annotations:
      batch.kubernetes.io/job-tracking: ""
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"batch/v1","kind":"Job","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"admission-webhook","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-admission-patch","namespace":"ingress-nginx"},"spec":{"template":{"metadata":{"labels":{"app.kubernetes.io/component":"admission-webhook","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-admission-patch"},"spec":{"containers":[{"args":["patch","--webhook-name=ingress-nginx-admission","--namespace=$(POD_NAMESPACE)","--patch-mutating=false","--secret-name=ingress-nginx-admission","--patch-failure-policy=Fail"],"env":[{"name":"POD_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}}],"image":"registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b","imagePullPolicy":"IfNotPresent","name":"patch","securityContext":{"allowPrivilegeEscalation":false}}],"nodeSelector":{"kubernetes.io/os":"linux","minikube.k8s.io/primary":"true"},"restartPolicy":"OnFailure","securityContext":{"runAsNonRoot":true,"runAsUser":2000},"serviceAccountName":"ingress-nginx-admission"}}}}
    creationTimestamp: "2023-10-07T05:01:33Z"
    generation: 1
    labels:
      app.kubernetes.io/component: admission-webhook
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
    name: ingress-nginx-admission-patch
    namespace: ingress-nginx
    resourceVersion: "873"
    uid: eefc7d96-ec82-40ba-8743-e6c8850df2a6
  spec:
    backoffLimit: 6
    completionMode: NonIndexed
    completions: 1
    parallelism: 1
    selector:
      matchLabels:
        batch.kubernetes.io/controller-uid: eefc7d96-ec82-40ba-8743-e6c8850df2a6
    suspend: false
    template:
      metadata:
        creationTimestamp: null
        labels:
          app.kubernetes.io/component: admission-webhook
          app.kubernetes.io/instance: ingress-nginx
          app.kubernetes.io/name: ingress-nginx
          batch.kubernetes.io/controller-uid: eefc7d96-ec82-40ba-8743-e6c8850df2a6
          batch.kubernetes.io/job-name: ingress-nginx-admission-patch
          controller-uid: eefc7d96-ec82-40ba-8743-e6c8850df2a6
          job-name: ingress-nginx-admission-patch
        name: ingress-nginx-admission-patch
      spec:
        containers:
        - args:
          - patch
          - --webhook-name=ingress-nginx-admission
          - --namespace=$(POD_NAMESPACE)
          - --patch-mutating=false
          - --secret-name=ingress-nginx-admission
          - --patch-failure-policy=Fail
          env:
          - name: POD_NAMESPACE
            valueFrom:
              fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
          image: registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
          imagePullPolicy: IfNotPresent
          name: patch
          resources: {}
          securityContext:
            allowPrivilegeEscalation: false
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        nodeSelector:
          kubernetes.io/os: linux
          minikube.k8s.io/primary: "true"
        restartPolicy: OnFailure
        schedulerName: default-scheduler
        securityContext:
          runAsNonRoot: true
          runAsUser: 2000
        serviceAccount: ingress-nginx-admission
        serviceAccountName: ingress-nginx-admission
        terminationGracePeriodSeconds: 30
  status:
    completionTime: "2023-10-07T05:01:40Z"
    conditions:
    - lastProbeTime: "2023-10-07T05:01:40Z"
      lastTransitionTime: "2023-10-07T05:01:40Z"
      status: "True"
      type: Complete
    ready: 0
    startTime: "2023-10-07T05:01:33Z"
    succeeded: 1
    uncountedTerminatedPods: {}
kind: List
metadata:
  resourceVersion: ""
➜  ~ 
```