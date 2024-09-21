class Employee:
    def __init__(self,name,company):
        self.name=name
        self.company=company
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0], string.split("-")[1])
e1=Employee("Sagar","Microsoft")
print(e1.name)
print(e1.company)  

string="Krishna-infosys"
e2=Employee.fromStr(string)
print(e2.name)
print(e2.company)
#for the string and the integer combine
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def from_string(cls,string):
        name,age=string.split(',')
        return cls(name,int(age))
person=Person.from_string("Ankita,8")
print(person.name,person.age)    
