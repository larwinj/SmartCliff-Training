class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ₹{self.price}"