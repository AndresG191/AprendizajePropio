#Crea un programa donde puedas registrar las calificaciones de los alumnos y posteriormente verificarlas

#Para almacenar a los alumnos
alumnos = []

def switch_case(valor):
    opcion = {
        1:"Ingresar Calificacion",
        2:"Visualizar Datos del Alumno",
        3:"Salir del sistema"
    }
    return opcion.get(valor, "Opción no valida")

while True:
    print("Bienvenido al sistema de Maestros, ¿Qué deseas realizar?\n"
            "1.- Ingresar Calificacion y Alumno\n"
            "2.- Visualizar Datos del Alumno\n"
            "3.- Salir del sistema")

    try:
        opcion =int(input("Ingresa la opcion deseada: "))
        result = switch_case(opcion)

    #Imprime el primer resultado
        print(result)

        if opcion <= 1:
            nombre = input("Ingresa el nombre del alumno: ")
            calif = int(input("Ingresa la calificacion del alumno: "))
            alumnos.append({"nombre": nombre, "calificacion": calif})# Agrega el alumno y su calificación a la lista
        elif opcion <=2:
            print("Lista de alumnos registrados: ")
            print("-------------------------------------------------------------")
            for alumno in alumnos:
                if alumno["calificacion"] is not None:
                    print(f"Nombre: {alumno['nombre']}, Calificación: {alumno['calificacion']}")
                else:
                    print(f"Nombre: {alumno['nombre']}, Calificación: No ingresada")
            print("-------------------------------------------------------------")
        elif opcion <=3:
            print("Saliendo del sistema.")
            break
        else:
            print("Has ingresado una opción no válida")

    except ValueError:
        print("Error... Por favor, ingrese un numero válido.")


# NombreAlumno = (input("Ingresa el nombre del Alumno: "))
# Calificacion = int(input("Ingresa la calificacion: "))
# if Calificacion >= 60:
#     print("El alumno",NombreAlumno,"aprobó la materia")
# else:
#     print("El alumno",NombreAlumno,"no acredito la materia")
