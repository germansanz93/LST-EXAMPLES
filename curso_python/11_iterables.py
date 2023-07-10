pets_list = ["Perro", "Gato", "Loro", 3, True, "Caiman"] #Lista

#Queremos recorrer toda la lista e imprimir sus elementos uno a uno

# for i in range(5):
#     print(pets_list[i])

#Queremos recorrer toda la lista e imprimir sus elementos uno a uno, pero indicando cuando
#un valor no es string

# for i in range(5):
#     if(type(pets_list[i]) == str):
#         print(pets_list[i])
#     else:
#         print(f"El valor en la posicion {i} no es un tipo de mascota")

#Queremos recorrer toda la lista e imprimir sus elementos uno a uno, pero indicando cuando
#un valor no es string, ademas quiero que si el tipo es perro, se imprima  "El mejor amigo del hombre"

# for i in range(6):
#     if(type(pets_list[i]) == str):
#         print(pets_list[i])
#         if(pets_list[i].lower() == "perro"):
#             print("El mejor amigo del hombre")
#     else:
#         print(f"El valor en la posicion {i} no es un tipo de mascota")

# for i in range(len(pets_list)): #No dependemos de saber previamente la longitud de la lista
#     if(type(pets_list[i]) == str):
#         print(pets_list[i])
#         if(pets_list[i].lower() == "perro"):
#             print("El mejor amigo del hombre")
#     else:
#         print(f"El valor en la posicion {i} no es un tipo de mascota")


for pet in pets_list: #Iterando por elementos
    if(type(pet) == str):
        print(pet)
        if(pet.lower() == "perro"):
            print("El mejor amigo del hombre")
    else:
        print(f"El valor en la posicion {pets_list.index(pet)} no es un tipo de mascota")