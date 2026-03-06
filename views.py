from tabulate import tabulate


def show_product(inventory, args):
    try:
        product_id = args[0].upper()
        product = inventory.products.get(product_id)
        product = inventory.products.get(product_id)
        if not product:
            raise ValueError("Product not found")

        print("\nProduct Details")
        print("----------------")
        print(f"ID       : {product.id}")
        print(f"Name     : {product.name}")
        print(f"Price    : {product.price}")
        print(f"Quantity : {product.quantity}")

    except KeyError:
        raise ValueError("Wrong Product Id")


# prints the warning events
def show_warnings(state, args):

    warning_events = state.warnings

    for warning_id, warning in warning_events.items():
        print(f"Line {warning_id}: {warning}")


def show_products_table(state, args):

    if not state.products:
        print("No products available.")
        return

    table = []
    headers = ["ID", "Name", "Price", "Quantity", "Active"]

    for p in state.products.values():
        table.append([p.id, p.name, p.price, p.quantity])

    print(tabulate(table, headers=headers, tablefmt="grid"))
