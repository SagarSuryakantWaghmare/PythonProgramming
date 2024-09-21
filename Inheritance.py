class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"The name of employee:{self.id} is {self.name}")    

class Programer(Employee):
    def showLanguage(self):
        print("The default language is python")
e1=Programer("Sagar",2139)   
e1.showDetails()
e1.showLanguage()
e2=Employee("Nikhil",2140)
e2.showDetails() 