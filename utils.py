from datetime import datetime, timezone
import sys


# returns current time in UTC ISO format used for time_stamp in event logging
def current_utc_timestamp():
    return datetime.now(timezone.utc).isoformat()


def exit_app():
    sys.exit("--Exiting the program--")


def show_help():

    print("\nInventory Management CLI")
    print("=" * 26)

    print("\nCommands:\n")

    print("  create <name> <price>")
    print("      Create a new product.")

    print("\n  restock <product_id> <quantity>")
    print("      Add stock to an existing product.")

    print("\n  sell <product_id> <quantity>")
    print("      Sell quantity from an existing product.")

    print("\n  deactivate <product_id>")
    print("      Remove a product from inventory.")

    print("\n  show_product <product_id>")
    print("      Show details of a single product.")

    print("\n  list_products")
    print("      List all products in inventory.")

    print("\n  show_warnings")
    print("      Show warnings generated during event replay.")

    print("\nSystem Commands:\n")

    print("  help")
    print("      Show this help message.")

    print("\n  exit / quit")
    print("      Exit the application.\n")
