#Para obtener la informacion del usuario durante la ejecucion del programa, podemos
#utilizar la funcion input()

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

print("Hola, " + nombre + "!")
print("Wow, tienes "+ edad + " años.")
print("------------------------------")

#IMPORTANTE
#La funcion input() siempre devuelve una cadena de texto. Si deseas trabajar con otros
#tipos de datos, como números enteros o flotantes, debes realizar una conversion explicita
#utilizando funciones como int() o float().

edad = int(input("Ingresa tu edad: "))

if edad >=18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#Salida de datos, podemos utilizar la f-string (formateo de cadenas) para incrustar
#variables directamente dentro de una cadena de texto.

nombre = "Juan"
edad = 25

print(f"Hola, mi nombre es {nombre} y tengo {edad} años:)")