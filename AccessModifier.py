#By the default it is public
# class Employee:
#     def __init__(self):
#         # self._name="Sagar"
#         #for the any vaiable like as _var then it become private
#         self.__name="Sagar"
#         #for the any varible for the name mangling

# a=Employee()
# # print(a._name)  #and access through the obj._name
# print(a._Employee__name)
#for the protected 
class Student:
    def __init__(self):
        self._name="Sagar"
    def _funName(self):#protected method
        return "Code by Sagar"
class boy(Student):#inheritale class
    pass
obj=Student()
obj1=boy()
#calling by object of student class
print(obj._name)
print(obj._funName())
#calling by object of boy class
print(obj1._name)
print(obj1._funName())

