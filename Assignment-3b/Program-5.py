class Student:
    def __init__(self, student_id=0, name="Unknown", age=0, grade="Unknown"):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


if __name__ == "__main__":
    student1 = Student()
    print("Student 1 (Default Constructor):")
    student1.display_info()

    student2 = Student(95, "Larwin", 20, "B.E(CSE)")
    print("\nStudent 2 (Parameterized Constructor):")
    student2.display_info()
