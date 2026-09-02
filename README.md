# Real-Time E-Commerce Fraud Detection

A Machine Learning based fraud detection system for identifying potentially fraudulent e-commerce transactions in real time.

## 🚀 Project Overview

This project uses Machine Learning to analyze e-commerce transaction data and predict whether a transaction is fraudulent or non-fraudulent.

The trained model is deployed through a FastAPI REST API, allowing users or applications to send transaction details and receive a fraud prediction, probability, and risk level.

## 🎯 Objectives

- Detect fraudulent e-commerce transactions
- Handle imbalanced fraud data using class balancing
- Perform feature engineering
- Compare multiple Machine Learning models
- Deploy the trained model using FastAPI
- Provide real-time fraud prediction through REST API

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest
- Logistic Regression
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

The dataset includes transaction amount, payment method, product category, customer age, account age, device information, location information, transaction history, and fraud indicators.

## ⚙️ Feature Engineering

The following additional features were created:

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

The Random Forest model was selected as the final model based on ROC-AUC performance.

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
- Health check endpoint
- Interactive Swagger documentation

### API Endpoints

```text
GET  /
GET  /health
POST /predict