# Custom Exceptions
class NegativeValueError(Exception):
    pass

class ZeroOrderError(Exception):
    pass

class OrderProcessor:
    def __init__(self, orders):
        self.orders = orders

    def process_orders(self):
        try:
            if not self.orders:
                raise ZeroOrderError("Order list cannot be empty.")

            total_cost = 0
            for order in self.orders:
                item, quantity, price = order

                # Validate data types
                if not isinstance(quantity, (int, float)) or not isinstance(price, (int, float)):
                    raise ValueError("Quantity and Price must be numbers.")

                # Check for negatives
                if quantity < 0:
                    raise NegativeValueError("Quantity cannot be negative.")
                if price < 0:
                    raise NegativeValueError("Price cannot be negative.")

                total_cost += quantity * price

            print(f"Total cost: ₹{total_cost}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except NegativeValueError as ne:
            print(f"Error: {ne}")
        except ZeroOrderError as zo:
            print(f"Error: {zo}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

orders1 = [("Laptop", 2, 50000), ("Mouse", 1, 1000)]
processor1 = OrderProcessor(orders1)
processor1.process_orders()

orders2 = [("Keyboard", -1, 2000)]
processor2 = OrderProcessor(orders2)
processor2.process_orders()

orders3 = []
processor3 = OrderProcessor(orders3)
processor3.process_orders()

orders4 = [("Monitor", "Two", 15000)]
processor4 = OrderProcessor(orders4)
processor4.process_orders()
