# Smart Error Log Analyzer 🔍🤖

A Django web application that classifies server error logs using machine learning (Naive Bayes) and suggests fixes.

## Features ✨
- Classifies error types (Network, Database, Storage, etc.)
- Provides instant fix suggestions
- Simple web interface for quick analysis
- Beginner-friendly Django + ML integration


## Setup Guide 🛠️

### 1. Clone the Repository
```bash
git clone https://github.com/jihane01/log-analyzer-django-ml.git
cd log-analyzer-django-ml

###  Install Dependencies
pip install -r requirements.txt
### Run Django Server
python manage.py migrate
python manage.py runserver

Open your browser to:
👉 http://127.0.0.1:8000/


Troubleshooting ⚠️
Issue: "Model file not found"
Fix: Run python analyzer/ml_model.py to generate model files

You are welcome to Contribute 🤝
