def read_user_command():

    user_input = input("Command:").strip().lower()
    return user_input


def parse_command(user_input):

    COMMANDS_SCHEMA = {
        "create": {"args": 2, "types": [str, int]},  # name, price
        "sell": {"args": 2, "types": [str, int]},  # pid, quantity
        "restock": {"args": 2, "types": [str, int]},  # pid, quantity
        "deactivate": {"args": 1, "types": [str]},  # pid
        "list_products": {"args": 0, "types": {}},
        "show_product": {"args": 1, "types": [str]},  # pid
        "help": {"args": 0, "types": []},
        "show_warnings": {"args": 0, "types": []},
        "exit": {"args": 0, "types": []},
        "quit": {"args": 0, "types": []},
    }

    tokens = user_input.strip().split()

    if not tokens:
        raise ValueError("Empty command")

    cmd, *arg_tokens = tokens

    schema = COMMANDS_SCHEMA.get(cmd)

    if not schema:
        raise ValueError("Unknown command")

    if len(arg_tokens) != schema["args"]:
        raise ValueError(f"{cmd} expects {schema['args']} arguments")

    args = []

    for i, (value, expected_type) in enumerate(zip(arg_tokens, schema["types"])):
        try:
            typed_value = expected_type(value)
        except ValueError:
            raise ValueError(f"Argument {i+1} must be {expected_type.__name__}")

        args.append(typed_value)

    return {"cmd": cmd, "args": args}
