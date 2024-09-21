class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("Animal make sound")
# class Dog(Animal):
#     def __init__(self,name,bread):
#         Animal.__init__(self,name,species="Dog") 
#         self.bread=bread
#     def make_sound(self):
#         print("Bark")
# d=Dog("Sher","dogger")
# d.make_sound()
# a=Animal("Elephant","Royal")
# a.make_sound()     

#Quick Quiz
class Cat(Animal):
    def __init__(self,name,color):
        Animal.__init__(self,name,species="Wild")
        self.color=color
    def make_sound(self):
        print("Meow")  
c=Cat("Catu","Catgirl")
c.make_sound()
a=Animal("Elephant","Royal")
a.make_sound()            