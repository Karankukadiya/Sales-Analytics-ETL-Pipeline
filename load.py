from sqlalchemy import create_engine
from config import *

def get_engine():

    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    return engine


def load_data(customers, products, orders):

    engine = get_engine()

    customers.to_sql(
        "customers",
        engine,
        if_exists="replace",
        index=False
    )

    products.to_sql(
        "products",
        engine,
        if_exists="replace",
        index=False
    )

    orders.to_sql(
        "orders",
        engine,
        if_exists="replace",
        index=False
    )