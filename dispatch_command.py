from command_handlers import (
    handle_create_command,
    handle_deactivate_command,
    handle_restock_command,
    handle_sell_command,
)
from views import show_product, show_products_table, show_warnings
from utils import show_help, exit_app


def dispatch_command(state, parsed_cmd):

    COMMANDS = {
        "create": {"handler": handle_create_command, "needs_state": True},
        "restock": {"handler": handle_restock_command, "needs_state": True},
        "sell": {"handler": handle_sell_command, "needs_state": True},
        "deactivate": {"handler": handle_deactivate_command, "needs_state": True},
        "list_products": {"handler": show_products_table, "needs_state": True},
        "show_warnings": {"handler": show_warnings, "needs_state": True},
        "show_product": {"handler": show_product, "needs_state": True},
        "help": {"handler": show_help, "needs_state": False},
        "exit": {"handler": exit_app, "needs_state": False},
        "quit": {"handler": exit_app, "needs_state": False},
    }

    cmd_name = parsed_cmd["cmd"]
    args = parsed_cmd["args"]

    cmd = COMMANDS.get(cmd_name)

    if not cmd:
        raise ValueError(f"Unknown command: {cmd_name}")

    handler = cmd["handler"]

    if cmd.get("needs_state", True):
        handler(state, args)
    else:
        handler()
