#Un paquete es una forma de organizar modulos relacionados en una estructura jerarquica de directorios.
#Los paquetes nos permiten agrupar modulos relacionados y evitar conflictos de nombres entre modulos

#Crear y utilizar paquetes

#Para crear un paquete creamos un directorio con el nombre deseado y agregamos un archivo especial
#llamado __init__.py dentro del directorio. Este archivo puede estar vacio o contener codigos de inicializacion del paquete.
#EJEMPLO
#
# mi_paquete/
#     __init__.py
#     modulo1.py
#     modulo2.py

#Luego, podemos utilizar los modulos del paquete en nuestro programa.
#
# from mi_paquete import modulo1, modulo2
# modulo1.funcion1()
# modulo2.funcion2()

x = 5
y = "3"
z = x + int(y)
print(z)