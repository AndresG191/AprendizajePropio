#A medida que nuestros programas crecen en tamaño y complejodad, es una buena practica de organizar
#nuestro codigo en modulos separados segun su funcionalidad.
#Esto nos permite conservar un codigo más legible, agrupado en modulos y facil de mantener.

#Por ejemplo, se pueden tener modulos operaciones.py relacionada a operaciones matematicas
#y otro utilidades.py que contenga funciones de uso general.

#operaciones.py
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

#utilidades.py
def imprimir_mensaje(mensaje):
    print(mensaje)

def obtener_nombre_usuario():
    return input("Ingresa tu nombre: ")

#Luego, podemos importar y utilizar estas funciones en nuestro programa principal.
#import operaciones
#import utilidades
#
# resultado = operaciones.sumar(5, 3)
# utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")
#
# nombre = utilidades.obtener_nombre_usuario()
# utilidades.imprimir_mensaje(f"Hola, {nombre}")

#Al organizar nuestro codigo en modulos, podemos reutilizar funciones y mantener un codigo mas estructurado y agrupado en modulos.