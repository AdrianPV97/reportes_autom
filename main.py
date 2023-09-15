##Definimos las librerias
#from matplotlib import markers
from datetime import datetime
import os
import funciones
#import matplotlib.pyplot as plt
import json
#import calculo
#import new


##Funcion del menu
def menu(opcion):
    if type(opcion) == int and opcion <= 6:
        match opcion:
            case 1:
                print("Cargando archivo...")
            case 2:
                print("Regenrando gráficas...")
            case 3:
                print("Regenerando reportes...")
            case 4:
                print("Editar unitariamente")
            case 5:
                print("Agrega el cliente")
            case 6:
                print("Elimina el cliente")
    else:
        print("Introduce un valor válido")



def main():
    print('Bienvenid@ al generador de repoetes, elige una opcion:')
    ##Generamos un menu
    print("1.- Cargar archivo")
    print("2.- Regenerar gráficas")
    print("3.- Regenerar documentos")
    print("4.- Edicion unitaria")
    print("5.- Agregar cliente")
    print("6.- Eliminar cliente")

    respuesta = int(input())
    os.system('cls')
    menu(respuesta)

main() 
