#Lista de frutas
from Numeros import numero

frutas = ["Manzana", "Platano", "Uva"]

#Para acceder a los elementos de una lista
print(frutas[0], frutas[1], frutas[2])
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas)

#Metodos de listas
#append(elemento): agrega elemento al final de la lista
#insert (indice, elemento): inserta un elemento en una posicion especifica
#remove(elemento): elimina la primera aparicion de un elemento en la lista.
#pop(indice): elimina y devuelve el elemento en una posicion especifica de la lista
#sort(): ordena los elementos de la lista en orden ascendente
#reverse(): invierte el orden de los elementos de la lista.

frutas = ["Manzana", "Platano", "Uva"]

frutas.append("pera")
print(frutas)

frutas.insert(2, "Mango")
print(frutas)

frutas.remove("Uva")
print(frutas)

frutas_eliminada = frutas.pop(1)
print(frutas)
print(frutas_eliminada)

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)

#Listas de comprension

numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)
