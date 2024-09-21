#factorial(8)=8*7*6*5*4*3*2*1
# factorial(n)=n*factorial(n-1)
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))    
print(factorial(3))
print(factorial(5))
#handrun for this 5
# 5*factorial(4)
# 5*4*factorial(3)
# 5*4*3*factorial(2)
# 5*4*3*2*factorial(1)
# 5*4*3*2*1
# WOP for the fibonacci sequence
# f0=0
# f1=1
# f2=f0+f1
print("Fibonacci sequence")
f:0=0
f:1=1
f:2=f:0+f:1
def fibonacci(f(n)):
    if(n==0):
        print(n)
    elif(n==1): 
        print(1)  
    else:
       print (f(n)+f(n-1))
fibonacci(f(4))    
