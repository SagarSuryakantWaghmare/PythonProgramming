class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def show_details(self):
        print(f"The name of the student is {self.name} and the roll no is {self.rollno}")

class Programmer(Student):
    def __init__(self, name, cgpa):
        Student.__init__(self, name, rollno=40) 
        self.cgpa = cgpa

    def show_details(self):
        Student.show_details(self)
        print(f"Student CGPA is {self.cgpa}") 

class Employee(Programmer):
    def __init__(self, name, lang):
        Programmer.__init__(self, name, cgpa="9")
        self.lang = lang

    def show_details(self):
        Programmer.show_details(self)
        print(f"Programming language is {self.lang}")

s = Student("Sagar", 40)
s.show_details()

p = Programmer("Sagar", 9)
p.show_details()

e = Employee("Sagar", "Java")
e.show_details()
