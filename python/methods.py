class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello,", self.name)

student1 = Student("Hema")
student1.greet()