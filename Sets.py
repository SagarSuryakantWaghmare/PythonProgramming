# sets are unordered we can write sets in {} and sets cannot change
s={2,4,5,7}
print(s)
info={'sagar',20,True,5.9}
print(info)
Sagar={}
print(Sagar)
print(type(Sagar))#output for this is <class 'dict'> because this syntax for the dict and sets are same
Sagar=set()#for making the null sets
print(type(Sagar))
#for loop for the set
for value in info:
    print(value)
    #output is in the unordered because in the set order is not importannt