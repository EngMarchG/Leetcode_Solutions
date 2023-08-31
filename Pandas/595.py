import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    results = world[(world["area"] >= 3000000) | (world["population"] >= 25000000)]

    return results[["name", "population", "area"]]