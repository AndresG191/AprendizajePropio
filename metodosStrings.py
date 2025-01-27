animal = "  cerdo maullador"
print(animal.upper()) #El "UPPER lo hace mayuscula"
            #lower lo hace en minuscula
print(animal.strip().capitalize())#toma el primer caracter del string y lo hace mayuscula
print(animal.title()) #toma las primeras letras donde haya espacio y las hace mayusculas
print(animal.strip())#remueve los espacios que hayan a la izquierda y derecha de nuestro string
print(animal.lstrip())
print(animal.rstrip())
print(animal.find("c"))#Buscara cadena de caracteres y nos regresará el índice
print(animal.replace("cerdo","gato"))#el replace debe de recibir dos argumentos
print("cerdo" in animal)#la diferencia es que find devuelve el indice de donde se encuentra la cadena de caracteres
#"in" devuelve boolean si es que se encuentra o no (SOLO PARA SABER SI UN CARACTER SE ENCUENTRA EN UNA VARIABLE")
print("cerdo" not in animal)#podemos preguntar si no se encuentra