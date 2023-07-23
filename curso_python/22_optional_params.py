def suma_dos(x, y):
    print(x, y)
    print(f"La suma es: {x + y}")

def suma_tres(x, y, z):
    print(x, y, z)
    print(f"La suma es: {x + y + z}")

def suma(x, y, z = 0, nombre="nombre"):
    print(x, y, z)
    print(f"La suma es: {x + y + z}")
    print(f"El nombre de la persona es {nombre}")

def suma_n(x, y, *args, **kwargs):
    suma = x + y
    for num in args:
        suma += num
    print(f"La suma es: {suma}")
    nombre = kwargs.get("nombre", "nombre")
    apellido = kwargs.get("apellido", "")
    print(f"El nombre de la persona es {nombre} {apellido}")



# suma_dos(4, 5)
# print()
# suma_tres(4, 5, 6)
# print()
# suma(4, 5)
# print()
# suma(4, 5, 6)
# print()
# suma(4, 5, nombre = "lasecta")
print()
suma_n(4, 5, 6, 7, 8, 9, 10, 11, 12, 15, nombre="Bruce", apellido="Dickinson")
print()
suma_n(4, 5, 6)
