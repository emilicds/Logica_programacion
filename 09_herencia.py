
### HERENCIA Y POLIFORMISMO ###

# crear nuevas clases en base a una pre esxistente 

# clase padre

class Animal:
    def __init__(self, name : str):
        self.name = name 

    def sound(self):
        pass

# subclases

class Dog(Animal):

    def sound(self):
        print("guau")



class Cat(Animal):

    def sound(self):
        print("miau")



my_dog = Dog("peky")
my_cat = Cat("li")

my_cat.sound()


#############

def print_sound(animal : Animal):
    animal.sound()


my_animal = Animal("animal") 
print_sound(my_animal)

my_dog = Dog("pepito")
print_sound(my_dog)


my_cat = Cat("leo")
print_sound(my_cat)


print()
#####################




