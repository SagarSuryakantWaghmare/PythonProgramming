# comments are ignored in the program
#docString :python docstring are strings used right after the definition of a function,method,class or module.
#They are used to document our code
print("docstring and pep-8")
def square(n):
    print(n)#for this the o/p is none because the docstring under the function
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)    
print(square.__doc__)