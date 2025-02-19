### CLASES ###

class Animal:
    def __init__(self , animal):
        self.animal = animal
    def caminar (self ):
        print(self.animal , "esta caminando")
    def comer (self):
        print(self.animal , "esta comiendo")
    def dormir (self):
        print(self.animal, "esta durmiendo")
        

myanimal = Animal ("tigre")
myanimal.caminar()
myanimal.comer()
myanimal.dormir()

# asignamos una variable a la clase "animal" con el nombre "tigre" para que asi las funciones asignadas a nuestra clase puedan trabajar
# myanimal.caminar()








