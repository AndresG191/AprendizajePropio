#Importar modulos
#Para utilizar un modulo en nuestro programa, debemos importarlo utilizando la declaracion import.

import math
resultado = math.sqrt(25)
print(resultado)    #imprime 5.0
#Se importa el modulo math con "import" luego se utiliza la funcion sqrt() del modulo math
#para calcular la raíz cuadrada de 25.

#Tambien podemos importar funciones especificas de un modulo utilizando la sintaxis "from" modulo "import" funcion.

from math import sqrt
resultado = sqrt(25)
print(resultado)    #imprimte 5.0

#Funciones y clases de modulos estandar
#Ejemplos más comúnes de bibliotecas son:

#Math: Proporciona funciones matematicas, como sqrt() (raíz cuadrada), sin() (seno), cos() (coseno) etc.
#Random: Ofrece funciones para generar números aleatorios, como random() (numero aleatorio entre 0 y 1)
#randint() (numero entre aleatorio en un rango) etc
#Datetime: Permite trabajar con fechas y horas, como datetime.now() (fecha y hora actual), datetime.date()
#(fecha), datetime.time() (hora) etc.

import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio) #imprime un numero entero aleatorio entre 1 y 10

fecha_actual = datetime.datetime.now()
print(fecha_actual) #Imprime la fecha y hora actual.

#Para saber más, acudir a la documentacion de Python sobre los modulos y sus funcionalidades