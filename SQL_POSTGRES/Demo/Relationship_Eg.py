from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/mydb")  # SQLite DB
Session = sessionmaker(bind=engine)
session = Session()

# ------------------------------------
# Many-to-Many Association Table
# ------------------------------------
product_supplier = Table(
    "product_supplier", Base.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("supplier_id", ForeignKey("suppliers.id"), primary_key=True)
)

# ------------------------------------
# One-to-Many: Category → Product
# ------------------------------------
class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(name={self.name})>"

# ------------------------------------
# Product & ProductDetail (1:1)
# ------------------------------------
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="products")
    detail = relationship("ProductDetail", uselist=False, back_populates="product")
    suppliers = relationship("Supplier", secondary=product_supplier, back_populates="products")

    def __repr__(self):
        return f"<Product(name={self.name})>"

class ProductDetail(Base):
    __tablename__ = "product_details"
    id = Column(Integer, primary_key=True)
    description = Column(String)
    product_id = Column(Integer, ForeignKey("products.id"))

    product = relationship("Product", back_populates="detail")

    def __repr__(self):
        return f"<ProductDetail(description={self.description})>"

# ------------------------------------
# Many-to-Many: Product ↔ Supplier
# ------------------------------------
class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    products = relationship("Product", secondary=product_supplier, back_populates="suppliers")

    def __repr__(self):
        return f"<Supplier(name={self.name})>"

# ------------------------------------
# Create Tables
# ------------------------------------
Base.metadata.create_all(engine)

# ------------------------------------
# Insert Sample Data
# ------------------------------------
# Categories
cat1 = Category(name="Electronics")
cat2 = Category(name="Stationery")

# Products (1:N with Category)
p1 = Product(name="Laptop", category=cat1)
p2 = Product(name="Smartphone", category=cat1)
p3 = Product(name="Notebook", category=cat2)

# Product Details (1:1)
p1.detail = ProductDetail(description="Intel i7, 16GB RAM, 512GB SSD")
p2.detail = ProductDetail(description="5G, 128GB Storage, Dual Camera")
p3.detail = ProductDetail(description="200 Pages, A4 Size")

# Suppliers (M:N)
s1 = Supplier(name="Tech Distributors Inc.")
s2 = Supplier(name="Global Supplies Ltd.")

p1.suppliers = [s1, s2]   # Laptop supplied by both
p2.suppliers = [s1]       # Smartphone supplied by Tech Distributors
p3.suppliers = [s2]       # Notebook supplied by Global Supplies

session.add_all([cat1, cat2, p1, p2, p3, s1, s2])
session.commit()

# ------------------------------------
# Queries
# ------------------------------------
print("\n--- One-to-One ---")
print(p1.name, "details:", p1.detail.description)

print("\n--- One-to-Many ---")
print(cat1.name, "category has products:", [p.name for p in cat1.products])

print("\n--- Many-to-Many ---")
print(p1.name, "supplied by:", [s.name for s in p1.suppliers])
print(s2.name, "supplies:", [p.name for p in s2.products])
