# buscar = 11
# for numero in range(5):     #Existen las Iterables / Listas / Tuplas
#     print(numero)           #para buscar identificadores o algo asi, lo que sea
#     if numero == buscar:
#         print("Encontrado", buscar)
#         break
# else:
#     print("No se encontró el numero buscado")
#
# for char in "Ultimate piton":
#     print(char) #Se imprime cada uno de los caracteres de lo que pusimos

#FOR
frutas = ["Manzanas", "Peras", "Platanos"]
print(frutas)

#WHILE
#Bloque de condicion a repetir
#Instrucciones

contador = 0
while contador < 6:
    print(contador)
    contador += 1
print("------------------------------------")
contador = 0
while True:
    print(contador)
    contador +=1

    if contador ==5:
        break

#La instruccion "continue" se utiliza para saltar el resto del
#bloque de codigo dentro de un bucle y pasar la sig iteración.

for i in range(10):
    if i % 2 ==0:
        continue
    print(i)

for i in range(5):
    pass
#El pass no sirve de nada más que guardar un bloque de memoria para el futuro