"""
Train a machine learning model to predict clothing prices.

Usage:
    python train_price_model.py

Outputs:
    price_model.joblib
"""

import joblib
import pandas as pd
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import train_test_split

from models.clothing_price_model import ClothingPriceModel

DATA_PATH = "clothing_pricing_dataset.csv"
TARGET_COL = "price"
MODEL_PATH = "price_model.joblib"

def main():
    # algorithm_name = "random_forest" 
    algorithm_name = "decision_tree" 
    # algorithm_name = "cat_boost" 
    # algorithm_name = "linear_regression" 

    # Load the dataset
    df = pd.read_csv(DATA_PATH)

    print("=" * 45)
    print("Training Clothing Price Prediction Model")
    print("=" * 45)
    print(f"Algorithm : {algorithm_name.replace('_', ' ').title()}")
    print(f"Dataset   : {len(df)} samples")
    print()

    # Split the dataset into training and testing sets
    train_df, test_df = train_test_split(
        df,
        test_size=0.2,
        random_state=42,
    )
    
    # Create the prediction model
    model = ClothingPriceModel(
        algorithm=algorithm_name
    )

    # Train the model
    model.fit(
        train_df,
        train_df[TARGET_COL],
    )

    # Make predictions on the test training set
    predictions = model.predict(test_df)

    # Get the expected prices
    expected_prices = test_df[TARGET_COL]

    mae = mean_absolute_error(
        expected_prices,
        predictions,
    )

    rmse = mean_squared_error(
        expected_prices,
        predictions,
    ) ** 0.5

    r2 = r2_score(
        expected_prices,
        predictions,
    )

    print("Training Results")
    print("----------------")
    print(f"MAE  : {mae:.2f}")
    print(f"RMSE : {rmse:.2f}")
    print(f"R2   : {r2:.4f}")
    print()

    # Save the trained model
    joblib.dump(model, MODEL_PATH)

    print("Model saved successfully!")
    print()

if __name__ == "__main__":
    main()