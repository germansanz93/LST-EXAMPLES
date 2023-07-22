from output_utils import show_menu, print_actual_status
from list_utils import choose_random_element

MENU_OPTIONS = ["Cargar palabras", "Jugar", "Salir"]
FILENAME = "words.txt"
MAX_ALLOWED_ERRORS = 5

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

def play_game():
    with open(FILENAME) as file:
        words = file.readlines()
    choosen_word = choose_random_element(words).lower().strip()
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
    option = show_menu(MENU_OPTIONS)
    if(option == "0"):
        add_words()
    elif(option == "1"):
        isFinished = play_game()
    elif(option == "2"):
        print("Exiting..")
        break
    else:
        print("Ingrese una opcion valida!")