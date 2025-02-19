
# recursividad 2 

# NUMEROS DEL 0 AL 100 (COUNT)

# sin recursividad 

def conteo1 (num1 : int):
    for x in range (1,num1 +1):  # metodo mas facil
        print(x)

conteo1(4)

print()

# con recursividad 

def conteo2 (num2 : int):
    if num2 < 10:
        num2 += 1              # metodo mas complejo
        print(num2)
        conteo2(num2)

conteo2 (0)

print("===========")

####################################################

# NUMEROS DEL 10 AL 0 (COUNTDOWN)

#sin recursividad

def countdown1 (numero1 : int):
    while numero1 > 0:
        numero1 -= 1 
        print(numero1)

countdown1 (11)

# con recursividad

def countdown2 (numero2: int):
    if numero2 > 0:
        numero2 -=1 
        print(numero2)
        countdown2(numero2)

countdown2(5)

