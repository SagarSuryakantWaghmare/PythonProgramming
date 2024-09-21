class Employee:
    company="Microsoft"
    def show(self):
       print(f"The name is {self.name} and the company is {self.company}")
     
    @classmethod#if we don't use the class method then the company is not changed
    def changeCompany(clg,newCompany):
        clg.company=newCompany
e1=Employee()
e1.name="Sagar"
e1.show()   
e1.changeCompany("Apple")
e1.show()
print(Employee.company)
