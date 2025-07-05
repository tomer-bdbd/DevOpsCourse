# GetUser Web Application

A simple web application that displays the current username in a designed web interface.

## Installation

### Docker (local)

1. Build the image:
   ```bash
   docker build -t getuser:latest .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 getuser:latest
   ```

3. Access the web UI at `http://localhost:5000`

### Kubernetes

1. Deploy using the provided manifests:
   ```bash
   kubectl apply -f getuser-dep.yaml
   kubectl apply -f getuser-service.yaml
   ```

2. Access the service (depending on your cluster setup):
   ```bash
   kubectl get service getuser-service
   ```

3. When using minikube or similar, expose the service online using:
   ```bash
   kubectl port-forward service/getuser-service 8080:80 --address=0.0.0.0
   ```
   Then go to ```http://<external-ip>:8080```