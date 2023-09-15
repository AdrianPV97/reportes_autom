#Matplot y pandas
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
#Json controller
import json
#Fechas
from datetime import datetime
import requests
#import json


def calcularPromedio(comercio):
    promedio = {
        "promedio1":round((comercio["mes_1"] / int(comercio["Clientes por mes"]["mes1"])),2),
        "promedio2":round((comercio["mes_2"] / int(comercio["Clientes por mes"]["mes2"])),2),
        "promedio3":round((comercio["mes_3"] / int(comercio["Clientes por mes"]["mes3"])),2),
        "promedio4":round((comercio["mes_4"] / int(comercio["Clientes por mes"]["mes4"])),2),
        "promedio5":round((comercio["mes_5"] / int(comercio["Clientes por mes"]["mes5"])),2),
        "promedio6":round((comercio["mes_6"] / int(comercio["Clientes por mes"]["mes6"])),2),
        "promedio7":round((comercio["mes_7"] / int(comercio["Clientes por mes"]["mes7"])),2),
        "promedio8":round((comercio["mes_8"] / int(comercio["Clientes por mes"]["mes8"])),2),
        "promedio9":round((comercio["mes_9"] / int(comercio["Clientes por mes"]["mes9"])),2),
        "promedio10":round((comercio["mes_10"] / int(comercio["Clientes por mes"]["mes10"])),2),
        "promedio11":round((comercio["mes_11"] / int(comercio["Clientes por mes"]["mes11"])),2),
        "promedio12":round((comercio["mes_12"] / int(comercio["Clientes por mes"]["mes12"])),2),
        "promedio13":round((comercio["mes_13"] / int(comercio["Clientes por mes"]["mes13"])),2),
        "promedio14":round((comercio["mes_14"] / int(comercio["Clientes por mes"]["mes14"])),2)
    }
    return promedio


def calcularClientesXMes(filtro):
    calculoTotal = {
        "mes1":str((filtro["mes_1"] != 0).sum()), 
        "mes2":str((filtro["mes_2"] != 0).sum()),
        "mes3":str((filtro["mes_3"] != 0).sum()),
        "mes4":str((filtro["mes_4"] != 0).sum()),
        "mes5":str((filtro["mes_5"] != 0).sum()),
        "mes6":str((filtro["mes_6"] != 0).sum()),
        "mes7":str((filtro["mes_7"] != 0).sum()),
        "mes8":str((filtro["mes_8"] != 0).sum()),
        "mes9":str((filtro["mes_9"] != 0).sum()),
        "mes10":str((filtro["mes_10"] != 0).sum()),
        "mes11":str((filtro["mes_11"] != 0).sum()),
        "mes12":str((filtro["mes_12"] != 0).sum()),
        "mes13":str((filtro["mes_13"] != 0).sum()),
        "mes14":str((filtro["mes_14"] != 0).sum()),
        }
    return calculoTotal


def leerClientes(base, diccionario):
    #documento = pd.read_excel('churn.xlsx')
    documento = pd.read_excel(base)
    diccionario = json.load(open(diccionario, encoding="utf-8"))
    clientes= []
    filtros=[]
    for cliente in diccionario["clientes"]:
        comercio = {}
        match cliente["tipo"]:
            case "ISO":
                if cliente["ps"] == "True":
                    filtro = documento[(documento['Iso'] == cliente['clave']) | (documento['Iso'] == 'PS -' + cliente['clave'])]
                else:
                    filtro = documento[documento['Iso'] == cliente["clave"]]
            case "REP":
                if cliente["ps"] == "True":
                    filtro = documento[(documento['Rep'] == cliente['clave']) | (documento['Rep'] == 'PS -' + cliente['clave'])]
                else:
                    filtro = documento[documento['Rep'] == cliente["clave"]]
            case "AGENTE":
                if cliente["ps"] == "True":
                    filtro = documento[(documento['Agente'] == cliente['clave']) | (documento['Agente'] == 'PS -' + cliente['clave'])]
                else:
                    filtro = documento[documento['Agente'] == cliente["clave"]]
            case "SUBAGENTE":
                if cliente["ps"] == "True":
                    filtro = documento[(documento['SubAgente'] == cliente['clave']) | (documento['SubAgente'] == 'PS -' + cliente['clave'])]
                else:
                    filtro = documento[documento['SubAgente'] == cliente["clave"]]
        
        #Calculamos promedios     
        

        comercio["nombre"]= cliente["nombre"]
        comercio["mes_1"] = int(filtro['mes_1'].sum()+0)
        comercio["mes_2"] = int(filtro['mes_2'].sum()+0)
        comercio["mes_3"] = int(filtro['mes_3'].sum()+0)
        comercio["mes_4"] = int(filtro['mes_4'].sum()+0)
        comercio["mes_5"] = int(filtro['mes_5'].sum()+0)
        comercio["mes_6"] = int(filtro['mes_6'].sum()+0)
        comercio["mes_7"] = int(filtro['mes_7'].sum()+0)
        comercio["mes_8"] = int(filtro['mes_8'].sum()+0)
        comercio["mes_9"] = int(filtro['mes_9'].sum()+0)
        comercio["mes_10"] = int(filtro['mes_10'].sum()+0)
        comercio["mes_11"] = int(filtro['mes_11'].sum()+0)
        comercio["mes_12"] = int(filtro['mes_12'].sum()+0)
        comercio["mes_13"] = int(filtro['mes_13'].sum()+0)
        comercio["mes_14"] = int(filtro['mes_14'].sum()+0)
        comercio["Clientes por mes"] = calcularClientesXMes(filtro)
        comercio["promedio"] = calcularPromedio(comercio)
        clientes.append(comercio)


    return clientes





def generarGraficas(control):
    #Declaramos las variables que nos ayudaran a obtener los meses que se debe incluir en el reporte
    date = datetime.now()
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    mes_actual = date.month-1
    x = [meses[mes_actual - 12], meses[mes_actual - 11], meses[mes_actual - 10], meses[mes_actual - 9], meses[mes_actual - 8], meses[mes_actual - 7], meses[mes_actual - 6], meses[mes_actual - 5], meses[mes_actual - 4], meses[mes_actual - 3], meses[mes_actual - 2], meses[mes_actual - 1]]
    #Iteramos el control de clientes, ya teniendo el número total de ventas mensuales
    with open(control) as file:
        controlVentas = json.load(file)
    for cliente in controlVentas:
        comercio = cliente['nombre']
        mes1 = cliente["promedio"]["promedio3"]
        mes2 = cliente["promedio"]["promedio4"]
        mes3 = cliente["promedio"]["promedio5"]
        mes4 = cliente["promedio"]["promedio6"]
        mes5 = cliente["promedio"]["promedio7"]
        mes6 = cliente["promedio"]["promedio8"]
        mes7 = cliente["promedio"]["promedio9"]
        mes8 = cliente["promedio"]["promedio10"]
        mes9 = cliente["promedio"]["promedio11"]
        mes10 = cliente["promedio"]["promedio12"]
        mes11 = cliente["promedio"]["promedio13"]
        mes12 = cliente["promedio"]["promedio14"]
        ventas = [mes1, mes2, mes3, mes4, mes5, mes6, mes7, mes8, mes9, mes10, mes11, mes12]
        plt.figure(figsize=(15,6))
        for i in range(len(x)):
            plt.text(x[i],ventas[i], "$" + str(ventas[i]) + "MXN")
        plt.plot(x,ventas, marker='o')
        plt.yticks(rotation=0)
        plt.ticklabel_format(style='plain', axis='y')
        plt.title("Ventas " + comercio + " " + meses[mes_actual -1])
        plt.savefig('C:/users/adrian/Documents/reportes/GeneradorDeReportes/graficas/' + comercio + ".jpg")
        plt.clf()
        #new.rend(ventas, usuario)

