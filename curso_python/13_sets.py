my_set = {"Hola", 3, 1, 0,  False, 5.32, "Hola"} #set
my_set.add("Chau")
my_set.add(True)

new_set = set(["e1", "e2", 3, False])
immutable_set = frozenset(["e1", 3, "chau"])
print(my_set)
print(new_set)
print(immutable_set)
print("Hola" in my_set)

print(len(my_set))