sentences = ["Hola, mundo!\n", "Este texto esta almacenado en una lista.\n", "Cada elemento es una oracion.\n"]

with open("writing.txt", "w") as file:
    file.writelines(sentences)
