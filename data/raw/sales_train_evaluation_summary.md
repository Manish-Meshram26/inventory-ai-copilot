# `sales_train_evaluation.csv`

## Contains

-   **1 row = 1 product in a specific store**
-   **Rows:** 30,490
-   **Columns:** 1,947
-   The first **6 columns** contain product metadata.
-   The remaining **1,941 columns (`d_1` to `d_1941`)** contain daily
    unit sales.

------------------------------------------------------------------------

## Purpose

This is the **primary dataset** used for forecasting.

It stores the historical daily sales of every product-store combination.
The objective of the M5 Forecasting competition is to predict the future
sales for each row.

------------------------------------------------------------------------

## Key Columns

### `id`

-   Unique identifier for each product-store combination.
-   Used for submission and tracking predictions.

### `item_id`

-   Product identifier.

### `dept_id`

-   Department to which the product belongs.

### `cat_id`

-   High-level product category.
-   Examples:
    -   Foods
    -   Household
    -   Hobbies

### `store_id`

-   Store identifier.

### `state_id`

-   State where the store is located.
-   Examples:
    -   CA
    -   TX
    -   WI

### `d_1` → `d_1941`

-   Daily unit sales.
-   Each column represents one day.
-   The mapping from `d_x` to actual dates comes from **calendar.csv**.

------------------------------------------------------------------------

## Relationships

``` text
sales_train_evaluation.csv
        │
        ├── joins with calendar.csv
        │        using: d_1 ... d_1941
        │
        └── joins with sell_prices.csv
                 using:
                 item_id
                 store_id
                 wm_yr_wk (through calendar.csv)
```

------------------------------------------------------------------------

## Important Observations

-   Wide-format time series dataset.
-   Each row represents one unique **item-store** combination.
-   Sales are stored as integers representing units sold.
-   Many products have long sequences of zero sales.
-   Metadata columns are categorical and useful for grouping and
    aggregation.
-   The dataset spans **1,941 consecutive days** of sales history.

------------------------------------------------------------------------

## Role in the ML Pipeline

This dataset serves as the **target dataset** for forecasting.

Typical preprocessing steps include:

-   Convert from wide format to long format (melting).
-   Join with `calendar.csv` to obtain actual dates.
-   Join with `sell_prices.csv` to incorporate pricing information.
-   Create lag features (e.g., 7-day, 28-day).
-   Compute rolling statistics (mean, std, max, min).
-   Encode categorical variables.
-   Train forecasting models such as LightGBM, XGBoost, or other
    time-series models.

------------------------------------------------------------------------

## Summary 

> **sales_train_evaluation.csv** contains historical daily unit sales
> for every product-store combination. Each row represents a unique item
> sold in a specific store, while the daily sales are recorded across
> `d_1` to `d_1941`. It is the primary dataset used to train forecasting
> models and is enriched by joining with `calendar.csv` for temporal
> features and `sell_prices.csv` for pricing information.
