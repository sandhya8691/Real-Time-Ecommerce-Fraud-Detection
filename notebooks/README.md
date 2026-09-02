# Real-Time E-Commerce Fraud Detection

## 📌 Project Overview

Real-Time E-Commerce Fraud Detection is a Machine Learning based system designed to identify potentially fraudulent e-commerce transactions.

The system analyzes transaction-related features such as transaction amount, payment method, customer behavior, device information, location changes, failed transactions, and transaction timing to predict whether a transaction is fraudulent.

The trained Machine Learning model is integrated with a **FastAPI REST API** for real-time fraud prediction.

---

## 🎯 Project Objectives

* Detect fraudulent e-commerce transactions
* Analyze customer transaction behavior
* Engineer meaningful fraud-related features
* Compare multiple Machine Learning models
* Deploy the best model through a REST API
* Provide fraud probability and risk level
* Validate API inputs for reliable predictions

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* FastAPI
* Uvicorn
* Pydantic
* Joblib
* Jupyter Notebook
* Git & GitHub

---

## 📊 Dataset

The project uses a synthetic e-commerce transaction dataset containing **50,000 transactions**.

The dataset includes information about:

* Transaction amount
* Payment method
* Product category
* Customer age
* Account age
* Device type
* Customer location
* Previous transactions
* Failed transactions
* New device indicator
* New location indicator
* Night transaction indicator
* Fraud label

---

## ⚙️ Feature Engineering

The following features were created to improve fraud detection:

* `transaction_hour`
* `amount_log`
* `failure_rate`
* `customer_avg_amount`
* `amount_deviation`
* `risk_signal_score`

These features help the model identify unusual transaction behavior.

---

## 🤖 Machine Learning Models

Two classification models were evaluated:

1. Logistic Regression
2. Random Forest Classifier

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

### 🏆 Best Model

**Random Forest Classifier**

---

## 📈 Model Performance

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 96.36% |
| Precision | 89.62% |
| Recall    | 97.68% |
| F1 Score  | 93.47% |
| ROC-AUC   | 99.61% |

The high recall indicates that the model is effective at identifying fraudulent transactions.

---

## 🚀 API Features

The FastAPI backend provides:

### Health Check

```text
GET /health
```

Checks whether the API and trained model are available.

### Fraud Prediction

```text
POST /predict
```

Returns:

* Fraud / Non-Fraud prediction
* Fraud probability
* Fraud percentage
* Risk level

Risk levels:

* LOW
* MEDIUM
* HIGH

---

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
├── venv/
│
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Activate Virtual Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Start FastAPI Server

From the project root:

```powershell
uvicorn api.main:app --reload
```

### 3. Open API

Open the following address in your browser:

```text
http://127.0.0.1:8000
```

### 4. Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

Use Swagger UI to test the `/predict` endpoint.

---

## 🔍 Example API Response

```json
{
    "prediction": "FRAUD",
    "fraud_probability": 0.9498,
    "fraud_percentage": "94.98%",
    "risk_level": "HIGH"
}
```

---

## 💡 Business Value

This system can help e-commerce businesses:

* Identify suspicious transactions
* Reduce potential financial losses
* Detect unusual customer behavior
* Support real-time transaction monitoring
* Improve fraud investigation workflows

---

## 🔮 Future Improvements

Possible future enhancements include:

* Real-time transaction streaming
* XGBoost model comparison
* Model monitoring
* Automated retraining
* Database integration
* Docker deployment
* Cloud deployment
* Fraud monitoring dashboard
* Authentication and API security

---

## 👩‍💻 Author

**Sandhyarani Sahu**

Machine Learning | Data Analytics | Python | SQL | Power BI
