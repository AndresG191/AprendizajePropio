# and, or, not
# and cuando tengamos dos condiciones
# or si uno es true el resultado de una operacion bastara para que sea true ignorando el segundo caso
# not niega el resultado de una operacion

gas = False
encendido = True
edad = 18

if not gas and (encendido and edad > 17):   #And ambos valores tienen que ser true para que entre a la condicion
    print("Puedes avanzar")