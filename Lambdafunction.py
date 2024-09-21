#Using the lambda function the we make function in one line
#function
# def square(x):
#     return x*x
#lambda function
square=lambda x:x*x
print(square(4))
cube=lambda x:x*x*x
print(cube(2))
avg=lambda x,y,z:(x+y+z)/3
print(avg(9.2,9.1,9.0))

  
  #function to function passing
def appl(fx,value):
    return 6+fx(value)
print(appl(lambda x:x*x*x,2))
   #In this way we pass the function to funv=ction