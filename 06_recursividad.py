
# RECURSIVIDAD 
# no siempre la recursividad es optima 

# numeros del 0 al 100 

# sin recursividad

def creacion ():
    for number in range (0 , 101):
        print(number)

creacion ()
print("=================")


# con recursividad 

def count (num : int):
    if num < 100:
        num += 1 
        print(num)
        count(num)

count(-1)
print("================")
# numeros del 100 al 0 

# sin recursividad

def down (number : int):
    while number > 0 :
        number -=1
        print(number)

down (100)
# sin recursividad




# factorial 

#1 metodo emi 

print("=================")
numero = 5 

def factorial (numero):
    neutro = 1 #variable local
    for element in range (1, numero +1):
        neutro *= element 
    return neutro 

data = factorial (numero)
print(data)

# metodo recursividad



####

