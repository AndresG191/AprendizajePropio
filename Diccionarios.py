#Diccionarios
#Es una estructura de datos mutable y no ordenada que permite almacenar
#pares de clave-valor, los diccionarios se encierran con {}
#Los pares valor se separan por comas

#Creacion y acceso

persona ={"nombre": "Juan", "Edad":25, "Ciudad": "Madrid"}

print(persona["nombre"]) #Imprime "Juan"
print(persona["Edad"])   #Imprime "25"
print(persona["Ciudad"]) #Imprime "Madrid"

#Metodos de diccionarios
#Keys(): devuelve una vista de todas las claves del diccionario
#values(): devuelve una vista de todos los valores del diccionario
#items(): devuelve una vista de todos los pares clave-valor del diccionario.
#update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.

#Ejemplo

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(persona.keys())
print(persona.values())
print(persona.items())

persona.update({"profesion": "Ingeniero"})
print(persona)
