# Un programa que decida si una persona es mayor de edad
# Usuario ingresa su edad
# Si la edad es mayor o igual a 18 -> "Sos mayor de edad"
# Si la edad es mayor o igual a 14 o menor a 18 -> sos adolescente
# Sino -> "Sos menor de edad"

edad = int(input("Ingrese su edad: "))


if(edad >= 18):
    print("Sos mayor de edad.")
elif(edad >= 14):
    print("Sos adolescente.")
else:
    print("Sos menor de edad.")

print("Fin del programa.")
