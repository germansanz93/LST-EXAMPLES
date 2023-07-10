pets_list = ["Perro", 3, True, "Gato"] #Lista
pets_tuple = ("Perro", 3, True) #Tupla

pets_list[1] = "Gato"
print(pets_list)

# pets_tuple[1] = "Gato" #OJO las tuplas son inmutables
# print(pets_tuple)

# Funcion len()
print(len(pets_list))
print(len(pets_tuple))

# Metodos tanto para listas como para tuplas
# index
# count

print(pets_list.index("Gato")) #Devuelve el primer donde aparece determina valor (Parametro)
print(pets_tuple.index(True))

print(pets_list.count("Gato")) #Devuelve la cantidad de veces que aparece determina valor (Parametro)
print(pets_tuple.count(True))


# Metodos solo para listas

print()
print()
print()

print(pets_list)
pets_list.clear()
print(pets_list)
pets_list.append("Loro")
print(pets_list)
pets_list_copy = pets_list.copy()
print(pets_list_copy)
pets_list.extend(["Perro", "Gato"])
print(pets_list)
pets_list.insert(1, "Caiman")
print(pets_list)
pets_list.pop() #Remueve el ultimo elemento
print(pets_list)
pets_list.pop(1)
print(pets_list)
pets_list.reverse()
print(pets_list)
pets_list.append("Manati")
pets_list.sort(reverse=True)
print(pets_list)
