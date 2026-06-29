# `calendar.csv`

## Contains

-   **1 row = 1 calendar day**
-   **Rows:** 1,969
-   **Columns:** 14
-   Covers approximately **5.4 years** of daily data.
-   Each day is assigned a unique day identifier (`d_1`, `d_2`, ...,
    `d_1969`).

------------------------------------------------------------------------

## Purpose

This dataset acts as the **master calendar** for the project.

It links the day IDs used in the sales datasets to: - Actual calendar
dates - Walmart week numbers - Holidays and special events - SNAP (food
assistance program) availability by state

It is essential for creating **time-based features** used in
forecasting.

------------------------------------------------------------------------

## Key Columns

### `date`

-   Actual calendar date.
-   Example: `2011-01-29`
-   Used for time-series analysis.

### `d`

-   Internal day identifier.
-   Example:
    -   `d_1`
    -   `d_2`
    -   `d_1913`
-   Used to map sales columns from the sales datasets.

### `wm_yr_wk`

-   Walmart week identifier.
-   Used to join with **sell_prices.csv** since prices are recorded
    weekly.

### `weekday`

-   Name of the day (Monday--Sunday).

### `wday`

-   Numeric day of the week (1--7).

### `month`

-   Month number (1--12).

### `year`

-   Calendar year.

### `event_name_1`

-   Primary event occurring on that day (e.g., Christmas, Thanksgiving,
    Easter).
-   Missing when there is no event.

### `event_type_1`

-   Category of the primary event.

### `event_name_2`

-   Secondary event (if any).
-   Very rarely populated.

### `event_type_2`

-   Type of the secondary event.

### `snap_CA`

### `snap_TX`

### `snap_WI`

-   Binary indicators (`0` or `1`) showing whether SNAP benefits are
    available on that day in California, Texas, and Wisconsin.

------------------------------------------------------------------------

## Relationships

``` text
calendar.csv
      │
      ├── joins with sales_train_validation.csv
      │        using: d (d_1 ... d_1913)
      │
      ├── joins with sales_train_evaluation.csv
      │        using: d
      │
      └── joins with sell_prices.csv
               using: wm_yr_wk
```

------------------------------------------------------------------------

## Important Observations

-   One record per calendar day.
-   No missing values in date-related columns.
-   Holiday columns contain many missing values, indicating **no event**
    on those days.
-   Secondary events are extremely rare.
-   Only **282 unique Walmart weeks** across 1,969 days.
-   SNAP indicators are binary features that may influence product
    demand.

### Missing Values

  Column           Missing
  -------------- ---------
  event_name_1        1807
  event_type_1        1807
  event_name_2        1964
  event_type_2        1964

------------------------------------------------------------------------

## Role in the ML Pipeline

This dataset is primarily used for **feature engineering**:

-   Map `d_1`, `d_2`, ... to actual dates.
-   Extract temporal features:
    -   Day of week
    -   Month
    -   Year
    -   Weekend indicator
    -   Quarter
    -   Season
-   Encode holiday and event effects.
-   Add SNAP-related features.
-   Join weekly price information through `wm_yr_wk`.

------------------------------------------------------------------------

## Summary 

> **calendar.csv** contains one record for each calendar day in the
> forecasting period. It maps the sales day identifiers (`d_1`, `d_2`,
> ...) to actual dates and provides temporal information such as
> weekdays, months, years, holiday events, Walmart week identifiers, and
> SNAP indicators. It is primarily used for time-based feature
> engineering and for integrating the sales and pricing datasets.
