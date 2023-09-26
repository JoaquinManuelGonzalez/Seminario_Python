
import csv

archivo_log = "log_completo.csv" 

def mi_funcion(datos, *args):

    mis_datos = filter(lambda x: x[1] in args and x[6] == "web", datos)
                    
    dicci = {}               
    for elem in mis_datos:
        if elem[1] in dicci.keys():
            dicci[elem[1]] = min(dicci[elem[1]], float(elem[8]))
        else:
            dicci[elem[1]] = float(elem[8])
    return dicci


with open(archivo_log, encoding='utf-8') as data_set:
    reader = csv.reader(data_set, delimiter=',')
    encabezado_log, datos_log = next(reader), list(reader)
    
resultado = mi_funcion(datos_log, "Hypno", "Butterfree", "Rhyhorn", "Slowpoke")
print(resultado)

