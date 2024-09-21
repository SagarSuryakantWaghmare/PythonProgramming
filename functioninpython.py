#user defined function
#calculate the mean by the function
def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
a=9
b=8
# gmean=(a*b)/(a+b)
# print(gmean)
calculateGmean(a,b)
c=8
d=7
# gmean=(c*d)/(c+d)
# print(gmean)
calculateGmean(c,d)
#calculate the max no by the function
def MaxNumber(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater")
# m=int(input("Enter the first number"))
# n=int(input("Enter the second number"))
m=6
n=8

MaxNumber(m,n)
o=7
p=6
MaxNumber(o,p)  
def MinNumber(a,b):
    if(a<b):
        print("First number is less")
    else:
        print("Second number is less") 
MinNumber(m,n)
MinNumber(o,p) 
#for printing the user greet
def greetUser(name,surname):
    print("Good Morning",name,surname)
name="Sagar"
surname="Waghmare"
greetUser(name,surname)       
#in built function            