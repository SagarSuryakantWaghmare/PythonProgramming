#Heirarchical Inheritance 
class Animal:
    def speak(self):
        return "Animal Sound"
class Dog(Animal):
    def speak(self):
        return "Bark" 
class Cat(Animal):
    def speak(self):
        return "Meow"
a=Animal()
print(a.speak())    
dog=Dog()
print(dog.speak())
cat=Cat()
print(cat.speak())

#Hybrid Inheritance
class Animal:
    def speak(self):
        return "Animal sound"
class Dog(Animal):
    def speak(self):
        return "Bark" 
class Cat(Animal):
    def speak(self):
        return "Meow"
class B(Dog,Cat):
    def speak(self):
        return "KEEE"
b=B()
print(b.speak())
