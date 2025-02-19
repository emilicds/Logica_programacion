
# CADENAS DE TEXTO 
"""
s1 = "hola"
s2 = "Emi"

# cambio por terminal 

print(s1.upper())
print(s2.lower())

# concatenacion 

print(s1 + s2 + "," + "estos strings estan concatenados")

# repeticion 

print(s2 * 4) #repetira el string 4 veces 

# indexacion (busqueda)

print(s1[0]) # busqueda por caracter 
print(s1[3])

# Slicing por caracter 

print(s2[0:2]) # inicio : fin +1

# reemplazo 

print(s1.replace("o", "i"))  #reemplazando la o por la i

# division 

print(s2.split("m"))  #corte por la letra m 

# busqueda por inicio y fin 

print(s1.startswith("a"))
print(s2.endswith("i"))

"""

# EJERCICIO DE LOGICA 

# check 1 , palabra palindroma 


palabra1 = "reconocer"

def check1(palabra1):
    if palabra1 == palabra1[::-1]:
        print("esta palabra es palindroma")
    else:
        print("no son nada")

check1(palabra1)


# check palabra isograma

palabra2 = "calle"

def check2 (palabra2):
    if len(palabra2) == len(set(palabra2)):
        print("es un isograma")
    else:
        print("no es nada")


check2(palabra2)

