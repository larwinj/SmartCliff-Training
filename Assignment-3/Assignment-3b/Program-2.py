class Employee:
    def __init__(self):
        self.salary = 0
        self.hours = 0

    def getInfo(self, salary, hours):
        self.salary = salary
        self.hours = hours

    # Add $10 if salary < 500
    def AddSal(self):
        if self.salary < 500:
            self.salary += 10

    # Add $5 if work hours > 6
    def AddWork(self):
        if self.hours > 6:
            self.salary += 5

    def finalSalary(self):
        self.AddSal()
        self.AddWork()
        return self.salary

if __name__ == "__main__":
    emp = Employee()

    salary = float(input("Enter employee salary: "))
    hours = int(input("Enter working hours per day: "))

    emp.getInfo(salary, hours)
    print("Final Salary:", emp.finalSalary())
