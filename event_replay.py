import json
from event_handlers import (
    handle_product_created,
    handle_product_deactivated,
    handle_product_restocked,
    handle_product_sold,
)
from inventory import InventoryState


def replay_events(file_name):

    state = InventoryState(event_log_path=file_name)

    events_applied = 0
    state.warnings = {}

    invalid_lines = []

    EVENT_SCHEMA = {
        "ProductCreated": ("name", "price"),
        "ProductRestocked": ("quantity",),
        "ProductSold": ("quantity",),
        "ProductDeactivated": (),
    }

    EVENT_HANDLERS = {
        "ProductCreated": handle_product_created,
        "ProductRestocked": handle_product_restocked,
        "ProductSold": handle_product_sold,
        "ProductDeactivated": handle_product_deactivated,
    }

    try:

        with open(file_name) as file:

            for row_no, row_data in enumerate(file, start=1):

                # skipping blank line
                if not row_data.strip():
                    continue

                # checking for KeyError and json error
                try:

                    event = json.loads(row_data)

                    # if a row dosen't have this than its invalid and we'll skip it
                    event_type = event["event_type"]

                    data = event.get("data", {})

                    # schema validation
                    required = EVENT_SCHEMA.get(event_type)
                    if required is None:
                        state.warnings[row_no] = "Invalid event type"
                        continue

                    for field in required:

                        _ = data[field]  # raises KeyError if missing

                    # checking for the max pid
                    if event_type == "ProductCreated":
                        pid_num = int(event["product_id"][1:])
                        state.next_pid = max(state.next_pid, pid_num + 1)

                    handler = EVENT_HANDLERS.get(event_type)

                    try:

                        handler(state.products, event)
                        events_applied += 1

                    except ValueError as e:
                        state.warnings[row_no] = str(e)

                except json.JSONDecodeError:

                    invalid_lines.append(row_no)
                    continue

                except KeyError as e:

                    invalid_lines.append(row_no)
                    continue

        print(f"INFO: Replayed {events_applied} events")
        for line in invalid_lines:
            print(f"WARN: Skipped corrupted event at line {line}")

        print("INFO: System ready")

    except FileNotFoundError:
        return {"error": True, "message": "File Not Found"}

    return {
        "error": False,
        "message": None,
        "state": state,
    }
