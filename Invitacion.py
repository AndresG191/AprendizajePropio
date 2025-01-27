from fpdf import FPDF


def crear_invitacion(nombre_novios, fecha, lugar):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)

    pdf.cell(190, 10, f"Invitacion de boda", 0, 1, 'C')

    pdf.set_font('Arial', '', 12)
    pdf.ln(10)#añade salto de linea

    #Contenido
    mensaje = (f'Queridos amigos y familiares HOY ME CASO!!!!!!!! ,\n\n'
        f'Nos complace invitarlos a la boda {nombre_novios}. \n'
        f'La ceremonia se llevará a cabo el {fecha} \n'
        f'en {lugar}.\n\n'
        f'NO VAYAN A FALTAR IJUESUSHINGAMARE\n\n'
        f'Con cariño,\n'
        f'{nombre_novios}')
    pdf.multi_cell(0, 10, mensaje)

    #Guardar pdf

    pdf.output("Invitacion_boda_Lesly.pdf")
    print("¡Invitacion creada!")

#Uso de la funcion "crear_invitacion"

crear_invitacion("Lesly Pereira y el misterioso enmascarado","el 26 de Enero del 2025", "en el hotel Maeva Playa Miramar")