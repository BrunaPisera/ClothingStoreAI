import numpy as np
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer, OneHotEncoder

from models.constants import (
    CATEGORICAL_COLS,
    NUMERIC_COLS,
)

def parse_accessories(series: pd.Series):
    return series.apply(
        lambda s: [] if s == "none" else s.split("|")
    ).tolist()

class FeatureBuilder:

    def __init__(self):
        # Convert categorical values into numerical features
        self.OneHotEncoder = OneHotEncoder(
            handle_unknown="ignore"
        )

        self.mlb = MultiLabelBinarizer()

   # Transform the input DataFrame into numerical features for the machine learning model
    def build(self, df: pd.DataFrame, fit: bool):
        # Extract the categorical columns
        categorical_features = df[CATEGORICAL_COLS].copy()

        # Learn and encode the training data
        if fit:
            encoded_categorical_features = (
                self.OneHotEncoder
                .fit_transform(categorical_features)
                .toarray()
            )
        # Encode using the learned mapping
        else:
            encoded_categorical_features = (
                self.OneHotEncoder
                .transform(categorical_features)
                .toarray()
            )

        # Extract the numerical feature values
        numerical_features = df[
            NUMERIC_COLS
        ].to_numpy()

        # Combine all features into a single array
        return np.hstack([
            encoded_categorical_features,
            numerical_features
        ])

    # Return the names of all features in the same order they are sent to the model
    def feature_names(self):

        return (
            list(
                self.OneHotEncoder.get_feature_names_out(
                    CATEGORICAL_COLS
                )
            )
            + NUMERIC_COLS
        )