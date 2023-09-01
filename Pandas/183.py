import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers = pd.merge(customers, orders, how="outer", left_on="id", right_on="customerId")
    customers.rename(columns={"name":"Customers"}, inplace=True)
    return customers[customers["customerId"].isnull()][["Customers"]]

# More complex solution
# import pandas as pd

# def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
#     # Define a condition using apply and lambda
#     if orders.empty:
#         if customers.empty:
#             return pd.DataFrame(columns=["Customers"])
#         customers.rename(columns={"name": "Customers"}, inplace=True)
#         return customers[["Customers"]]

#     condition = customers.apply(lambda row: row["id"] not in orders["customerId"].values, axis=1)
    
#     # Filter the customers DataFrame based on the condition
#     customers_filtered = customers[condition]
    
#     # Rename the "name" column to "Customers"
#     customers_filtered.rename(columns={"name": "Customers"}, inplace=True)
    
#     return customers_filtered[["Customers"]]