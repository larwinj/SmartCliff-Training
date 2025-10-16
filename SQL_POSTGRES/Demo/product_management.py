from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# -------------------------------
# Database Setup
# -------------------------------
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/productmanagement")  # SQLite DB
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

# -------------------------------
# Product Model
# -------------------------------
class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, default=0)

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, stock={self.stock})"

# Create table
Base.metadata.create_all(engine)

# -------------------------------
# CRUD Functions
# -------------------------------
def add_product(name, price, stock):
    product = Product(name=name, price=price, stock=stock)
    session.add(product)
    session.commit()
    print(f"Product '{name}' added successfully!")

def view_products():
    products = session.query(Product).all()
    if not products:
        print("No products found!")
    for p in products:
        print(p)

def update_product(product_id, new_price=None, new_stock=None):
    product = session.get(Product,product_id)
    if not product:
        print("Product not found!")
        return
    if new_price is not None:
        product.price = new_price
    if new_stock is not None:
        product.stock = new_stock
    session.commit()
    print(f"Product ID {product_id} updated successfully!")

def delete_product(product_id):
    product = session.get(Product,product_id)
    if not product:
        print("Product not found!")
        return
    session.delete(product)
    session.commit()
    print(f"Product ID {product_id} deleted successfully!")

# -------------------------------
# Menu-Driven Program
# -------------------------------
def menu():
    while True:
        print("\n--- Product Management System ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = int(input("Enter price: "))
            stock = int(input("Enter stock: "))
            add_product(name, price, stock)

        elif choice == "2":
            view_products()

        elif choice == "3":
            pid = int(input("Enter product ID to update: "))
            new_price = input("Enter new price (leave blank to skip): ")
            new_stock = input("Enter new stock (leave blank to skip): ")
            update_product(pid,
                           int(new_price) if new_price else None,
                           int(new_stock) if new_stock else None)

        elif choice == "4":
            pid = int(input("Enter product ID to delete: "))
            delete_product(pid)

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

# -------------------------------
# Run the Program
# -------------------------------
if __name__ == "__main__":
    menu()
