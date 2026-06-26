import pandas as pd

def transform_data(customers, products, orders):

    customers = customers.drop_duplicates()
    products = products.drop_duplicates()
    orders = orders.drop_duplicates()

    orders["order_date"] = pd.to_datetime(
        orders["order_date"]
    )

    orders["sales"] = orders["sales"].fillna(0)

    orders["profit"] = orders["profit"].fillna(0)

    return customers, products, orders

# if __name__ == "__main__":

#     from extract import extract_data

#     customers, products, orders = extract_data()

#     customers, products, orders = transform_data(
#         customers,
#         products,
#         orders
#     )

#     print("Transform Success")