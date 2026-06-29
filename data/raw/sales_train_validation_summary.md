# `sales_train_validation.csv`

## Contains

-   **1 row = 1 product in a specific store**
-   **Rows:** 30,490
-   **Columns:** 1,919
-   The first **6 columns** contain product metadata.
-   The remaining **1,913 columns (`d_1` to `d_1913`)** contain daily
    unit sales used for model training and validation.

------------------------------------------------------------------------

## Purpose

This dataset contains the historical sales data provided for the
**validation phase** of the M5 Forecasting competition. Models are
trained on these observations and evaluated by forecasting the next 28
days.

------------------------------------------------------------------------

## Key Columns

### `id`

-   Unique identifier for each product-store combination.
-   Ends with `_validation`, distinguishing it from the evaluation
    dataset.

### `item_id`

-   Unique product identifier.

### `dept_id`

-   Department to which the product belongs.

### `cat_id`

-   High-level product category.

### `store_id`

-   Store where the item is sold.

### `state_id`

-   State of the store (`CA`, `TX`, or `WI`).

### `d_1` → `d_1913`

-   Daily unit sales.
-   Each column represents one calendar day.
-   Actual dates are obtained from **calendar.csv**.

------------------------------------------------------------------------

## Relationships

``` text
sales_train_validation.csv
        │
        ├── joins with calendar.csv
        │        using: d_1 ... d_1913
        │
        └── joins with sell_prices.csv
                 using:
                 item_id
                 store_id
                 wm_yr_wk (through calendar.csv)
```

------------------------------------------------------------------------

## Important Observations

-   Wide-format time-series dataset.
-   Each row corresponds to one unique item-store combination.
-   Sales values are integer counts of units sold.
-   Many products contain long periods of zero sales.
-   Metadata columns enable aggregation by item, department, category,
    store, and state.
-   Covers **1,913 consecutive days** of historical sales.

------------------------------------------------------------------------

## Difference from `sales_train_evaluation.csv`

  Validation                               Evaluation
  ---------------------------------------- --------------------------------
  Sales available until `d_1913`           Sales available until `d_1941`
  Used for public leaderboard validation   Used for final evaluation
  `id` ends with `_validation`             `id` ends with `_evaluation`

------------------------------------------------------------------------

## Role in the ML Pipeline

This dataset is used to:

-   Train forecasting models.
-   Convert from wide to long format.
-   Merge with `calendar.csv` for temporal features.
-   Merge with `sell_prices.csv` for price information.
-   Generate lag, rolling, and date-based features.
-   Validate forecasting performance before testing on the evaluation
    dataset.

------------------------------------------------------------------------

## Summary (Interview Style)

> **sales_train_validation.csv** contains historical daily unit sales
> for every product-store combination used during the validation stage
> of the M5 Forecasting competition. Each row represents a unique item
> sold in a specific store, while the daily sales are stored across
> `d_1` to `d_1913`. The dataset is combined with `calendar.csv` and
> `sell_prices.csv` to engineer temporal and pricing features for
> training demand forecasting models.
