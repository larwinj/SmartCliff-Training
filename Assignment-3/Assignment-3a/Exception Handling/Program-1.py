# bookstore_inventory.py

def get_book_quantity():
    while True:
        try:
            qty = int(input("Enter quantity of books: "))
            return qty
        except ValueError:
            print("Error: Input should be a valid integer. Please enter quantity again.")


def get_book_price():
    while True:
        try:
            price = float(input("Enter price of the book: "))
            return price
        except ValueError:
            print("Error: Invalid price format. Please enter price again.")


def update_inventory(books):
    while True:
        try:
            index = int(input("Enter index to update book: "))
            print(f"Updating book at index {index}: {books[index]}")
            break
        except IndexError:
            print("Error: Index out of bounds. Please enter a valid index.")
        except ValueError:
            print("Error: Index should be an integer.")


if __name__ == "__main__":
    books = ["Book A", "Book B", "Book C"]

    # 1. Get Quantity
    quantity = get_book_quantity()
    print(f"Quantity entered: {quantity}")

    # 2. Get Price
    price = get_book_price()
    print(f"Price entered: {price}")

    # 3. Update Inventory
    update_inventory(books)
