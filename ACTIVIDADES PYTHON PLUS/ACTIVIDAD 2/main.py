import json, csv
from random import randrange
import  clases 

def obtengoDatos():
    opcion = randrange(2)
    if opcion == 0:
        archi = open("datos.json", "r")
        Datos=json.load(archi)
        archi.close()
    elif opcion == 1:
        archi = open("datos.csv", "r")
        csvreader = csv.reader(archi, delimiter=',')
        linea1 = next(csvreader)
        linea2 = next(csvreader)
        Datos = dict(zip(linea1, linea2))
        archi.close()
    else:
        Datos = {}
    return Datos

Datos = obtengoDatos()

banda = clases.Banda(Datos['nombre'], Datos["genero"])

print(banda)
print("FIN DEL PROGRAMA")