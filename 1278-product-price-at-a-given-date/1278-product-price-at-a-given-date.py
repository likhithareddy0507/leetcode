import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    # Convert 'change_date' to datetime for accurate comparisons
    products['change_date'] = pd.to_datetime(products['change_date'])

    # Target date specified in the problem
    target_date = pd.to_datetime('2019-08-16')

    # Filter records up to the target date
    filtered_df = products[products['change_date'] <= target_date]

    # Find the most recent price change before or on the target date for each product
    latest_price_df = (
        filtered_df.sort_values(by=['product_id', 'change_date'], ascending=[True, False])
        .groupby('product_id')
        .first()
        .reset_index()
    )

    # Create a list of all unique products
    all_products = pd.DataFrame({'product_id': products['product_id'].unique()})

    # Merge with the latest prices and fill missing prices with default price (10)
    final_result = all_products.merge(latest_price_df[['product_id', 'new_price']], 
                                      on='product_id', 
                                      how='left').fillna({'new_price': 10})

    # Rename columns to match expected output
    final_result = final_result.rename(columns={'new_price': 'price'})

    # Return the final result sorted as required by LeetCode
    return final_result[['product_id', 'price']]