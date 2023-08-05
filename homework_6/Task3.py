class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def promote(self):
        self.grade +=1

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

student = Student("Jane", 19, 4)
student.promote()
student.get_details()
