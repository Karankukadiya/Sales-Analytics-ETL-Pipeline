from extract import extract_data
from transform import transform_data
from load import load_data

import logging

# Configure logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:

    logging.info("Pipeline Started")

    customers, products, orders = extract_data()

    customers, products, orders = transform_data(
        customers,
        products,
        orders
    )

    load_data(
        customers,
        products,
        orders
    )

    logging.info(
        "Pipeline Completed Successfully"
    )

except Exception as e:

    logging.error(f"Pipeline Failed: {e}")

    raise