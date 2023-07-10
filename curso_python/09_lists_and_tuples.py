pets_list = ["Perro", 3, True] #Lista
pets_tuple = ("Perro", 3, True) #Tupla
one_item_tuple = (1,) #OJO que si tiene un solo elemento debe ir la coma al final
print(type(one_item_tuple))

print(pets_list)
print(pets_tuple)

print(pets_list[0]) #Recordar que el indice se cuenta desde cero
print(pets_tuple[2])

print(pets_list[-1]) #Siempre el ultimo elemento

# >>> +---+---+---+---+
# >>> |-4 |-3 |-2 |-1 |  <= negative indexes
# >>> +---+---+---+---+
# >>> | A | B | C | D |  <= sequence elements
# >>> +---+---+---+---+
# >>> | 0 | 1 | 2 | 3 |  <= positive indexes

#print(pets_list[3]) # OJO Indice fuera de la lista, la lista solo tiene indices 0, 1, 2

pets_list = pets_list + ["Gato"] 
print(pets_list)

pets_tuple = pets_tuple + ("Gato",) #No es modificacion, es guardar una nueva copia pero que tiene un elemento mas
print(pets_tuple)

pets_list = [*pets_list, *["Gato", "Loro"]] #Es lo mismo que ["Perro", 3, True, "Gato", "Loro"] 
print(pets_list)

pets_tuple = (*pets_tuple, *("Gato",)) #No es modificacion, es guardar una nueva copia pero que tiene un elemento mas
print(pets_tuple)

a, b, c = [1, 2, 3]
x, y, z = (1, 2, 3)

print(a)
print(y)
