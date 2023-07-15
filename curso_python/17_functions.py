def nombre(parametro_1, parametro_2, parametro_3):
    suma = parametro_1 + parametro_2
    prod = suma * parametro_3
    return prod

argumento_1 = 2
argumento_2 = 5
argumento_3 = 7

resultado = nombre(argumento_1, argumento_2, argumento_3)
print(resultado)

def saludar():
    print("*"*50)
    print("Hola")
    print("*"*50)

saludar()
saludar()
saludar()
