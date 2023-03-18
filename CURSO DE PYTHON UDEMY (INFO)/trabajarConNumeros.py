from math import * #Importamos toda la libreria math

num1 = int(input("Introduzca un numero entero: "))
num2 = float(input("Introduzca un numero decimal: "))
resul = int(num1 + num2)
print(resul)
print(int(num1 + num2))
print (num1**2)
print (num1**num2)
print (num2//num1)
num1 += num1
num2 += 3
print(num1, num2)
num3 = 2
print(abs(num3))
print(pow(num3, 4))
print(max(num1, num2, num3, 16, 10))
print(min(num1, num2, num3, 16, 10))
print(round(4.3))
print(floor(num2))
print(ceil(num2))
print(sqrt(num1))

"""
Operaciones Aritmeticas:

    Suma "+": Suma de variables, si las variables son de distintos tipos numericos podemos 
              especificar en cual de ellos queremos almacenar el resultado
    
    Resta "-": Resta de variables, si las variables son de distintos tipos numericos podemos 
              especificar en cual de ellos queremos almacenar el resultado

    Multiplicacion "*": Multiplicacion de variables, si las variables son de distintos tipos numericos podemos 
                        especificar en cual de ellos queremos almacenar el resultado

    Division "/": Division de variables, si las variables son de distintos tipos numericos podemos 
              especificar en cual de ellos queremos almacenar el resultado

    Exponente "**" Elevar una variable a una potencia, si las variables son de distintos tipos numericos podemos 
              especificar en cual de ellos queremos almacenar el resultado

    Division de Enteros o Hacer DIV "//": Guarda solo la parte entera de una division

    Hacer MOD "%": Nos da el resto de la division

Operadores de Asignacion: Son los que nos permiten asignar valores a una variable 

    Operador "=": Nos sirve para darle un valor cualquiera a una variable, ya sea un valor especifico
                  o una operacion entre variables

    Operador de Asignacion de Suma "+=": Sirve para asignarle a una variable un valor que conlleve una suma de valores
    
    Operador de Asignacion de Resta "-=": Sirve para asignarle a una variable un valor que conlleve una resta de valores

    Operador de Asignacion de Multiplicacion "*=": Sirve para asignarle a una variable un valor que conlleve una multiplicacion de valores

    Operador de Asignacion de Division "/=": Sirve para asignarle a una variable un valor que conlleve una division de valores

    Operador de Asignacion de Exponente "**=": Sirve para asignarle a una variable un valor que conlleve una potencia de valores

    Operador de Asignacion DIV "//=": Sirve para asignarle a una variable un valor que conlleve una division de enteros de valores

    Operador de Asignacion MOD "%=": Sirve para asignarle a una variable un valor que conlleve el resto de una division de valores

Funciones Habituales con Numeros:

    Funcion "abs(variable)": Devuelve el valor absoluto del numero

    Funcion "pow(variable, valor)": Devuelve la potencia de la variable elegida elevada al valor especificado

    Funcion "max(variable, variable, ...)": Devuelve el valor maximo entre las variables especificadas

    Funcion "min(variable, variable, ...)": Devuelve el valor minimo entre las variables especificadas

    Funcion "round(valor)": Redondea el valor o la variable al entero mas cercano

Funciones que necesitan la libreria math:

    Funcion "floor(valor)": Redondea el valor o variable al Entero cercano mas bajo

    Funcion "ceil(valor)": Redondea el valor o variable al Entero cercano mas alto

    Funcion "sqrt(valor)": Realiza la raiz cuadrada del valor o variable indicada
"""