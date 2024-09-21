#Union of the two Sets
e={0,2,4,6,8,10}
o={1,3,5,7,9}
print(o.union(e))
print(e,o)
#By the Update
e.update(o)
print(e)
#Union of the two sets which are the String
# cities={"Tokyo","Madrid","Berlin","Delhi"}
# cities2={"Tokyo","Kabul","Seoul","Madrid"}
# cities3=cities.union(cities2)
# print(cities3)
# cities.intersection_update(cities2)
# if we use the third variable then we directly use the intersection only
# print(cities)
# Symmetric Difference
# a SD b=(a-b)union(b-a)
#We directly cut the intersection of part in sets
# cities3=cities.symmetric_difference(cities2)
# print(cities3)
# cities3=cities.difference(cities2)
# print(cities3)
# The disjoint() method checks if items of given set are present in another set .This method gives false if items are present,else false.
e={0,2,4,6,8,10}
o={1,3,5,7,9}
print(e.isdisjoint(o))#it gives the True because the there is no common elements in sets
# issuperser() method checks if all the items of a particular set are present in the original set.
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Kabul","Seoul"}
print(cities.issuperset(cities2))
cities3={"Madrid","Delhi"}
print(cities.issuperset(cities3))
# add or update method if we want to add item in the cities
cities.add("Chhatrapati Shambhajnagar")
print(cities)
# remove or discard method
cities.remove("Delhi")
print(cities)
#pop method is used to removes the last item but it is in unordered
cities={"Tokyo","Madrid","Berlin","Delhi"}
item=cities.pop()
print(cities)
print(item)
# del is not the method ,rather it is a keyword which deletes the set entirely
cities={"Tokyo","Madrid","Berlin","Delhi"}
del cities
# print(cities)this gives error
#clear is clear all the set and prints the empty set
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities.clear()
print(cities)
info={"Sagar",20,"SecondYear",True}
if "Sagar" in info:
    print("Sagar is present")
else:
      print("Sagar is  not present")   
      print("try again")