def validate_product_created(products, product_id, product_name, product_price):

    if product_id in products:

        raise ValueError("product already exists")

    # product_name related checks are already done by the product class
    if not product_name.strip():
        raise ValueError("product must have a name")

    if not isinstance(product_price, int):
        raise ValueError("product price must be and integer")

    if product_price < 0:

        raise ValueError("product price can't be negative")


def validate_product_restocked(products, product_id, quantity):

    if product_id not in products:

        raise ValueError("Can't restock a non existing product")

    if not isinstance(quantity, int):
        raise ValueError("product price must be and integer")

    if not 0 < quantity:

        raise ValueError("Quantity can't be negative OR zero")


def validate_product_sold(products, product_id, quantity):

    if product_id not in products:

        raise ValueError("Can't SELL a non existing product")

    if not isinstance(quantity, int):
        raise ValueError("product price must be and integer")

    if not 0 < quantity:

        raise ValueError("Quantity can't be negative OR zero")

    if not 0 < quantity <= products[product_id].quantity:

        raise ValueError("Not enough quantity to sell")


def validate_product_deactivated(products, product_id):

    if product_id not in products:

        raise ValueError("Can't deactivate a non existing product")
