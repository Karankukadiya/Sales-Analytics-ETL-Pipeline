import pandas as pd

def extract_data():

    customers = pd.read_csv("data/customers.csv")
    products = pd.read_csv("data/products.csv")
    orders = pd.read_csv("data/orders.csv")

    return customers, products, orders

# if __name__ == "__main__":
#     customers, products, orders = extract_data()

#     print(customers.head())
#     print(products.head())
#     print(orders.head())