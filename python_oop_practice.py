# Python OOP Practice
# Classes, Objects, Methods and Constructors

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def start(self):
        print(self.brand, self.model, "is starting...")


# Creating objects
car1 = Car("Toyota", "Fortuner", 2025)
car2 = Car("BMW", "M4", 2026)

# Using objects
car1.show_details()
car1.start()

print()

car2.show_details()
car2.start()


# Student class practice
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            print(self.name, "has passed.")
        else:
            print(self.name, "has failed.")

    def show_marks(self):
        print(self.name, "scored", self.marks, "marks.")


student1 = Student("Saumay", 85)
student2 = Student("Aman", 35)

student1.show_marks()
student1.result()

print()

student2.show_marks()
student2.result()
