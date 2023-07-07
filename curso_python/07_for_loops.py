# se requiere imprimir los primeros 10 numeros enteros

for i in range(0, 10, 1): #crea una variable i, inicializala en cero y anda sumandole 1 hasta que llegue a 10
    print(i)                #range(inicio, fin, paso) OJO incluye el valor de inicio, pero no el de fin

print()

for i in range(0, 10): #si el paso es 1 puedo no indicarlo
    print(i)

print()

for i in range(10): #Si el inicio es 0 y el paso es 1 puedo no indicarlos y python les asignara esos valores por defecto
    print(i)

print()

for j in range(5, 7, 1): #arrancamos desplazados 5 numeros y finalizamos en 7
    print(j)

print()

for par in range(0, 100, 2):
    print(par)

for k in range(10, 0, -1):
    print(k)

string = "Hello World"
for x in string:
    print(x)

