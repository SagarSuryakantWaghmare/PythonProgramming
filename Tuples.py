tup=(1)
print(type(tup),tup)#for the single element we have write the(1,) in tuple otherwise the type is like int
tup=(1,)
print(type(tup),tup)
tup=(1,5,6)
print(type(tup),tup)
# we can add the string and the number int tuple
tup=(1,3,5,8,"soham")
print(type(tup),tup)
# we can also print the tup by the index like form the 0,1,2,3,4 and so on.
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
if "soham" in tup:
    print("soham is present in tuple")
else:
    print("soham is not present in the tuple")
#we can also get the length of the tub
print(len(tup))  
print(tup[-2]) #we can also get the negative like  the (tup[len(tup)-3])  
tup2=tup[1:4]
print(tup2)