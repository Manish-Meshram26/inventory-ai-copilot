import pandas as pd


def add_lag_features(df: pd.DataFrame, lags=(1, 7, 28)) -> pd.DataFrame:
    """Add lagged sales columns for each item_id/store_id pair.

    Parameters:
        df: DataFrame containing at least 'item_id', 'store_id', and 'sales'.
        lags: Iterable of integer lag periods to add as columns.

    Returns:
        DataFrame with new lag columns like 'lag_1', 'lag_7', 'lag_28'.
    """

    result = df.copy()
    for lag in lags:
        result[f'lag_{lag}'] = result.groupby(['item_id', 'store_id'])['sales'].shift(lag)
    return result


def rolling_mean(df: pd.DataFrame, windows=(7, 28)) -> pd.DataFrame:
    """Add rolling mean sales columns for each item_id/store_id pair.

    Parameters:
        df: DataFrame containing at least 'item_id', 'store_id', and 'sales'.
        windows: Iterable of integer window sizes to add as columns.

    Returns:
        DataFrame with new rolling mean columns like 'rolling_mean_7', 'rolling_mean_28'.
    """

    result = df.copy()
    for window in windows:
        result[f'rolling_mean_{window}'] = (
            result.groupby(['item_id', 'store_id'])['sales']
            .transform(lambda x: x.shift(1).rolling(window, min_periods=1).mean())
        )
    return result


