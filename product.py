import re


class Product:

    def __init__(self, id, name, price, quantity):

        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):

        return f" Id: {self.id} name: {self.name} price: {self.price} quantity: {self.quantity}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, n):

        if not isinstance(n, str):
            raise ValueError("Product ID must be of type Str")

        if n.startswith("P") and len(n) >= 2 and n.count("P") == 1 and n[1:].isdigit():
            self._id = n

        else:
            raise ValueError("Invalid product id data")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):

        if not isinstance(n, str):
            raise ValueError("Invalid name data")

        if not re.fullmatch(r"[a-zA-Z0-9_-]+", n):
            raise ValueError("Invalid product name ")

        if not n.strip():
            raise ValueError("Name cant be empty")

        self._name = n

    @property
    def price(self):

        return self._price

    @price.setter
    def price(self, n):

        if not isinstance(n, int):
            raise ValueError("Price data must be int")
        if n < 0:
            raise ValueError("Price can't be negative ")

        self._price = n

    @property
    def quantity(self):

        return self._quantity

    @quantity.setter
    def quantity(self, n):

        if not isinstance(n, int):
            raise ValueError("Quantity can't a string ")

        if n < 0:
            raise ValueError("Quantity can't be negative ")

        self._quantity = n

    def restock_product(self, n):

        if not isinstance(n, int):
            raise ValueError("Restock quantity must be int")

        if n > 0:
            self.quantity += n

        else:
            raise ValueError("cant restock with negative quantity ")

    def sell_product(self, n):

        if not isinstance(n, int):
            raise ValueError("Selling product's quantity must be int ")

        if not n > 0:
            raise ValueError("Selling Quantity can't be negative ")

        if not 0 < n <= self.quantity:
            raise ValueError("Not enough quantity to sell ")

        self.quantity -= n

    def numeric_id(self):

        return int(self.id[1:])
