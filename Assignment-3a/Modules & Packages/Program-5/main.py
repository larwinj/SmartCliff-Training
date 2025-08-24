from ecommerce.products import Product
from ecommerce.cart import Cart
from ecommerce.discounts import apply_discount

p1 = Product(101, "Laptop", 50000)
p2 = Product(102, "Mouse", 1000)
p3 = Product(201, "Phone", 30000)
p4 = Product(202, "Charger", 1500)
p5 = Product(203, "Case", 500)

# Initialize cart
cart = Cart()

print("=== Test Case 1 ===")
cart.add_product(p1)
cart.add_product(p2)
cart.show_cart()

total = cart.calculate_total()
discount = apply_discount(total, "DISCOUNT10")
final_total = total - discount

print(f"Discount: ₹{int(discount)}")
print(f"Final total: ₹{int(final_total)}\n")

# Reseting
cart = Cart()

print("=== Test Case 2 ===")
cart.add_product(p3)
cart.add_product(p4)
cart.remove_product(202)
cart.add_product(p5)
cart.show_cart()

total = cart.calculate_total()
discount = apply_discount(total, "SAVE20")
final_total = total - discount

print(f"Discount: ₹{int(discount)}")
print(f"Final total: ₹{int(final_total)}")