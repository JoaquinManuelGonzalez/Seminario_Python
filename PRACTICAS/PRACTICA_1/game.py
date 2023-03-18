from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
#print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
cant_C = 0
cant_I = 0
for i in range(0, times):
# Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    # Se imprime la cuenta.
    while (operator == operators[-1]) and (number_2 == 0):
        number_1 = randrange(10)
        number_2 = randrange(10)
        operator = choice(operators)
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = float(input("resultado: "))
    match operator:
        case("+"):
            aux = number_1 + number_2
        case("-"):
            aux = number_1 - number_2
        case("*"):
            aux = number_1 * number_2
        case("/"):
            aux = number_1 / number_2
    if result == aux:
        print("Correcto")
        cant_C += 1
    else:
        print("Incorrecto")
        cant_I += 1
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"\n Cantidad de Operaciones Correctas: {cant_C} y la Cantidad de Operaciones Incorrectas es de: {cant_I}")