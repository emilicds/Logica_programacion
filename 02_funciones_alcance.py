
# funcion basica 

def saludo():
    print("hola python! ")

saludo()

# funcion con return 

def saludo2():
    return "hello World"

saludo = saludo2()
print(saludo)  # al usar return el resultado se debe guardar en una variable para ser utilizado 


# funcion con valor por defecto 


def greet(nombre = "noname"): #establecemos valor por defecto 
    print("hello", nombre)

greet()

# Funcion con doble retorno 

lenguaje = "python"
nombre = "emi"

def multiple_retorno():
    return "hi", "python"

saludo3 , nombre2 = multiple_retorno()
print(saludo3) 
print(nombre2)

# funcion de recurso pre existente

palabra = input("escribe una palabra: ")

def up(palabra):
    return palabra.upper()

resultado = up(palabra)
print(resultado)

#####################################################

# VARIABLE GLOBAL Y LOCAL 

global_var = "python" # variable global , se puede acceder siempre a ella

def fun():
    local_var = "hello" # variable local , solo es propia de una funcion
    print(f"{local_var.upper()} ,{global_var} ")

fun()
