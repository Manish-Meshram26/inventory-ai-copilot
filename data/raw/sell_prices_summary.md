# `sell_prices.csv`

## Contains

-   **1 row = Price of one product in one store during one Walmart
    week**
-   **Rows:** 6,841,121
-   **Columns:** 4
-   Stores the weekly selling price for every product-store combination.

------------------------------------------------------------------------

## Purpose

This dataset provides the historical selling price of products across
Walmart stores. Since prices are recorded weekly rather than daily, it
must be combined with `calendar.csv` using `wm_yr_wk` to obtain the
applicable price for each day.

Price information is an important feature because demand often changes
with discounts, promotions, and price fluctuations.

------------------------------------------------------------------------

## Key Columns

### `store_id`

-   Store where the product is sold.

### `item_id`

-   Product identifier.

### `wm_yr_wk`

-   Walmart week identifier.
-   Used to join with `calendar.csv`.

### `sell_price`

-   Selling price of the product during that Walmart week.
-   Numeric (floating-point) value.

------------------------------------------------------------------------

## Relationships

``` text
calendar.csv
      │
      │ wm_yr_wk
      ▼
sell_prices.csv
      │
      │ item_id + store_id
      ▼
sales_train_validation.csv
sales_train_evaluation.csv
```

------------------------------------------------------------------------

## Important Observations

-   One row represents the selling price of one item in one store for
    one Walmart week.
-   Prices are **weekly**, not daily.
-   Multiple stores can sell the same product at different prices.
-   Prices can change over time because of promotions, discounts, or
    pricing strategies.
-   Some products maintain constant prices, while others experience
    frequent price changes.
-   The dataset contains **no missing values**.

------------------------------------------------------------------------

## Role in the ML Pipeline

This dataset is primarily used for **price-based feature engineering**.

Typical features include:

-   Current selling price
-   Price difference from previous week
-   Percentage price change
-   Rolling average price
-   Maximum and minimum historical price
-   Discount percentage
-   Price volatility

These features help the model learn how pricing affects customer demand.

------------------------------------------------------------------------

## Summary (Interview Style)

> **sell_prices.csv** contains the weekly selling price of every
> product-store combination in the M5 Forecasting dataset. Each row
> represents the price of one item sold in a specific Walmart store
> during a particular Walmart week. It is joined with `calendar.csv`
> through `wm_yr_wk` and with the sales datasets through `item_id` and
> `store_id` to create price-related features that improve demand
> forecasting accuracy.
