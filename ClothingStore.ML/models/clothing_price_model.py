import numpy as np

from models.algorithms import create_algorithm
from models.feature_builder import FeatureBuilder


class ClothingPriceModel:

    def __init__(self, algorithm="random_forest", **algorithm_parameters):
        # Store the selected algorithm name
        self.algorithm = algorithm

        # Create the feature builder
        self.feature_builder = FeatureBuilder()

        # Create the machine learning algorithm
        self.model = create_algorithm(
            algorithm,
            **algorithm_parameters
        )

    # Train the model
    def fit(self, df, expected_prices):

        # Build the input features for training
        features = self.feature_builder.build(
            df,
            fit=True
        )

        # Train the machine learning model
        self.model.fit(
            features,
            expected_prices
        )

        # Return the current instance
        return self


    def predict(self, df):
        # Build the input features for the machine learning mode
        input_features = self.feature_builder.build(
            df,
            # Do not learn again; use the mapping learned during training
            fit=False
        )

        predictions = self.model.predict(input_features)

        # Round up and convert to integers
        return np.ceil(predictions).astype(int)

    # Return the most important features used by the model
    def feature_importances(self, top_n=15):
         # Check if the model provides feature importances
        if not hasattr(self.model, "feature_importances_"):
            raise AttributeError(
                f"{self.algorithm} does not provide feature importances."
            )

        feature_names = self.feature_builder.feature_names()

         # Get the importance value of each feature
        importances = self.model.feature_importances_

        order = importances.argsort()[::-1][:top_n]

        # Return the feature names with their importance values
        return [
            (feature_names[i], importances[i])
            for i in order
        ]

    # Return the coefficients of each feature
    def coefficients(self):
        # Check if the model provides coefficients
        if not hasattr(self.model, "coef_"):
            raise AttributeError(
                f"{self.algorithm} does not provide coefficients."
            )
        
        # Get the feature names
        feature_names = self.feature_builder.feature_names()

        # Return the feature names with their coefficients
        return list(
            zip(
                feature_names,
                self.model.coef_
            )
        )