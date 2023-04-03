texto = """
 El salario promedio de un hombre en Argentina es de $60.000, mientras que el de una mujer es de $45.000. Además, las mujeres tienen menos posibilidades de acceder a puestos de liderazgo en las empresas.
  """
mayusculas = sum(1 for carac in texto if carac.isupper())
minusculas = sum(1 for carac in texto if carac.islower())
no_letra = sum(1 for carac in texto if (carac.isnumeric() or (carac == "$" or carac == "," or carac == ".")))
print (f"La cantidad de letras mayusculas que tiene el texto es de: {mayusculas}")
print(f"La cantidad de letras minusculas que tiene el texto es de: {minusculas}")
print(f"La cantidad de caracteres que no son mayusculas ni minusculas es de: {no_letra}")
list = texto.split(" ")
list.remove("\n")
for num in range(2):
    list.remove("")
print(sum(1 for palabra in list if not palabra.startswith("$")))