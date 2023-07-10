# while(condicion == True):
#     hace algo

# i = 0
# while(i < 10): # OJO que si la condicion nunca falla, el bucle sera infinito
#     print(i)
#     i += 1 # i = i + 1

print("Menu:")
print("1 Auto")
print("2 Moto")
print("-1 Salir")

isValid = False

while(not isValid):
    opcion = int(input("Seleccione una opcion: "))
    if(opcion == 1):
        print("Auto")
        isValid = True #Una forma de salir del bucle es con un flag
    elif(opcion == 2):
        print("Moto")
        break #Otra forma es con la sentencia break
    elif(opcion == -1):
        print("Chau")
        break
    else:
        print("Debe ingresar un valor correcto: ")