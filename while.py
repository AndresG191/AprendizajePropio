# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2

comando = ""
#
# while comando != "Salir":
#     comando = input("$ ")#Cuando ingresemos algo dentro de la aplicacion, el comando se asigna a la variable de comando?
#     print(comando)

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break