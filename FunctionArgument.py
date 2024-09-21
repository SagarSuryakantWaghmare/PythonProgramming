def average(a=4,b=2):
    print("The average of the numbers",(a+b)/2)
#for calling the function    
average()    #output for this is 3
average(5,8)#then the get the argument form the given form the calling funtion
average(2)  #in this ex a=2 not the a=4 and take b=2
def greet(name="sagar",surname="Waghmare"):
    print("hello",name,surname)
greet("Krishna")    
greet(surname="Garad")
greet(surname="Waghmare",name="Nikhil")
# variable length argument
def average(*numbers):
    #print(type(numbers))
    sum=0
    for i in  numbers:
        sum=sum+i
    return sum/len(numbers)   
c=average(5,6,7,4,3)  
print(c)     
#for the names by variable length arguments
def name(**name):
    print(type(name))
    print("Hello ",name["fname"],name["mname"],name["lname"])
name(fname="Sagar",mname="Suyakant",lname="Waghmare")    