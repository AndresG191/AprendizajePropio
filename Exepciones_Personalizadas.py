#Excepcion personalizada
def funcion():
    #Codigo que puede generar una excepcion personalizada
    if condicion:
        raise Exception("Descripcion del error")

try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")