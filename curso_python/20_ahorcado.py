'''
El juego comienza mostrando un menú con 3 opciones: cargar palabras, jugar, salir. Es necesario cargar manualmente las palabras a utilizar durante el juego.

Cuando el usuario decide jugar, cuenta con 6 intentos para arriesgar letras. Sólo puede completar la palabra arriesgando letras (no puede arriesgar la palabra completa en cualquier momento).

Si arriesga una letra que ya había arriesgado anteriormente, ese intento no cuenta y se le vuelve a pedir una letra. Cuando el usuario ingresa su opción, si la letra existe en la palabra, se muestra en el lugar correspondiente y se contabiliza como letra ya utilizada. Si la letra no existe en la palabra, se resta un intento, pero también se cuenta a la letra como ya utilizada. Si la letra no existe en la palabra y, además, quedaba un solo intento, el juego termina.

No se distinguen mayúsculas o minúsculas (todas son convertidas a una forma estándar). Se distinguen vocales acentuadas o con diéresis.

El juego termina cuando:

    No quedan más intentos (pierde).
    El usuario acierta todas las letras, una a una (gana).

'''
from random import random
from math import floor

MENU_OPTIONS = ["Cargar palabras", "Jugar", "Salir"]
FILENAME = "words.txt"
MAX_ALLOWED_ERRORS = 5

def show_menu():
    for i in range(len(MENU_OPTIONS)):
        print(f"{i} - {MENU_OPTIONS[i]}")
    option = input("Ingrese una opcion: ")
    return option

def add_words():
    words = []
    while(True):
        word = input("Ingrese una palabra o presione enter sin escribir caracteres para finalizar la carga: ")
        if(len(word) > 0):
            words.append(word + "\n")
        else:
            with open(FILENAME, "a") as file:
                file.writelines(words)
            break

def choose_random_word(list):
    length = len(list)
    rand_index = floor(random() * length)
    return list[rand_index]

def print_actual_status(choosen_word, attempts, choosen_word_letters):
    result = ""
    for letter in choosen_word:
        if(letter in attempts):
            result += letter
        else:
            result += "_"
    if(len(attempts) > 0):
        print(f"Intentos actuales: {attempts}")
        print(f"Errores: {attempts.difference(choosen_word_letters)}")
    print(result)

def play_game():
    with open(FILENAME) as file:
        words = file.readlines()
    choosen_word = choose_random_word(words).lower().strip()
    choosen_word_letters = set()
    for letter in choosen_word:
        choosen_word_letters.add(letter)
    attempts = set()
    while(True):
        print_actual_status(choosen_word, attempts, choosen_word_letters)
        if(len(attempts.difference(choosen_word_letters)) > MAX_ALLOWED_ERRORS):
            print("You lose!")
            return True
        attempt = input("Ingrese una letra: ").lower().strip()
        if(len(attempt) > 1):
            print("Debe ingresar un unico caracter! intente nuevamente.")
        else:
            attempts.add(attempt)
        if(choosen_word_letters.issubset(attempts)):
            print(f"You won! The word was: {choosen_word}")
            return True

while(True):
    option = show_menu()
    if(option == "0"):
        add_words()
    elif(option == "1"):
        isFinished = play_game()
    elif(option == "2"):
        print("Exiting..")
        break
    else:
        print("Ingrese una opcion valida!")