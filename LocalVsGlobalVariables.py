# x=4 #global variable
# print(x)
# def hello():
#     x=5#local variable
#     print(x)
#     print(f"The local  x is:{x}")
#     print("Hello Guys")
# print(f"The global x is:{x}")
# hello()  
# x=5 
# print(f"The global x is:{x}")
#Using the global keyword
x=10


def function():
    global x
    x=4
    y=5
    print(y)
function()
print(x)    