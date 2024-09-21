# Class in this way we do
class student():
    name="Sagar "
    Age=20
    Roll_no=2139
    # self keyword is instance of the object that used to access the current obect
    def info(self):
        print(f"{self.name} Age is {self.Age}")
#And the object is like shown below       
s=student()
s.name="Ram"
s.Age=20
k=student()
k.name="Krishna"
k.age=16
S=student()
# print(s.name,s.Age)
s.info()
k.info()
S.info()#we get the default value for this