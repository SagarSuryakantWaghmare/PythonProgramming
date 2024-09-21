# dir()method
# x=[1,2,3,4]
# print(dir(x))
# print(x.__len__)
# __dict__attribute
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1
p=person("Sagar",20)
print(p.__dict__) 
# help for help of the documentation      
print(help(str)) 