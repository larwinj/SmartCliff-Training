# Base class
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def displayInfo(self):
        print(f"Brand: {self.brand}, Year: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def displayCarInfo(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")


if __name__ == "__main__":
    brand = input("Enter car brand: ")
    year = int(input("Enter manufacturing year: "))
    model = input("Enter car model: ")

    car1 = Car(brand, year, model)

    print("\n--- Vehicle Info ---")
    car1.displayInfo()

    print("\n--- Car Info ---")
    car1.displayCarInfo()
