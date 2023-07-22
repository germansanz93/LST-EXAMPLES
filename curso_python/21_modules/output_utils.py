def show_menu(MENU_OPTIONS):
    for i in range(len(MENU_OPTIONS)):
        print(f"{i} - {MENU_OPTIONS[i]}")
    option = input("Ingrese una opcion: ")
    return option

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