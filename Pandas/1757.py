import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    results = products[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")]
    return results[["product_id"]]