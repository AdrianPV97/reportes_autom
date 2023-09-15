from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
import datetime
import locale
import json
from reportlab.pdfgen import canvas

control = "C:/users/adrian/Documents/reportes/GeneradorDeReportes/Recursos/controlVentas.json"

def nuevoArchivo(nombre_archivo):
    doc = SimpleDocTemplate(nombre_archivo, pagesize=letter, topMargin=-7)
    story = []
    ancho_hoja, _ = letter
    ancho_titulo = doc.width
    styles = getSampleStyleSheet()

    #Definimos fecha
    locale.setlocale(locale.LC_TIME, 'es_ES')
    fecha_actual = datetime.datetime.now()
    mes_actual = fecha_actual.strftime('%B')
    meses_anteriores = [(fecha_actual - datetime.timedelta(days=30 * i)).strftime('%B') for i in range(1, 13)]
    
    #Encabezado
    encabezado = Table([
        [''],
    ], colWidths=[620])
    encabezado.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.yellowgreen),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
    ]))
    story.append(encabezado)

    #Logo Emida
    logo_route = "C:/users/adrian/Documents/reportes/GeneradorDeReportes/recursos/img/emida.png"
    story.append(Spacer(1, 20))
    story.append(Image(logo_route, width=ancho_hoja - 420, height=55))
    # Título
    titulo = "A9 - ZC - JORGE DE ZAVALA"
    x_titulo = (ancho_hoja - ancho_titulo) / 2
    story.append(Spacer(1, 20))  # Espacio entre encabezado y título
    story.append(Paragraph(titulo, styles['Title']))

    # Cuerpo del documento
    body_text = [
        "Estimado Cliente:",
        "Por este medio le comparto la siguiente gráfica, la cual muestra sus",
        "ventas del periodo Abril 2022 - Abril 2023"
    ]
    for para in body_text:
        story.append(Paragraph(para, styles['Normal']))

    # Insertar la gráfica
    chart_route = "C:/users/adrian/Documents/reportes/GeneradorDeReportes/graficas/A9 - ZC - JORGE DE ZAVALA.jpg"
    story.append(Spacer(1, 20))  # Espacio entre texto y gráfica
    story.append(Image(chart_route, width=ancho_hoja - 30, height=300))

    #Consultar documento de ventas
    with open(control) as file:
        controlVentas = json.load(file)
    for ventas in controlVentas:
        ventas1= "$" + str(ventas["promedio"]["promedio3"]) 
        ventas2= "$"+ str(ventas["promedio"]["promedio4"])
        ventas3= "$"+ str(ventas["promedio"]["promedio5"])
        ventas4= "$"+ str(ventas["promedio"]["promedio6"])
        ventas5= "$"+ str(ventas["promedio"]["promedio7"])
        ventas6= "$"+ str(ventas["promedio"]["promedio8"])
        ventas7= "$"+ str(ventas["promedio"]["promedio9"])
        ventas8= "$"+ str(ventas["promedio"]["promedio10"])
        ventas9= "$"+ str(ventas["promedio"]["promedio11"])
        ventas10= "$"+ str(ventas["promedio"]["promedio12"])
        ventas11= "$"+ str(ventas["promedio"]["promedio13"])
        ventas12= "$"+ str(ventas["promedio"]["promedio14"] )

        rendimiento1 = round(((ventas["promedio"]["promedio4"] - ventas["promedio"]["promedio3"])/ventas["promedio"]["promedio3"])*100, 2)
        rendimiento2 = round(((ventas["promedio"]["promedio5"] - ventas["promedio"]["promedio4"])/ventas["promedio"]["promedio4"])*100, 2)
        rendimiento3 = round(((ventas["promedio"]["promedio6"] - ventas["promedio"]["promedio5"])/ventas["promedio"]["promedio5"])*100, 2)
        rendimiento4 = round(((ventas["promedio"]["promedio7"] - ventas["promedio"]["promedio6"])/ventas["promedio"]["promedio6"])*100, 2)
        rendimiento5 = round(((ventas["promedio"]["promedio8"] - ventas["promedio"]["promedio7"])/ventas["promedio"]["promedio7"])*100, 2)
        rendimiento6 = round(((ventas["promedio"]["promedio9"] - ventas["promedio"]["promedio8"])/ventas["promedio"]["promedio8"])*100, 2)
        rendimiento7 = round(((ventas["promedio"]["promedio10"] - ventas["promedio"]["promedio9"])/ventas["promedio"]["promedio9"])*100, 2)
        rendimiento8 = round(((ventas["promedio"]["promedio11"] - ventas["promedio"]["promedio10"])/ventas["promedio"]["promedio10"])*100, 2)
        rendimiento9 = round(((ventas["promedio"]["promedio12"] - ventas["promedio"]["promedio11"])/ventas["promedio"]["promedio11"])*100, 2)

    # Insertar la tabla
    datos_tabla = [
        ['',meses_anteriores[0][0:3], meses_anteriores[1][0:3], meses_anteriores[2][0:3], meses_anteriores[3][0:3], meses_anteriores[4][0:3], meses_anteriores[5][0:3], meses_anteriores[6][0:3], meses_anteriores[7][0:3], meses_anteriores[8][0:3], meses_anteriores[9][0:3], meses_anteriores[10][0:3], meses_anteriores[11][0:3]],
        ['Ventas',ventas1, ventas2, ventas3, ventas4, ventas5, ventas6, ventas7, ventas8, ventas9, ventas10, ventas11, ventas12],
        ['Rend',"-","-","-",rendimiento1, rendimiento2, rendimiento3, rendimiento4, rendimiento5, rendimiento6, rendimiento7, rendimiento8, rendimiento9],
    ]
    
    ancho_columnas = [(doc.width+80) / len(datos_fila) for datos_fila in datos_tabla]

    tabla = Table(datos_tabla, ancho_columnas)
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.green),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
    ]))
    story.append(Spacer(1, 20))  # Espacio entre gráfica y tabla
    story.append(tabla)

    doc.build(story)

# Llamar a la función para generar el PDF
nuevoArchivo("test_con_tabla.pdf")








# #PDFGen
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.lib import colors
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# def nuevoArchivo(nombre_archivo):
#     c = canvas.Canvas(nombre_archivo, pagesize=letter)
#     c.setTitle("Archivo de prueba")
#     c.setFillColor("yellowgreen")  
#     c.setStrokeColorRGB(255, 255, 255)
#     c.rect(-1, 773, 615, 20, fill=True)
#     logo_route = "C:/users/adrian/Documents/reportes/GeneradorDeReportes/Recursos/img/emida.png"
#     c.drawImage(logo_route, 410, 710, width=180, height=35)  
#     #Termina encabezado

#     #Titulo
#     ancho_hoja, alto_hoja = letter
#     c.setFillColor("midnightblue")
#     ancho_titulo = c.stringWidth("A9 - ZC - JORGE DE ZAVALA", "Helvetica-Bold", 20)
#     x_titulo = (ancho_hoja - ancho_titulo) / 2
#     c.setFont("Helvetica-Bold", 20)
#     c.drawString(x_titulo, 650, "A9 - ZC - JORGE DE ZAVALA")

#     #Cuarpo del documento
#     c.setFont("Helvetica-Bold", 18)
#     c.drawString(30, 600, "Estimado Cliente:")
#     c.setFont("Helvetica", 15)
#     c.drawString(30, 550, "Por este medio le comparto la siguiente gráfica, la cual muestra sus")
#     c.drawString(30, 520, "ventas del periodo Abril 2022 - Abril 2023")

#     #Insertamos la gráfica
#     chart_route = "C:/users/adrian/Documents/reportes/GeneradorDeReportes/graficas/A9 - ZC - JORGE DE ZAVALA.jpg"
#     c.drawImage(chart_route, 20, 200, width=ancho_hoja-30, height=300)

#     #Insertar tabla
#     datos_tabla = [
#         ['Celda 1', 'Celda 2', 'Celda 3', '...', 'Celda 12'],
#         ['Celda 1', 'Celda 2', 'Celda 3', '...', 'Celda 12'],
#         ['Celda 1', 'Celda 2', 'Celda 3', '...', 'Celda 12'],
#     ]

#     tabla = Table(datos_tabla, colWidths=[doc.widthOf("Celda")]*12)
#     tabla.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, -1), colors.green),
#         ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
#     ]))

#     story.append(Spacer(1, 20))  # Espacio entre gráfica y tabla
#     story.append(tabla)


#     c.save()


# nuevoArchivo("test.pdf")

