from validator import (
    validate_product_created,
    validate_product_deactivated,
    validate_product_restocked,
    validate_product_sold,
)
from product import Product


def handle_product_created(state, event):

    validate_product_created(
        state,
        product_id=event["product_id"],
        product_name=event["data"]["name"],
        product_price=event["data"]["price"],
    )

    new_product = Product(
        id=event["product_id"],
        name=event["data"]["name"],
        price=event["data"]["price"],
        quantity=0,
    )

    state[event["product_id"]] = new_product


def handle_product_restocked(state, event):

    validate_product_restocked(
        state, product_id=event["product_id"], quantity=event["data"]["quantity"]
    )

    state[event["product_id"]].restock_product(event["data"]["quantity"])


def handle_product_sold(state, event):

    validate_product_sold(
        state, product_id=event["product_id"], quantity=event["data"]["quantity"]
    )

    state[event["product_id"]].sell_product(event["data"]["quantity"])


def handle_product_deactivated(state, event):

    validate_product_deactivated(state, product_id=event["product_id"])

    del state[event["product_id"]]
