class School:
    totalStudents = 0

    MAX_CAPACITY = 500
    @classmethod
    def enrollStudent(cls):
        if cls.totalStudents < cls.MAX_CAPACITY:
            cls.totalStudents += 1
            print("Student enrolled successfully.")
        else:
            print("Enrollment failed: School has reached maximum capacity!")

    @classmethod
    def getTotalStudents(cls):
        return cls.totalStudents

if __name__ == "__main__":
    for i in range(5):
        School.enrollStudent()

    print("Total students enrolled:", School.getTotalStudents())

    print("School Maximum Capacity:", School.MAX_CAPACITY)
