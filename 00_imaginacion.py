### Imaginacion ###
""""

# opcion 1
neutro = 0

for x in range (1, 11):
    neutro+= x
print(neutro)

# opcion 2 

n = int(input("escribe un numero : "))

print( (n*(n+1))/2 )


#2

neutro2 = 0 

for y in range (1,6):
    neutro2 += 2**y 
print(neutro2)


#3 


neutro = 0 
for x in range (1,6):
    neutro += x**x
print(neutro)


#4


lista = [1,4,6,3,7]
neutro = 0 

for element in lista:
    neutro += element
print(neutro)



# algoritmo suma 

inicio = 1
limite = 5
neutro = 0 

def algoritmo_suma (neutro , inicio , limite):
    for x in range(inicio , limite +1): 
        neutro += x**x
    return neutro 

resultado = algoritmo_suma (neutro , inicio , limite)
print(resultado)


print()
print()

num = int(input("escribe un numero, : "))
neutro = 1
def factorial(num, neutro):
    for x in range (1, num +1 ):
        neutro *= x
    return neutro


result = factorial(num, neutro)
print(result)


def cont ():

    psw1 = input("escribe una pasword: ")

    while True:
        psw2 = input("reescribe la contraseña para confirmar: ")
        if psw1 != psw2:
            print("error , contraseñas incorrectas")
        else: 
            print("confirmacion exitosa")
            break 

cont()


max = int(input("escribe un numero para mostrar su orden entero: "))
num = 0

def count(max, num):
    if num < max:
        num +=1
        print(num)
        count(max, num)
    else:
        print("termino el proceso")

count (max, num)

"""

def factorial (num : int):
    if num == 1 :
        return 1
    else :
        return num * factorial(num -1)


result = factorial (4)
print(result)

