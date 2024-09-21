a=(input("Enter the number:"))
print(f"Multiplication table of {a} is:")
try:
   for i in range(1,11):
    print(f"{int(a)}X{i}={int(a)*i}")
except Exception as e:
  #we can also use the except:
  print("Invalid input")
print("Code is executed")   
# Wrong input error in the int
try:
  a=int(input("Enter the number:"))
  b=[8,4]
  print(b[a])

except ValueError:
  print("Entered value error") 
except IndexError:
  print("Index Error")   
#we can give the two error at once  