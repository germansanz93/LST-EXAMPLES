# Crea una tupla con los meses del año, pide un número al usuario, 
# si el numero esta entre 1 y la longitud máxima de la tupla, 
# muestra el contenido de esa posición sino muestra un mensaje de error.
months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

# month_number = int(input("Ingrese el numero del mes: "))

# if(1 <= month_number <= 12):
#     print(f"El mes seleccionado es: {months[month_number - 1]}")
# else:
#     print(f"El valor {month_number} no corresponde con ningun mes.")

# Pide números positivos y mételos en una lista, cuando el usuario meta un -1 ya 
# dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor.

# nums = []
# while(True):
#     num = int(input("Ingrese un entero positivo: "))
#     if(num > 0):
#         nums.append(num)
#     elif(num == -1):
#         break
#     else:
#         print("El valor ingresado no es valido, por favor ingrese un entero positivo o -1 para salir")
# nums.sort(reverse=True)    
# print(nums)

# Pide una cadena por teclado, mete los caracteres en una lista sin repetir caracteres.
input_string = input("Ingrese un texto: ")
unique_chars = []

for letter in input_string:
    if(unique_chars.count(letter) == 0):
        unique_chars.append(letter)

print(unique_chars)