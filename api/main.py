from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
import pandas as pd
import numpy as np
import joblib


# Load trained model
model = joblib.load("models/fraud_detection_model.pkl")

app = FastAPI(
    title="Real-Time E-Commerce Fraud Detection API",
    description="""
    Machine Learning powered API for detecting fraudulent e-commerce transactions.

    The API analyzes transaction features and returns:
    - Fraud / Non-Fraud prediction
    - Fraud probability
    - Fraud percentage
    - Risk level
    """,
    version="1.0.0",
    contact={
        "name": "E-Commerce Fraud Detection Project"
    }
)

class Transaction(BaseModel):
    transaction_amount: float = Field(
        gt=0,
        description="Transaction amount",
        example=1200.50
    )

    payment_method: str = Field(
        description="Payment method",
        example="Credit Card"
    )

    product_category: str = Field(
        description="Product category",
        example="Electronics"
    )

    customer_age: int = Field(
        ge=18,
        le=100,
        description="Customer age",
        example=25
    )

    account_age_days: int = Field(
        ge=0,
        description="Account age in days",
        example=15
    )

    device_type: str = Field(
        description="Device used for transaction",
        example="Mobile"
    )

    customer_location: str = Field(
        description="Customer location",
        example="Bhubaneswar"
    )

    previous_transaction_count: int = Field(
        ge=0,
        description="Number of previous transactions",
        example=5
    )

    failed_transaction_count: int = Field(
        ge=0,
        description="Number of failed transactions",
        example=4
    )

    is_new_device: int = Field(
        ge=0,
        le=1,
        description="Whether the device is new",
        example=1
    )

    is_new_location: int = Field(
        ge=0,
        le=1,
        description="Whether the location is new",
        example=1
    )

    night_transaction: int = Field(
        ge=0,
        le=1,
        description="Whether transaction happened at night",
        example=1
    )

    transaction_hour: int = Field(
        ge=0,
        le=23,
        description="Transaction hour (0-23)",
        example=2
    )

    amount_log: float = Field(
        ge=0,
        description="Log-transformed transaction amount",
        example=7.091
    )

    failure_rate: float = Field(
        ge=0,
        description="Customer transaction failure rate",
        example=0.667
    )

    customer_avg_amount: float = Field(
        ge=0,
        description="Average transaction amount for customer",
        example=300.0
    )

    amount_deviation: float = Field(
        ge=0,
        description="Transaction amount deviation from customer average",
        example=3.988
    )

    risk_signal_score: float = Field(
        ge=0,
        description="Calculated fraud risk signal score",
        example=5.333
    )

    @field_validator("payment_method")
    @classmethod
    def validate_payment_method(cls, value):
        allowed = ["Credit Card", "Debit Card", "UPI", "Net Banking", "Wallet"]

        if value not in allowed:
            raise ValueError("Invalid payment method")

        return value

    @field_validator("device_type")
    @classmethod
    def validate_device_type(cls, value):
        allowed = ["Mobile", "Desktop", "Tablet"]

        if value not in allowed:
            raise ValueError("Invalid device type")

        return value

    @field_validator("product_category")
    @classmethod
    def validate_product_category(cls, value):
        allowed = ["Electronics", "Clothing", "Grocery", "Home", "Beauty"]

        if value not in allowed:
            raise ValueError("Invalid product category")

        return value

@app.get("/")
def home():
    return {
        "message": "E-Commerce Fraud Detection API is running!"
    }
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": True
    }
@app.post("/predict")
def predict(transaction: Transaction):

    try:
        transaction_data = pd.DataFrame([transaction.model_dump()])

        prediction = model.predict(transaction_data)[0]
        probability = model.predict_proba(transaction_data)[0][1]

        if prediction == 1:
            result = "FRAUD"
        else:
            result = "NON-FRAUD"

        if probability >= 0.80:
            risk_level = "HIGH"
        elif probability >= 0.50:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        return {
            "prediction": result,
            "fraud_probability": round(float(probability), 4),
            "fraud_percentage": f"{probability * 100:.2f}%",
            "risk_level": risk_level
        }

    except Exception as e:
        return {
            "error": "Prediction failed",
            "details": str(e)
        }