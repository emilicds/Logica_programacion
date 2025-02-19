
# VALOR Y REFERENCIA 


# tipos de datos por valor 


my_int_a = 10
my_int_b = 2 

my_int_b = my_int_a  # b pasa a valer lo que vale a en esa instancia del programa , si a cambia a futuro , no se vera afectado b 
                # b guarda el valor de a en ese punto del programa 

my_int_a = 14   # como esta fue la ultima orden antes del print a cambia su valor 

print(my_int_a)
print(my_int_b)

# b no cambio su valor 
print()
print()



# tipos de dato por referencia 
# son datos que no son primitivos 

my_list_a = [10 , 20]
my_list_b = [30 , 40]

my_list_b = my_list_a    # asignacion de b - a 
my_list_b.append(30)     # la referencia comparte el mismo espacio de memoria , las variables se mutan a futuro 
my_list_b.append("holi") # no se queda estatico como en el valor 

print(my_list_a)
print(my_list_b)

 


