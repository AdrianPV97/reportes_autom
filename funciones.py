import os
import json
import procesoCompleto

#Creamos los iniciadores del menu
def cargarArchivo():
    os.chdir("Documentos")
    listaDeArchivos = os.listdir()
    if len(listaDeArchivos) > 1:
        print("Revise el directorío, hay mas de un archivo en cola")
    else:
        base = 'C:/users/adrian/Documents/reportes/GeneradorDeReportes/Documentos/'+ listaDeArchivos[0]
        diccionario = "C:/users/adrian/Documents/reportes/GeneradorDeReportes/Recursos/diccionario.json"
        controlVentas = "C:/users/adrian/Documents/reportes/GeneradorDeReportes/Recursos/controlVentas.json"
        
        respuesta = procesoCompleto.leerClientes(base, diccionario)
        #print(respuesta)
        with open(controlVentas, 'w') as file:
            json.dump(respuesta, file, indent=4)
        procesoCompleto.generarGraficas(controlVentas)
        #print("Ok!")
        #archivoDatos = json.load(open('base_ventas.json', encoding="utf-8"))
        #pd.set_option('display.max_rows', 30000)
        #df_ventas = pd.read_excel('churn.xlsx')
        #print("Se cargara el archivo: " + listaDeArchivos[0])


cargarArchivo()

