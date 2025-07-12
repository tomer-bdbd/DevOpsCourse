# DevOps Course

A simple Flask web application deployed on Kubernetes with autoscaling and monitoring.

## Setup Kubernetes Cluster

### Using Minikube

1. Start minikube:
   ```bash
   minikube start
   ```

2. Enable metrics server:
   ```bash
   minikube addons enable metrics-server
   ```

3. Check cluster is running:
   ```bash
   kubectl get nodes
   ```

## Deploy Application

1. Deploy all resources:
   ```bash
   kubectl apply -f k8s/
   ```

2. Check deployment status:
   ```bash
   kubectl get pods
   kubectl get services
   ```

## Access Application

1. Get service URL:
   ```bash
   minikube service getuser-service --url
   ```

2. Or use port forwarding:
   ```bash
   kubectl port-forward service/getuser-service 8080:80
   ```
   Then go to `http://localhost:8080`

## Clean up

```bash
kubectl delete -f k8s/
```
