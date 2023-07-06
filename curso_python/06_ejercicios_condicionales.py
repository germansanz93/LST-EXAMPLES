#Crear un programa que reciba un numero por teclado y decida si es par o impar
# n = int(input("Ingrese un numero entero: "))

# if(n % 2 == 0):
#     print(f"El numero {n} es par.")
# else:
#     print(f"El numero {n} es impar.")


#Crear un programa que reciba dos numeros por teclado y decida cual es el mayor

# n1 = int(input("Ingrese el primer valor: "))
# n2 = int(input("Ingrese el segundo valor: "))

# if(n1 > n2):
#     print(f"El valor {n1} es mayor a {n2}")
# elif(n2 > n1):
#     print(f"El valor {n2} es mayor a {n1}")
# else:
#     print(f"Los valores {n1} y {n2} son iguales.")

#Crear un programa que reciba tres numeros por teclado y decida cual es el mayor

# n1 = int(input("Ingrese el primer valor: "))
# n2 = int(input("Ingrese el segundo valor: "))
# n3 = int(input("Ingrese el tercer valor: "))

# mayor = 0

# if(n1 >= n2):
#     if(n1 >= n3):
#         mayor = n1
#     else:
#         mayor = n3
# else:
#     if(n2 >= n3):
#         mayor = n2
#     else:
#         mayor = n3


# print(f"El numero {mayor} es el mayor.")


#Crear un programa que le pida al usuario que seleccione si quiere sumar, restar, dividir o multiplicar
#Luego de eso se le debe solicitar al usurio que ingrese dos numeros
#Si se eligio la division y el segundo numero es cero, se debe mostrar un mensaje y no calcular el valor

print("Menu:")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")

menu = int(input("Seleccione una de las opciones: "))

if(menu > 4 or menu <= 0):
    print("Opcion invalida.")
else: 
    n1 = float(input("Ingrese el primer valor: "))
    n2 = float(input("Ingrese el segundo valor: "))

resultado = None

if(menu == 1):
    resultado = n1 + n2
elif(menu == 2):
    resultado = n1 - n2
elif(menu == 3):
    resultado = n1 * n2
elif(menu == 4):
    if(n2 == 0):
        print("No se puede dividir por cero.")
    else:
        resultado = n1 / n2

if(resultado != None):
    print(f"El resultado de su operacion es: {resultado}")

