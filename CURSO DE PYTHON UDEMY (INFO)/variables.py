num1 = 2  
num2 = 3
print(num1)
print(num2)
num1 = 4
print(num1)
resul = num1 + num2
print(resul)
print(type(num1))
num3 = 2.5
print(type(num3))
resul = resul * num3
print(resul)
num6 = int (input("introduce tu edad: "))
print(type(num6))
print("Mi nombre es Joaquin y tengo " + str(num6) + " años.")
print(type(num6))


"""
todos los nombres de las variables solo pueden empezar 
con letras alfanumericas (minus, mayus, num) o un "_"

Funcion type(): nos permite saber el tipo de la variable con la que
estamos trabajando.

TIPOS DE DATOS:
    Enteros (int): num = 2
                   num2 = -30

    Decimales (float): num3 = 2.34
                       num4 = -12.6

    Complejos (complex): num5 = 1 + 3j

    Strings (str): texto = "Hola Mundo"

    Booleans (bool): verdadero = True
                     falso = False

Se puede pedir ingresar valores por teclado usando la funcion Input de la siguiente forma:
nombreDeLaVariable = input("Texto descriptivo para que el usuario ingrese un valor")
A la hora de usar esta funcion, las variables se guardan con un tipo "str"
Si se quiere guardar un numero leido por teclado se debe especificar el tipo del variable
de la siguiente forma: num = int(input("ingrese un numero"))

utilizando la funcion str(variable) vamos a poder convertir cualquier variable a un
string, esto nos puede servir a la hora de concatenar strings con valores de variables que
nos de este tipo por ejm. print("hola mi nombre es " + nombre + "y tengo " + str(edad))

"""