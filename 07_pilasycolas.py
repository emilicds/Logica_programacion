
### PILAS Y COLAS ###
# concecptos dentro de arrays

# Pila / stack (lifo)

# last in first out 

stack = []
#push
stack.append("1")
stack.append("2")
stack.append("3")
print(stack)

#pop
stack_item = stack[len(stack)-1]  # empieza e eliminar desde el ultimo que entro 
del  stack[len(stack)-1]

print(stack_item) # muestra ultimo elemento
print(stack)

print(len(stack))

print()

#cola / queue (fifo)
# first in first out 

cola = []
# encolar
cola.append("1")
cola.append("2")
cola.append("3")

print(cola)

#desencolar 

cola.pop(0)  #el elemento que se elimina es el primero que entra




# ejercicio buscador Web (pilas) (lifo)

web = []
print()
print("bienvenido al buscador web, elgie una de las siguientes opciones para navegar")
print ("regresar , adelante , salir")
print("la opcion por omision siempre sera buscar")
print()

def buscador ():
    dato = ".com"
    while True:
        enlace = input("escribe una pagina web para buscarla: ")
        if enlace == "regresar":
            print("se elimino", web[len(web)-1])
            web.pop()
            print(web)
        elif enlace == "adelante":
            print("error , no se puede volver debido a que la pestaña se cerro o no existe")
        elif enlace == "salir":
            print("saliendo....")
            print("estas en pantalla de inicio")
            break
        else:
            web.append(enlace + dato)
            print(web)

buscador()




# ejercicio colas (fifo)

documentos = []
print()
print("bienvenido a la impresora publica !!!")
print("interactua con las opciones: imprimir/cancelar")
print()

def impresion ():
    tipo = ".txt"
    while True:
        dato = input("escribe el nombre del documento a imprimir o la interaccion disponible: ")
        if dato == "imprimir":
            print("se imprimio el archivo", documentos[0])
            documentos.pop(0)
            print("los documentos en cola son", documentos)
            if len(documentos) == 0:
                print("sin arvhivos a imprimir...")
        elif dato == "cancelar":
            print("saliendo...")
            print("cancelado de impresion exitoso")
            break
        else:
            documentos.append(dato + tipo)
            print(documentos)

impresion()


