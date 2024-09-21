class Student:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"The name of the Student is {self.name}")
class Programmer:
    def __init__(self,lang):
        self.lang=lang
    def show(self):
        print(f"The favourite language is {self.lang}")    
class StudentProgrammer(Student,Programmer):
    def __init__(self,name,lang):
        self.name=name
        self.lang=lang
s=StudentProgrammer("Sagar","Java")
print(s.name)
print(s.lang)
s.show()  
#mro method (sequence of the programmer for the finding the method)
print(StudentProgrammer.mro())
