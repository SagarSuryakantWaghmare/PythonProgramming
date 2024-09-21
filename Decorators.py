
def greet(fx):
    def mfx():
      print("Good morning")
      fx()
      print("Thanks for using")
    return mfx
@greet    
def hello():
    print("Hello world")

hello()   #or greet(hello)()
#For the arguments
def greet(fx):
   def mfx(*args,**kwargs):
      print("Good morning")
      fx(*args,**kwargs)
      print("Thanks for using the function")
   return mfx  
@greet
def hello():
   print("Hello World")
@greet
def add(a,b):
   print(a+b)
hello()
greet(add)(2,3)  