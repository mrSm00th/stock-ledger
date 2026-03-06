# Stock Ledger (Event Log Based Inventory CLI)

## Overview

This project is a small command‑line inventory application written in Python.

The application stores inventory operations as events in a log file. When the program starts, it reads the log file and rebuilds the inventory state by replaying the events in order.

The project was built as a learning exercise to practice designing a simple CLI application and organizing Python code into small modules.

This project is not intended for real production use.

---

## Features

The CLI supports the following operations:

* Create a product
* Restock a product
* Sell a product
* Deactivate a product
* List all products
* View a single product
* Show warnings from event replay

Each operation writes a new event to the event log.

When the program starts, the event log is replayed to rebuild the inventory state.

---

## Example Event

Each event is stored as a JSON object in `events.log`.

```json
{
  "timestamp": "2026-01-01T09:01:10Z",
  "event_type": "ProductRestocked",
  "product_id": "P100",
  "data": {
    "quantity": 10
  }
}
```

Events are appended to the log file and processed sequentially during startup.

---

## Project Structure

```
.
├── main.py               # Application entry point and main command loop
├── command_input.py      # Reads and parses CLI commands
├── dispatch_command.py   # Routes parsed commands to the correct handler
├── command_handlers.py   # Implements inventory operations
├── validator.py          # Validation logic for commands and events
├── product.py            # Product domain model
├── inventory.py          # In‑memory inventory state container
├── event_writer.py       # Appends events to the log file (JSON Lines)
├── event_replay.py       # Replays events from the log to rebuild state
├── event_handlers.py     # Applies events to the in‑memory state
├── views.py              # Console output helpers
├── utils.py              # Time utilities and CLI helper functions
├── events.log            # Example event log (contains valid and invalid events)
├── README.md
```
---
### Main Components

- **`main.py`**  
  Program entry point. Replays the event log to rebuild state and starts the command loop.

- **`command_input.py`**  
  Reads user input and converts it into a structured command format.

- **`dispatch_command.py`**  
  Routes parsed commands to the correct handler.

- **`command_handlers.py`**  
  Handles inventory operations and writes events to the log file.

- **`event_writer.py`**  
  Appends events to the log file.

- **`event_replay.py`**  
  Reads the event log and rebuilds the inventory state by applying events.

- **`event_handlers.py`**  
  Contains functions that apply events to the in-memory state.

- **`validator.py`**  
  Contains validation functions used during both command execution and event replay.

- **`product.py`**  
  Defines the `Product` class and enforces basic constraints on product data.

- **`views.py`**  
  Handles console output such as tables and product details.

- **`utils.py`**  
  Contains helper functions such as timestamps and CLI help messages.

---

## Requirements

* Python 3.9 or newer
* tabulate

Install the dependency:

```bash
pip install tabulate
```

---

## Running the Application

From the project directory:

```bash
python main.py
```

When the application starts it will:

1. Load `events.log`
2. Replay valid events
3. Skip invalid or corrupted events
4. Start the CLI

---

## CLI Commands

- **`create <name> <price>`**  
  Create a new product.

- **`restock <product_id> <quantity>`**  
  Add stock to an existing product.

- **`sell <product_id> <quantity>`**  
  Sell a quantity from an existing product.

- **`deactivate <product_id>`**  
  Remove a product from inventory.

- **`list_products`**  
  List all products.

- **`show_product <product_id>`**  
  Show details for a single product.

- **`show_warnings`**  
  Display warnings generated during event replay.

- **`help`**  
  Show help message.

- **`exit / quit`**  
  Exit the application.
---
## Handling Invalid Events

During event replay the system attempts to apply each event in the log file.

Events may be skipped if they contain problems such as:

* corrupted JSON
* missing required fields
* invalid quantities
* operations on products that do not exist

Skipped events are recorded as warnings with their corresponding line numbers.

---


## What I Learned

While building this project I :

* learned more about the CRUD and event sourcing
* learned how different layers apply validation rules to the same input but according to the layers intend and without making rules redundent
* separating command parsing and command execution
* validating input at different layers
* replaying an event log to rebuild application state
* learned how to organizing a Python project into modules for better debugging and scalibility

---

## Possible Improvements

Potential future improvements include:

* adding a database
* improving CLI usability
* adding additional product operations (such as updating price)

---

## License
MIT License
