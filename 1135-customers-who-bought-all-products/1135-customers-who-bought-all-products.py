import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # Count the total number of unique products
    total_products = len(product['product_key'].unique())
    
    # Count unique products bought by each customer
    customer_product_count = customer.groupby('customer_id')['product_key'].nunique()
    
    # Filter customers who bought all products
    customers_bought_all = customer_product_count[customer_product_count == total_products].reset_index()
    
    # Return only the required column with the correct name
    return customers_bought_all[['customer_id']]