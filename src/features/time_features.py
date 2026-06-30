"""
Time-based feature engineering functions.

This module creates calendar-related features used for demand forecasting.
"""

import pandas as pd;

def add_weekend_feature(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a binary feature indicating whether a date falls on a weekend.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe containing a 'weekday' column.

    Returns
    -------
    pd.DataFrame
        DataFrame with an additional 'is_weekend' column.
    """

    df = df.copy()

    df["is_weekend"] = (
        df["weekday"]
        .isin(["Saturday", "Sunday"])
        .astype("uint8")
    )

    return df

def add_month_boundary_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add month boundary features.
    """

    df = df.copy()

    df["is_month_start"] = df["date"].dt.is_month_start.astype("uint8")
    df["is_month_end"] = df["date"].dt.is_month_end.astype("uint8")

    return df

def create_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply all calendar-based feature engineering steps.
    """

    df = add_weekend_feature(df)
    df = add_month_boundary_features(df)

    return df