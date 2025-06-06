# CSY3056 Flask CI/CD Project



## 📌 Features

- RESTful Flask web service
- Unit testing using pytest
- CI/CD pipeline with Jenkins
- Docker-based containerization
- Kubernetes-based deployment with LoadBalancer service

## 🗂 Project Structure

```
.
├── app/
│   └── main.py
├── tests/
│   └── test_main.py
├── k8s/
│   └── deployment.yaml
├── requirements.txt
├── Dockerfile
└── Jenkinsfile
```

## 🚀 Getting Started

### Clone and Setup

```bash
git clone https://github.com/vonx323/csy3056-cicd-flask-app.git
cd csy3056-cicd-flask-app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run the Flask App

```bash
python app/main.py
```

### Run Tests

```bash
pytest tests/
```

### Build and Run with Docker

```bash
docker build -t csy3056-flask-app .
docker run -p 5000:5000 csy3056-flask-app
```

### Kubernetes Deployment

```bash
kubectl apply -f k8s/deployment.yaml
```

## 🛠 CI/CD Workflow

The Jenkins pipeline includes:
1. GitHub code checkout
2. Dependency installation
3. Unit testing via pytest
4. Docker image build
5. Image push to Docker Hub
6. Deployment to Kubernetes

## 👤 Author

- **Paoulo**
- CSY3056 - University of Northampton

## 📜 License

For educational use only.