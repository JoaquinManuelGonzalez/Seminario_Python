import json
import csv
from random import randrange
import clases


def obtengoDatos():
    """La funcion elige un numero aleatorio en un rango de 0 a 1 e intenta 
    extraer informacion de una banda almacenada en un archivo ya sea json
    o csv dependiendo de la opcion dada en el randrange. 

    Returns:
        <class "dict">: Diccionario con la informacion de la banda extraida.
    """


    opcion = randrange(2)
    try:
        if opcion == 0:
            archi = open("datos.json", "r")
            datos = json.load(archi)
            archi.close()
        elif opcion == 1:
            archi = open("datos.csv", "r")
            csvreader = csv.reader(archi, delimiter=",")
            linea1 = next(csvreader)
            linea2 = next(csvreader)
            datos = dict(zip(linea1, linea2))
            archi.close()
        else:
            datos = {}
        return datos
    except FileNotFoundError:
        raise (FileNotFoundError)


try:
    datos = obtengoDatos()
    banda = clases.Banda(datos["nombre"], datos["genero"])
    print(banda)
    print("FIN DEL PROGRAMA")
except FileNotFoundError:
    print("El Archivo no existe.")
