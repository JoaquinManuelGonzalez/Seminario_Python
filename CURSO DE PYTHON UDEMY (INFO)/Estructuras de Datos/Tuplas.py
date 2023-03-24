alumnos = ("joaquin", "ivan",  "feli", "coco", "fran")
edades = (19, 20, 24, 30, 72)
random = ("jose lui", 2, 3.4, 5j, (1, 2, 3, 4), ["holi", "chau"])

print(alumnos)
print(edades)
print(random)
print(random[4][2])
print(random[-1][0])

print(len(random))
print(alumnos.index("coco"))
print(random.count(2))  #Ver que nos devuelve 1 porque no tiene en cuenta el 2 que aparece en la sub tupla

"""
Definicion: Una Tupla es una estructura de datos que nos permite guardar datos
            de tipos heterogeneos y de distintos valores, hasta tambien otras estructuras
            de datos dentro de ellas, una particularidad de ellas es que son INMUTABLES, 
            es decir, el valor de sus elementos no puede ser modificado una vez creada la Tupla
            aunque si esta contiene otra estructura MUTABLE como una lista o un diccionario, el contenido
            de estas estructuras si va a poder ser modificado. su sintaxis es mediante el uso de (). 


Acceso a lo elementos de una Tupla: Esto lo vamos a hacer al igual que las listas, mediante la
                                    indexacion. Tambien se puede usar el Slicing para mostrar un
                                    conjunto de elementos de la Tupla.

Funciones Habituales con las Tuplas:
    
    Funcion "len(variable)": nos da la longitud que tiene nuestra tupla.

    Funcion "variable.index(elemento)": nos devuelve el indice del elemento que buscamos.

    Funcion "variable.count(elemento)": nos devuelve la cantidad de veces que aparece un elemento en nuestra tupla.

    Se puede hacer la funcion extend ya que nos va a crear una nueva Tupla.
"""