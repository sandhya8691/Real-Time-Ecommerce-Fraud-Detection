import pandas as pd
import numpy as np

np.random.seed(42)

n = 50000

payment_methods = ["Credit Card", "Debit Card", "UPI", "Net Banking", "Wallet"]
product_categories = ["Electronics", "Clothing", "Grocery", "Beauty", "Home", "Sports"]
device_types = ["Mobile", "Desktop", "Tablet"]
locations = ["Bhubaneswar", "Bangalore", "Hyderabad", "Mumbai", "Delhi", "Chennai", "Pune", "Kolkata"]

df = pd.DataFrame({
    "transaction_id": [f"TXN{i:06d}" for i in range(1, n + 1)],
    "customer_id": [f"CUST{np.random.randint(1000, 10000)}" for _ in range(n)],
    "transaction_amount": np.round(np.random.lognormal(6.2, 1.0, n), 2),
    "transaction_time": pd.date_range(
        start="2026-01-01",
        periods=n,
        freq="10min"
    ),
    "payment_method": np.random.choice(payment_methods, n),
    "product_category": np.random.choice(product_categories, n),
    "customer_age": np.random.randint(18, 70, n),
    "account_age_days": np.random.randint(1, 2500, n),
    "device_type": np.random.choice(device_types, n),
    "customer_location": np.random.choice(locations, n),
    "previous_transaction_count": np.random.randint(0, 100, n),
    "failed_transaction_count": np.random.randint(0, 10, n),
    "is_new_device": np.random.choice([0, 1], n, p=[0.85, 0.15]),
    "is_new_location": np.random.choice([0, 1], n, p=[0.88, 0.12]),
    "night_transaction": np.random.choice([0, 1], n, p=[0.75, 0.25])
})

# Fraud probability
fraud_score = (
    (df["transaction_amount"] > 500) * 0.20
    + (df["transaction_amount"] > 1000) * 0.15
    + (df["failed_transaction_count"] >= 3) * 0.20
    + (df["is_new_device"] == 1) * 0.15
    + (df["is_new_location"] == 1) * 0.15
    + (df["night_transaction"] == 1) * 0.10
    + (df["account_age_days"] < 30) * 0.10
)

random_component = np.random.random(n) * 0.15

df["is_fraud"] = (
    fraud_score + random_component > 0.55
).astype(int)

# Save dataset
df.to_csv("data/transactions.csv", index=False)

print("Dataset created successfully!")
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nFraud distribution:")
print(df["is_fraud"].value_counts())