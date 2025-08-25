from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employeeID, name):
        self.employeeID = employeeID
        self.name = name

    def displayInfo(self):
        print(f"Employee ID: {self.employeeID}, Name: {self.name}")

    @abstractmethod
    def calculateSalary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, employeeID, name, monthlySalary):
        super().__init__(employeeID, name)
        self.monthlySalary = monthlySalary

    def calculateSalary(self):
        return self.monthlySalary


class PartTimeEmployee(Employee):
    def __init__(self, employeeID, name, hourlyRate, hoursWorked):
        super().__init__(employeeID, name)
        self.hourlyRate = hourlyRate
        self.hoursWorked = hoursWorked

    def calculateSalary(self):
        return self.hourlyRate * self.hoursWorked


class ContractEmployee(Employee):
    def __init__(self, employeeID, name, contractDuration, fixedMonthlyPayment):
        super().__init__(employeeID, name)
        self.contractDuration = contractDuration
        self.fixedMonthlyPayment = fixedMonthlyPayment

    def calculateSalary(self):
        return self.contractDuration * self.fixedMonthlyPayment

if __name__ == "__main__":
    # Full-time employee
    emp1 = FullTimeEmployee(95, "Larwin", 50000)
    emp1.displayInfo()
    print(f"Full-time Salary: {emp1.calculateSalary()}\n")

    # Part-time employee
    emp2 = PartTimeEmployee(84, "Kavin", 500, 40)
    emp2.displayInfo()
    print(f"Part-time Salary: {emp2.calculateSalary()}\n")

    # Contract employee
    emp3 = ContractEmployee(114, "Navadin", 6, 30000)
    emp3.displayInfo()
    print(f"Contract Salary: {emp3.calculateSalary()}\n")