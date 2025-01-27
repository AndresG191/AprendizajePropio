#Tuplas
#Creacion de tupla:
punto = (3,4)

#Acceder a elementos
print(punto[0]) #imprime 3
print(punto[1]) #imprime 4
#Las tuplas no se pueden modificar una vez creadas.

#count(elemento): devuelve el numero de veces que aparece un elemento en la tupla
#index(elemento): devueve el indice de la primera aparicion de un elemento en la
#tupla. Opcionalmente, se puede especificar el inicio y fin de la busqueda.
#len(tupla): aunque no es un metodo de tupla, esta funcion incorporada devuelve la longitud de la tupla.

mi_tupla = (1, 2, 3, 2, 4, 2)

print(mi_tupla.index(2))                    #salida: 1
print(mi_tupla.index(2,2))    #salida: 3
print(mi_tupla.index(2,2, 4))  #salida: 3