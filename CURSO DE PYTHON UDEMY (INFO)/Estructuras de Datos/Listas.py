edades = [18, 20, 5, 68]  #Esta es una LISTA de numeros enteros
nombres = ["Juan", "Joaquin", "Pepe", "Juan"]  #Esta es una LISTA de strings
        #     0        1        -1
print(nombres)
print(edades)
aprobado = [True, False, False]  #Esta es una LISTA de booleans
lista = ["Joaquin", 18, True, 2.8, 1j]  #Esta es una lista con varios tipos de datos distintos

print(lista)
print(nombres[1])
print(nombres[-3])
print(lista[1])
print(edades[1:])
print(nombres[0:2])
print(lista[::-1])

nombres.append("Jose Luis")
print(nombres)
edades.insert(1, 11)
print(edades)
nombres.remove("Juan")
print(nombres)
aprobado.clear()
print(aprobado)
print("Juancho" in nombres)


"""
Listas: 
    Pueden ser declaradas de la siguiente forma
    nombreDeLaLista = [elementos]. Podemos mostrar los
    elementos de una Lista con tan solo hacer un print de 
    la variable Lista. Son Mutadas, es decir, se pueden añadir, modificar
    o eliminar elementos de las mismas.

Acceder a un Elemento independiente de una lista:
    Para acceder a un elemento podemos hacerlo mediante la indexacion
    variable[posicionDelElemento] igual que como se hace con los strings

Modificacion de los elementos de una Lista:

    Añadir ELemento:
        Funcion "append()": mediante la sentencia variable.append(elementoAAgregar)
                           podemos agregar elementos a una lista, de esta forma el 
                           elemento se agrega al final de la Lista.

    Insertar Elemento: 
        Funcion "insert()": mediante la sentencia variable.insert(posicionDondeSeInsertara, elementoAInsertar)
                            podremos insertar un elemento en nuestra lista en la posicion que nosotros querramos.
                            Esta funcion realiza los corrimientos necesarios para poder insertar al elemento deseado
                            en la posicion deseada. Los corrimientos son hacia la derecha.

    Eliminar un Elemento:
        Funcion "remove()": mediante la sentencia variable.remove(elementoAEliminar), se ejecutara esta funcion que busca
                            el elemento especificado y lo elimina de la misma. No elimina todas las ocurrencias del elemento
                            asi que si el elemento aparece mas de una vez en la lista, solo eliminara la primer ocurrencia del
                            mismo
        
        Funcion "clear()": mediante la sentencia variable.clear() podremos eliminar todos los elementos de una lista
    
    Busqueda de un Elemento dentro de una lista: Estas funciones sirven para saber si un elemento esta o no en la Lista

        Funcion "print(elemento in variable)": mediante esa sentencia el Print nos devolvera en pantalla True si el elemento esta
                                               en la Lista o False en caso contrario
        
        

"""