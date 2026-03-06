from event_writer import (
    write_product_created,
    write_product_deactivated,
    write_product_restocked,
    write_product_sold,
)
from validator import (
    validate_product_created,
    validate_product_deactivated,
    validate_product_restocked,
    validate_product_sold,
)
from product import Product


def handle_create_command(state, arguments):

    (
        name,
        price,
    ) = arguments

    product_id = state.get_next_pid()

    file_name = state.event_log_path

    validate_product_created(
        state.products, product_id=product_id, product_name=name, product_price=price
    )

    write_product_created(file_name, product_id, name, price)

    print(f"Product {product_id}: {name} Successfully Created!!")
    new_product = Product(id=product_id, name=name, price=price, quantity=0)

    state.products[product_id] = new_product

    state.next_pid += 1


def handle_restock_command(state, arguments):
    product_id, quantity = arguments
    product_id = product_id.upper()

    file_name = state.event_log_path

    validate_product_restocked(state.products, product_id=product_id, quantity=quantity)

    write_product_restocked(file_name, product_id, quantity)

    print("Product Successfully Restocked!!")

    state.products[product_id].restock_product(quantity)


def handle_sell_command(state, arguments):
    product_id, quantity = arguments
    product_id = product_id.upper()

    file_name = state.event_log_path

    validate_product_sold(state.products, product_id=product_id, quantity=quantity)

    write_product_sold(file_name, product_id, quantity)

    print("Product Successfully Sold!!")

    state.products[product_id].sell_product(quantity)


def handle_deactivate_command(state, arguments):
    (product_id,) = arguments
    product_id = product_id.upper()

    file_name = state.event_log_path

    validate_product_deactivated(state.products, product_id=product_id)

    write_product_deactivated(file_name, product_id)

    print("Product Successfully Deactivated!!")

    del state.products[product_id]
