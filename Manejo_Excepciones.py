#El bloque try contiene el codigo que puede generar una excepcion. Si ocurre una
#excepcion dentro del bloque try, el flujo de ejecucion se transfiere al bloque
#excep correspondiente.
try:
    #Codigo que puede generar una excepcion
    resultado = 10 / 0 #Division por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")

#El bloque except especifica el tipo de excepcion que se desea capturar y manejar
#Puedes tener multiples bloques except para manejar diferentes tipos de excepciones

try:
    #Codigo que puede generar una excepcion
    resultado = 10 / 0 #Division por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: Division por cero")
except ValueError:
    print("Error: Valor invalido")

#El bloque FINALLY es opcional y se ejecuta siempre, independientemente de
#si ocurrió una excepcion o no. Se utiliza comunmente para realizar tareas de limpieza
#o liberacion de recursos

try:
    #Codigo que puede generar une excepcion
    archivo = open("archivo.txt", "r")
    #Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close() #Cerrar el archivo siempre, incluso si ocurre una excepcion