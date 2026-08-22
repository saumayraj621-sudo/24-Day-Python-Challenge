# Python Classes and Objects
# Today's Class

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

    def study(self):
        print(self.name, "is studying Python.")


# Creating objects
student1 = Student("Saumay", 20, "CSE AIML")
student2 = Student("Rahul", 20, "CSE")

# Calling methods
student1.display_info()
student1.study()

print()

student2.display_info()
student2.study()


# Another example
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b


calc = Calculator()

print("\nCalculator Results:")
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(10, 5))
