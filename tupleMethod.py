countries=("spain","Italy","India","England","Germany")
temp=list(countries)
temp.append("Russia")#add item
temp.pop(3)#remove element
temp[2]="Finland"#add element at the index
countries=tuple(temp)
print(countries)
boy=("sagar","krishna","nikhil")
girl=("ankita","kavita","Varsha")
family=boy+girl
print(family)
tuple1=(0,1,2,3,4,5,6,4,3)
rep=tuple1.count(4)
res=tuple1.index(3,1,4)#for the element to find the tup1 1 to 4
print("count the element 3 in the tuple:",rep)
print(res)