word_or_phrase = input("Ingrese una palabra o una frase: ")
list = [carac for carac in word_or_phrase.lower() if carac != " "]
end = False
index = 0
while ((index < len(list)) and (not end)):
    amount = 0
    amount = list.count(list[index])
    end = amount > 1
    index += 1
if amount > 1:
    print(f"La frase o palabra: \"{word_or_phrase}\" no es un Heterograma")
else: 
    print(f"La frase o palabra: \"{word_or_phrase}\" es un Heterograma")