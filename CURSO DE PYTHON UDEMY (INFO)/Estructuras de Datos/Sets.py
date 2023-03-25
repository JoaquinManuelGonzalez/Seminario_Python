nombres = {"joaquin", "facu", "mile", "roxana", "oscar"}
edades = {19, 24, 30, 52, 55}
set_completo = {2.3, "holi", ("chau", 1234,), "casita", "auto", -12345}

print(nombres)
print(set_completo)
print(len(edades))
nombres.add("cacho")
print(nombres)
nombres.update(edades)
print(nombres)
nombres.remove("cacho")
print(nombres)
nombres.discard("juan carlos")

"""
Definicion: un set es una estructura de datos INMUTABLE que
            permite guardar un conjunto de valores distintos y de tipos
            distintos como una lista o una tupla, otra cuestion es que
            en un set no puede haber elementos repetidos, en un set no
            se puede tener un criterio de orden y no se puede acceder a un elemento
            especifico mediante la indexcion.

Funciones:

    funcion "variable.add(elemento)": añade un elemento a nuestro set

    funcion "len(variable)": esta funcion nos devuelve la cantidad de elementos que
                             tiene nuestro set
    
    funcion "variable.update(variable)": funciona como un extend, añade los elementos del set
                                         que se encuentra de argumento al set que invoca al metodo

    funcion "variable.remove(elemento)": elimina un elemento del set

    funcion "variable.discard(elemento)": otra forma de eliminar un elemento, utilizando discard es mas 
                                          eficiente ya que si el elemento que se quiere eliminar no existe
                                          en el set, no nos dara un error como pasaria con la funcion remove
    
    funcion "variable.pop()": elimina un elemento de manera random y devuelve el set
"""