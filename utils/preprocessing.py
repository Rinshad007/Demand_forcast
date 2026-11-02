import pandas as pd


def preprocess_input(
    inventory,
    units_ordered,
    price,
    discount,
    competitor_price,
    month,
    category,
    weather,
    season,
    promotion,
    model_columns,
):
    """
    Preprocess user input before prediction.
    """

    # Create DataFrame
    input_df = pd.DataFrame({
        "Inventory Level": [inventory],
        "Units Ordered": [units_ordered],
        "Price": [price],
        "Discount": [discount],
        "Competitor Pricing": [competitor_price],
        "Month": [month],
        "Category": [category],
        "Weather Condition": [weather],
        "Seasonality": [season],
        "Promotion": [promotion]
    })

    # One-Hot Encoding
    input_df = pd.get_dummies(input_df)

    # Match model training columns
    input_df = input_df.reindex(
        columns=model_columns,
        fill_value=0
    )

    return input_df