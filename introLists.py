#Tuple can't change but list can change
# for the numbers
marks=[10,9,7,8,9]
print(marks)
print(type(marks))
print(marks[0])
for i in range(0,5):
    print(marks[i])
# shortcut for the printing the marks
print(marks[:])   #for this it take start to 0 and end to last  
print(marks[1:4:2])  #for this silcing first form the 1 to 4 and then for the list it get 1 and 2
#for the string
lst1=["good","hi","bye","Sagar"]   
print(lst1)   
# combination of the string and num 
lst2=[3,"hi"]
print(lst2)
# in list index start form the index 0 to n
print(lst2[0]) #output for this is 3
print(len(lst2))#output is like no of elements
print(marks[-3])#negative index
print(marks[len(marks)-3])#convert of the negative to positive index
if 10 in marks:
    print("yes")
else:
    print("no")    
if "saga" in "sagar":
    print("yes")  
  #list comprehension
lst4=[i for i in range(4)]
print(lst4)
lst4=[i*i for i in range(4) if i%2==0]
print(lst4)
lst4=[i for i in range(4) if i%2==0]
print(lst4)
        
