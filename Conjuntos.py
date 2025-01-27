#Para crear un conjunto, se utiliza la funcion set():
#Creacion
frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

#Los conjuntos adminte operaciones matematicas de conjuntos, como la union ( | ), la
#interseccion ( & ), la diferencia ( - ), y la diferencia simetrica ( ^ ).
union = conjunto1 | conjunto2
print(union) #imprime {1, 2, 3, 4, 5}

interseccion = conjunto1 & conjunto2
print(interseccion) #Imprime {3}

diferencia = conjunto1 - conjunto2
print(diferencia)   #Imprime {1, 2}

diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica) #Imprime {1, 2, 4, 5}

#Metodos de conjuntos

#add(elemento): agrega un elemento al conjunto
#remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.
#discard(elemento): elimina un elemento del conjunto si esta presente. Si el elemento no existe, no hace nada.
#clear(): elimina todos los elementos del conjunto.

frutas = {"manzana", "banana", "naranja"}


frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()

