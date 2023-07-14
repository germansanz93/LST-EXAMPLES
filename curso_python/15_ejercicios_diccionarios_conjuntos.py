
# Escribe un programa en python para encontrar todas las palabras unicas que aparecen
# en un texto y contar la frecuencia de ocurrencia.
# Consejo: utilizar metodo split

text = input("Ingrese un texto: ").lower()

word_list = text.split()

word_set = set(word_list)

word_dict = dict()

for word in word_set:
    word_dict[word] = word_list.count(word)

for word, count in word_dict.items():
    print(f"La palabra {word} aparece {count} veces")

# Cree un programa que encuentre todas las sumas posibles en un listado de numeros

nums = []

sum_set = set()

while(True):
    user_input = input("Ingrese un entero o x para salir: ")
    if(user_input == "x"):
        break
    else:
        nums.append(int(user_input))

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        sum_set.add(nums[i] + nums[j])

print(sum_set)

# Cree un programa que dado un texto encuentre que cantidad de vocales y 
# de consonantes posee. Podria crear un dict que contenga las vocales y las compare. 
# otro para los signos de puntuacion y el espacio y si no esta en ninguno de esos 
# conjuntos, entonces es vocal. Crear un dict que contenga las claves vocales, 
# simbolos y consonantes.

vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
signs = {" ": 0, ".": 0, ",": 0}
consonants = dict()

text = input("Ingrese un texto: ").lower()

for letter in text:
    if(letter in vowels.keys()):
        vowels[letter] += 1
    elif(letter in signs.keys()):
        signs[letter] += 1
    else:
        if(letter in consonants.keys()):
            consonants[letter] += 1
        else:
            consonants[letter] = 0

print(vowels)
print(signs)
print(consonants)