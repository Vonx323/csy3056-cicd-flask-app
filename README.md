CSY3056 - CI/CD Pipeline for Flask Web Application

Project Overview

This project demonstrates a full DevOps pipeline for a Flask-based web application. It includes code development, automated testing, Docker containerization, and Kubernetes deployment through a Jenkins-managed CI/CD pipeline.

Features

Simple Python Flask web service

Unit testing with pytest

Code linting with flake8

Docker container with slim Python base

CI/CD with Jenkins pipeline

Kubernetes deployment with health checks and resource limits

File Structure

.
├── app/
│   └── main.py              # Flask application code
├── tests/
│   └── test_main.py         # Unit tests for Flask app
├── Dockerfile               # Docker build instructions
├── Jenkinsfile              # Jenkins pipeline definition
├── requirements.txt         # Python dependencies
└── k8s/
    └── deployment.yaml      # Kubernetes deployment manifest

Prerequisites

Python 3.10+

Docker

Jenkins (with Docker and Git)

Kubernetes cluster (e.g., Minikube or cloud provider)

Running Locally

# Set up environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Run the Flask app
python app/main.py

Visit: http://localhost:5000

Run Tests

pytest tests/ --cov=app

Docker Commands

# Build Docker image
docker build -t flask_app_image .

# Run container
docker run -d -p 5000:5000 flask_app_image

CI/CD Pipeline

Triggered via Jenkins on source code changes.

Lint, test, build Docker image, push to DockerHub.

Kubernetes deployment using kubectl apply.

Kubernetes Deployment

kubectl apply -f k8s/deployment.yaml
kubectl get pods
kubectl get svc

Health check endpoint: /health

Maintainer

Paoulo AgkoStudent ID: 21418507

