class InventoryState:
    def __init__(self, next_pid=0, event_log_path="events.log", warnings={}):
        self.products = {}
        self.next_pid = next_pid
        self.event_log_path = event_log_path
        self.warnings = {}

    def get_product(self, product_id):
        return self.products.get(product_id)

    def allocate_product_id(self):
        pid = self.next_pid
        num = int(pid[1:]) + 1
        self.next_pid = f"P{num}"
        return pid

    def get_next_pid(self):
        return f"P{self.next_pid}"
