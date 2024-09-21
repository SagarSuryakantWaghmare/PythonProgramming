dic={
    "Sagar":"Student",
    "age":20,
    "year":2,
    "college":"DIEMS"
}
print(dic)
# print(dic["Rajat"]) this gives the error
print(dic["age"])
print(dic.get("Sagar"))
print(dic.keys())#for the keys
print(dic.values())#for the values
for key in dic.keys():
    print(dic[key])
print(dic.items())    
for key,value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")
print("Thank You")  