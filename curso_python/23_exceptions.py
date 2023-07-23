# Pide números positivos y mételos en una lista, cuando el usuario meta un -1 ya 
# dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor.
# Dividir al mayor por un entero tambien ingresado por el usuario

nums = []
while(True):
    try:
        num = int(input("Ingrese un entero positivo: "))
        if(num > 0):
            nums.append(num)
        elif(num == -1):
            break
        else:
            print("El valor ingresado no es valido, por favor ingrese un entero positivo o -1 para salir")
    except Exception as e: #MALA PRACTICA, siempre atrapar excepciones particulares, son muy pocos los casos donde queremos excepts genericos
        print(f"Exception {type(e)}")
        print("El valor ingresado no es un entero, por favor intente nuevamente.")
nums.sort(reverse=True)
try:
    div = int(input("Ingrese un entero para dividir al mayor: "))
    result = nums[0]/div
    print(f"La division entre el mayor: {nums[0]} y el valor ingresado: {div} es {result}")
except ValueError as e: # Forma correcta para casi todos los casos, atrapar exceptiones particulares
        print(f"Exception {type(e)}")
        print("El valor ingresado no es un entero. No se hara la division")
except ZeroDivisionError as e:
        print(f"Exception {type(e)}")
        print("El valor ingresado es cero. No es posible dividir por cero")
print(nums)
