phrase = input("Ingrese una frase que le guste: ")
word = input("Ingrese la palabra de la que quiera saber la cantidad de ocurrencias: ")
phrase_lower = phrase.lower()
if word.lower() in phrase_lower.split():
    print(f"La palabra \"{word}\" apararece {phrase_lower.count(word.lower())} veces en la frase")
else:
    print(f"La palabra \"{word}\" no aparece en la frase indicada")
