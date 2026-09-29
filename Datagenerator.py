import pandas as pd
import numpy as np

# Make results reproducible
np.random.seed(42)

# Number of synthetic users
n_users = 20000

# Create user IDs
user_id = np.arange(1, n_users + 1)

# User behavior
monthly_purchases = np.random.poisson(5, n_users) + 1

avg_purchase_amount = np.round(
    np.random.lognormal(mean=5.2, sigma=0.5, size=n_users),
    2
)

late_payment_count = np.random.poisson(1, n_users)

on_time_payment_rate = np.round(
    np.clip(
        np.random.normal(0.85, 0.15, n_users),
        0.2,
        1.0
    ),
    2
)

cancellation_rate = np.round(
    np.clip(
        np.random.beta(2, 15, n_users),
        0,
        1
    ),
    2
)

offer_click_rate = np.round(
    np.clip(
        np.random.beta(3, 5, n_users),
        0,
        1
    ),
    2
)

avg_installments = np.random.choice(
    [2, 3, 4],
    size=n_users,
    p=[0.2, 0.3, 0.5]
)

monthly_spending = np.round(
    monthly_purchases * avg_purchase_amount,
    2
)

# Historical behavior / outcomes
feature_used = np.random.binomial(1, 0.45, n_users)

purchase_completed = np.random.binomial(
    1,
    np.clip(
        0.55
        + (on_time_payment_rate * 0.25)
        + (offer_click_rate * 0.15)
        - (cancellation_rate * 0.20),
        0.05,
        0.95
    )
)

late_payment_probability = np.clip(
    0.05
    + (late_payment_count * 0.04)
    + ((1 - on_time_payment_rate) * 0.30),
    0.01,
    0.90
)

late_payment = np.random.binomial(
    1,
    late_payment_probability
)

retained_30_days = np.random.binomial(
    1,
    np.clip(
        0.45
        + (monthly_purchases / 20)
        + (offer_click_rate * 0.20)
        - (cancellation_rate * 0.15),
        0.05,
        0.95
    )
)

# Create dataframe
df = pd.DataFrame({
    "user_id": user_id,
    "monthly_purchases": monthly_purchases,
    "avg_purchase_amount": avg_purchase_amount,
    "late_payment_count": late_payment_count,
    "on_time_payment_rate": on_time_payment_rate,
    "cancellation_rate": cancellation_rate,
    "offer_click_rate": offer_click_rate,
    "avg_installments": avg_installments,
    "monthly_spending": monthly_spending,
    "feature_used": feature_used,
    "purchase_completed": purchase_completed,
    "late_payment": late_payment,
    "retained_30_days": retained_30_days
})

# Save the dataset
df.to_csv("users.csv", index=False)

print("Dataset created successfully!")
print(f"Number of users: {len(df)}")
print("\nFirst 5 users:")
print(df.head())