class Employee:
    companyName="Microsoft"
    noOfEmployee=0
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02
        Employee.noOfEmployee+=1
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployee} sized {self.companyName} is {self.raise_amount}")

emp1=Employee("Sagar")
emp1.raise_amount=0.4
emp1.companyName="Apple"
emp1.showDetails()
emp2=Employee("Rajat")
emp2.companyName="Infosys"       
emp2.showDetails()
print("Thank You")