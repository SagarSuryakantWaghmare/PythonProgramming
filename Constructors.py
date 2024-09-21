# Syntax of the constructor
# def __init__(self):
class student():
    def __init__(self,n,a):
        print("Today I complete the 60Days doing the python")
        self.name=n
        self.age=a
    def info(self):
        print(f"{self.name} Age is {self.age}")    
a=student("sagar",20)
b=student("Abhi",15)   
a.info()
b.info()   
#if only the self is present in the paramerter then it is default constructor  
