# class ParentClass:
#     def parent_method(self):
#         print("I am the parent Class")
# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("Sagar")
#         super().parent_method()
#     def child_method(self):
#         print("I am the child class")    
#         super().parent_method()
# child_object=ChildClass()
# child_object.child_method()
# child_object.parent_method()
#new Example
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang
Krishna=Employee("Krishna",2008)
print(Krishna.name)
Sagar=Programmer("Sagar",2004,"Java")
print(Sagar.name)
print(Sagar.id)
print(Sagar.lang)
        