a=int(input("Enter any value between 5 and 9 :"))
if (a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")
class CustomError(Exception):
    print("out of the bound")
try:
    a=[1,3,5,7]    
    print(a[4])
except CustomError:
   CustomError(Exception)