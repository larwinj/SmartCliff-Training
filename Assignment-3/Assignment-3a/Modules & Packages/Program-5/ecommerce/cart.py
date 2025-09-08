from ecommerce.products import Product

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"Added: {product.name}")

    def remove_product(self, product_id):
        for product in self.items:
            if product.id == product_id:
                self.items.remove(product)
                print(f"Removed: {product.name}")
                return
        print("Product not found in cart.")

    def calculate_total(self):
        return sum(product.price for product in self.items)

    def show_cart(self):
        print("\nCart:")
        for product in self.items:
            print(product)
        print(f"Total before discount: ₹{self.calculate_total()}")
