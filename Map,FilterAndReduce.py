def square(x):
    return x*x
print(square(4))
#for the list normal method
l=[1,3,5,7,8]
# newl=[]
# for item in l:
#     newl.append(square(item))

#By the map 
#syntax of the map:list(map(fn,iteration))
newl=list(map(square,l))
print(newl)
# filter function
def filter_function(x):
    return x>5
new2l=list(filter(filter_function,l))
print(new2l)
#Reduce functions
from functools import reduce
def mysum(x,y):
    return x+y
l1=[1,2,6,8,9,7]
sum=reduce(mysum,l1)
print(sum)

