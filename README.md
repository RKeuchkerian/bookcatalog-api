# 📚 Book Catalog API – DevOps Diploma 2025

A RESTful API built with Django and automatically deployed to Kubernetes using a complete CI/CD pipeline.

---

## 🧠 Overview

This application allows users to manage a catalog of books via REST endpoints. It was developed as part of the final capstone project for the DevOps Diploma 2025.

Key features:

- Django REST API with full CRUD support
- Docker containerization
- Automated deployment via Helm + ArgoCD
- Full GitHub Actions CI/CD pipeline
- Reusable and configurable Helm chart

---

## 🚀 Main API Endpoints

| Method | Path                   | Description                  |
|--------|------------------------|------------------------------|
| GET    | `/api/books/`          | List all books               |
| POST   | `/api/books/`          | Create a new book            |
| GET    | `/api/books/<id>/`     | Retrieve book details        |
| PUT    | `/api/books/<id>/`     | Update book info             |
| DELETE | `/api/books/<id>/`     | Delete a book                |
| GET    | `/api/health/`         | Check API health             |

---

## ⚙️ Requirements

- Docker
- docker-compose
- Python 3.10+
- Helm
- kubectl
- k3d or Minikube
- ArgoCD (if using GitOps)

---

## 🧪 Running Locally

```bash
# Clone the repo
git clone https://github.com/<your_username>/<repo>.git
cd <repo>

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Start development server
python manage.py runserver


## 👤 Author

Romina  
Capstone Project – DevOps Diploma 2025
