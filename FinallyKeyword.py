# final block is always executed
# Syntax for the Finally block
# try:
#     statement which could generate Exception
# except:
#     solution of generated Exception
# finally:
#     block of code which is going to executed in any situation  
def func1():
  try:
    l=[1,3,4,6]
    i=int(input("Enter the index:"))
    print(l[i])
  except:
    print("Some error occurred")
  finally:
    print("Thank you")  
x=func1()
print(x)   
print("ok") 