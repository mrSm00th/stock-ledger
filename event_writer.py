import json
from utils import current_utc_timestamp


def write_product_created(file_name, product_id, product_name, product_price):

    time_stamp = current_utc_timestamp()

    try:

        with open(file_name, "a") as file:

            event = {
                "timestamp": time_stamp,
                "event_type": "ProductCreated",
                "product_id": product_id,
                "data": {"name": product_name, "price": product_price},
            }

            row = json.dumps(event)
            file.write(row + "\n")

    except FileNotFoundError:
        raise ValueError("file not found")


def write_product_restocked(file_name, product_id, quantity):

    time_stamp = current_utc_timestamp()

    try:

        with open(file_name, "a") as file:

            event = {
                "timestamp": time_stamp,
                "event_type": "ProductRestocked",
                "product_id": product_id,
                "data": {"quantity": quantity},
            }

            row = json.dumps(event)
            file.write(row + "\n")

    except FileNotFoundError:
        raise ValueError("file not found")


def write_product_sold(file_name, product_id, quantity):

    time_stamp = current_utc_timestamp()

    try:

        with open(file_name, "a") as file:

            event = {
                "timestamp": time_stamp,
                "event_type": "ProductSold",
                "product_id": product_id,
                "data": {"quantity": quantity},
            }

            row = json.dumps(event)
            file.write(row + "\n")

    except FileNotFoundError:
        raise ValueError("file not found")


def write_product_deactivated(file_name, product_id):

    time_stamp = current_utc_timestamp()

    try:

        with open(file_name, "a") as file:

            event = {
                "timestamp": time_stamp,
                "event_type": "ProductDeactivated",
                "product_id": product_id,
                "data": {},
            }

            row = json.dumps(event)
            file.write(row + "\n")

    except FileNotFoundError:
        raise ValueError("file not found")
