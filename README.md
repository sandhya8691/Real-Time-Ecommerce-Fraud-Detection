# Real-Time E-Commerce Fraud Detection

A Machine Learning based fraud detection system for identifying potentially fraudulent e-commerce transactions in real time.

## 📌 Project Overview

This project uses Machine Learning to analyze e-commerce transaction data and predict whether a transaction is fraudulent or non-fraudulent.

The trained model is deployed using FastAPI and provides real-time fraud predictions through a REST API.

## 🎯 Objectives

- Detect fraudulent e-commerce transactions
- Perform data preprocessing and feature engineering
- Handle imbalanced fraud data
- Compare Machine Learning models
- Select the best-performing model
- Deploy the model using FastAPI
- Provide real-time fraud prediction

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Logistic Regression
- Random Forest
- XGBoost
- Matplotlib
- Seaborn
- Plotly
- FastAPI
- Pydantic
- Uvicorn
- Jupyter Notebook
- Git & GitHub

## 📊 Dataset

The project uses a synthetic e-commerce transaction dataset containing 50,000 transactions.

The dataset contains transaction, customer, payment, device, location and fraud-related information.

## ⚙️ Feature Engineering

The following features were created:

- Transaction Hour
- Log Transaction Amount
- Failure Rate
- Customer Average Amount
- Amount Deviation
- Risk Signal Score

## 🤖 Machine Learning Models

Two classification models were evaluated:

1. Logistic Regression
2. Random Forest Classifier

Random Forest was selected as the final model based on ROC-AUC performance.

## 📈 Final Model Performance

| Metric | Score |
|---|---:|
| Accuracy | 96.36% |
| Precision | 89.62% |
| Recall | 97.68% |
| F1 Score | 93.47% |
| ROC-AUC | 99.61% |

**Final Model: Random Forest Classifier**

## 🌐 FastAPI

The trained Machine Learning model is deployed using FastAPI.

The API provides:

- Fraud / Non-Fraud prediction
- Fraud probability
- Fraud percentage
- Risk level
- Input validation
- Health check
- Interactive Swagger documentation

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API status |
| GET | `/health` | Health check |
| POST | `/predict` | Fraud prediction |

## 📁 Project Structure

```text
Real-Time-Ecommerce-Fraud-Detection/
│
├── api/
│   └── main.py
│
├── data/
│   ├── transactions.csv
│   └── transactions_featured.csv
│
├── models/
│   ├── fraud_detection_model.pkl
│   └── final_model_performance.csv
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── create_dataset.py
├── requirements.txt
├── .gitignore
└── README.md
