import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


class HealthAnalyzer:
    """
    Simple helper class for analysing the health study data.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Store the dataframe to use in the analysis.
        """
        self.df = df
        self.bp_age_model: LinearRegression | None = None
        self.bp_age_weight_model: LinearRegression | None = None

    def basic_stats(self) -> pd.DataFrame:
        """
        Compute mean, median, minimum and maximum for key numeric variables.
        """
        cols = ["age", "height", "weight", "systolic_bp", "cholesterol"]
        return self.df[cols].agg(["mean", "median", "min", "max"]).T

    def fit_bp_age_regression(self) -> LinearRegression:
        """
        Fit a simple linear regression model for systolic blood pressure using age as predictor.
        """
        X = self.df[["age"]].values
        y = self.df["systolic_bp"].values
        model = LinearRegression()
        model.fit(X, y)
        self.bp_age_model = model
        return model

    def fit_bp_age_weight_regression(self) -> LinearRegression:
        """
        Fit a multiple linear regression model for systolic blood pressure
        using both age and weight as predictors.
        """
        X = self.df[["age", "weight"]].values
        y = self.df["systolic_bp"].values
        model = LinearRegression()
        model.fit(X, y)
        self.bp_age_weight_model = model
        return model
