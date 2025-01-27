#Podemos abrir archivos en diferentes modos, como lectura ("r"), escritura ("w")
#o anexar ("a"), y realizar operaciones de lectura y escritura

#Para leer el contenido de un archivo, primero debemos abrirlo utilizando la funcion open()
#en modo de lectura ("r"). Luego, podemos leer el contenido del archivo utilizando metodos
#como read() o readlines().

archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

#Escritura de archivos
#Para escribir datos en un archivo, lo abrimos en modo escritura ("w") utilizando la funcion open().
#Si el archivo no existe, se creará automaticamente. Si el archivo ya existe, su contenido se sobrescribirá.

archivo = open("datos.txt", "w") #w --> writte
archivo.write("Hola, mundo!")
archivo.close()

#IMPORTANTE
#Es importante cerrar siempre los archivos despues de utilizarlos para liberar los recursos del sistema.

#También podemos utilizar la declaracion "with" para manejar la apertura y cierre de los archivos de manera automatica.

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
#El archivo se abre utilizando la declaracion with y se cierra automaticamente una vez
#que se sale del bloque with, incluso si ocurre una excepcion.
