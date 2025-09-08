class Car {
  constructor(brand, model, pricePerDay, available = true) {
    this.brand = brand;
    this.model = model;
    this.pricePerDay = pricePerDay;
    this.available = available;
  }

  rentCar(days) {
    if (!this.available) {
      console.log(`${this.brand} ${this.model} is not available right now.`);
      return;
    }
    this.available = false;
    const totalCost = days * this.pricePerDay;
    console.log(
      `You rented ${this.brand} ${this.model} for ${days} day(s). Total cost: $${totalCost}`
    );
  }

  returnCar() {
    this.available = true;
    console.log(`${this.brand} ${this.model} has been returned and is now available.`);
  }

  getInfo() {
    console.log(
      `${this.brand} ${this.model} - $${this.pricePerDay}/day - ${
        this.available ? "Available" : "Not Available"
      }`
    );
  }
}

let car1 = new Car("Toyota", "Corolla", 40);
let car2 = new Car("Hyundai", "Creta", 60);
let car3 = new Car("Maruti", "Swift", 30);

car1.getInfo();
car2.getInfo(); 
car3.getInfo();

car1.rentCar(3); 
car1.getInfo();  

car1.rentCar(2); 
car1.returnCar();
car1.getInfo();
