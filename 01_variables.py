
# VARIABLE Y ASIGNACION 

numero = 10 
print(numero)

numero +=10  # suma y asignacion 
print(numero)

numero -=3 
print(numero)

numero *=2 
print(numero)

numero /=2
print(numero)

numero **=2 
print(numero)


# va copilando con el numero 10 asignado al inicio 

# INTERPOLACION 

numero1 = 10
numero2 = 4

print(f"numero 1 + numero 2 es igual a : {numero1 + numero2}") # estructura fija de ejecucion de una operacion 
print(f"numero 1 - numero 2 es igual a : {numero1 - numero2}")


# PERTENENCIA 

nombre = "Emilio"
print("u"in nombre) # busca un elemento igual dentro de una variable str

nombre2 = "mexico"
print("a" not in nombre2)
 

# FLUJO ITERATIVO 

for x in range (1,11):
    print(x)

# FLUJO DE ERRORES 

try:
    print(10/0)
except:
    print("error en el sistema")
finally:
    print("recalculando...")

