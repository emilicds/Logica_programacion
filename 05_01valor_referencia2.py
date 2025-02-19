### PRUEBAS ###

# variables

a = 20
b = 3 

# ops 

a = b 
b *= 4

print(a)
print(b)


# diferencias de asignacion 

print()

# creacion de variable 
numero1 = 100
resultado = numero1 +100   # se crea una variable exclusiva para la operacion
print(resultado)

#indentacion 
numero2 = 100
numero2 += 100   # += es identacion 
print(numero2)




# indentacion lista

c = 1
d = 3
e = 0

my_list = []

def iteracion (c,d,e, my_list):


    if c % 2 == 0:
        my_list.append(1)
    else: 
        my_list.append("error")


    if d == 3:
        my_list.append(2)
    else:
        my_list.append("error")


    if e != 0:
        my_list.append(3)
    else:
        my_list.append("error")


    return my_list




resultado1 = iteracion (c,d,e, my_list)
print(resultado1)

# promedio de una lista 

neutro = 0
lista2 = [2,6,7,8]

def promedio (neutro, lista2):
    for element in lista2:
        neutro += element
    return neutro / len(lista2)

resultado3 = promedio (neutro, lista2)
print(resultado3)

