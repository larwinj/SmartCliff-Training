from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class ElectricVehicle(ABC):
    @abstractmethod
    def charge(self):
        pass


class GasVehicle(ABC):
    @abstractmethod
    def refuel(self):
        pass

class ElectricCar(Vehicle, ElectricVehicle):
    def start(self):
        print("ElectricCar started silently with battery power.")

    def stop(self):
        print("ElectricCar stopped smoothly.")

    def charge(self):
        print("ElectricCar is charging at the station.")


class GasMotorcycle(Vehicle, GasVehicle):
    def start(self):
        print("GasMotorcycle engine roars to life with fuel ignition.")

    def stop(self):
        print("GasMotorcycle engine turned off.")

    def refuel(self):
        print("GasMotorcycle is being refueled at the gas station.")

if __name__ == "__main__":
    tesla = ElectricCar()
    tesla.start()
    tesla.charge()
    tesla.stop()

    print("-" * 40)

    harley = GasMotorcycle()
    harley.start()
    harley.refuel()
    harley.stop()