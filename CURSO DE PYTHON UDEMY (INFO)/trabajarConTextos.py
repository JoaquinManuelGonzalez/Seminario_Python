texto = "hola Mundo señores y señoras"
        #0123456789...
print(texto)
print(texto[3])
print(texto[-4])
print(texto[0:4])
print(texto[-7:])
print(texto[:10])
print(texto[0:10:2])    #Imprimir texto desde la posicion 0 a la 9 de 2 en 2
print(texto[::-1])      #Imprimir texto al reves
print(len(texto))
print(texto.capitalize())
print(texto.replace("Mundo", "lindos"))
print(texto.index("e"))
print(texto.islower())
print(texto.isupper())
print(texto.count("o"))

"""
Acceso a elementos de un string mediante la Indexacion y el Rebanado

    Indexacion: Nos permite acceder a un elemento que compone a nuestra
                variable, esto se puede hacer haciendo un 
                print(vriable[posicionQueQueremosAcceder]), las posiciones 
                empiezan desde el 0 hasta n, y si se quiere acceder a un elemento
                de derecha a izquierda se empieza desde el -1 hasta n.

    Rebanado: Nos sirve para acceder a mas de un elemento a la vez de nuestro
              string, esto lo hacemos con un print(variable[rangoDeElementos])
              el numero mayor de nuestro rango de numeros no se va tomar, por lo
              tanto serian [j:k-1], si al rango se le agrega otros dos puntos
              podemos determinar cada cuanto tomar un elemento (PASO), ejemplo [0:20:2]
              asi tomaria cada 2 elementos, si el Paso es negativo vamos de derecha a 
              izquierda.

Funciones habituales con Strings:

    Funcion "len()": Esta funcion nos devuelve la cantidad de elementos que tiene nuestro
                   string (len(variable))

    Funcion "capitalize()": Pone en mayuscula la primera letra de nuestro string, la podemos
                          utilizar en un print(variable.capitalize())

    Funcion "replace()": Nos sirve para poder reemplazar palabras de nuestro string por otras
                       que querramos, podemos usarlo con un 
                       print(variable.replace("palabraAReemplazar", "palabraReemplazo"))

    Funcion "index()": Nos sirve para buscar ua palabra o letra dentro de nuestra variable de
                     texto, esta, nos devuelve la posicion donde se encuentra la letra o palabra
                     se puede usar en un print(variable.index("letraOPalabraABuscar"))

    Funcion "lower()": Nos sirve para poner todo nuestro texto en minusculas, se puede usar en un
                     print(variable.lower())

    Funcion "upper()": Nos sirve para poner todo nuestro texto en mayusculas, se puede usar en un
                     print(variable.upper())

    Funcion "count()": Nos sirve para contalizar la cantidad de veces que aparece un elemento en una cadena de texto

Funciones que devuelven valores Booleanos:
    
    Estas funciones siempre van a empezar de la siguiente manera, variable.is...

    Funcion "islower()": Esta funcion devuelve True si todo el texto esta en minusculas, sino, devuelve False

    Funcion "isupper()": Esta funcion evuelve True si todo el texto esta en mayusculas, sino devuelve False

    Funcion "isalnum()": Esta funcion devuelve True si todos los caracteres del texto son alfanumericos y False
                         en caso contrario

    Funcion "isalpha()": Esta funcion devuelve True si todos los elementos del texto son alfabeticos y False en caso
                         contrario

    Funcion "isdecimal()": Devulve True si todos los elementos del texto son numeros decimales y False en caso contrario

    Funcion "isdigit()": Devuelve True si todos los elementos del texto son digitos


"""