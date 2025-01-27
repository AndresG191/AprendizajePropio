#Para crear un modulo personalizado, creamos un nuevo archivo python y definimos las funciones, clases y variables
#que queremos incluir en el modulo. Por ejemplo, creamos un archivo (en el mismo directorio donde ejecutamos Python)
#llamado mi_modulo.py con el siguiente contenido:

#mi_modulo.py
def saludar(nombre):
    print(f"Hola,{nombre}!")

def calcular_suma(a,b):
    return a + b
#Luego, podemos importar y utilizar las funciones definidas en " mi_modulo.py " en otro archivo python

