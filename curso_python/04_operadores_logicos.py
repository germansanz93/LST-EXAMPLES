# >	    Devuelve True si el valor de la izquierda es mayor que el valor de la derecha
# <	    Devuelve True si el valor de la derecha es mayor que el valor de la izquierda
# ==	Devuelve True si ambos valores son iguales
# >=	Devuelve True si el valor de la izquierda es mayor o igual que el valor de la derecha
# <=	Devuelve True si el valor de la derecha es mayor o igual que el valor de la izquierda
# !=	Devuelve True su los valores son diferentes

print(True < False)
print("Hola" == "Hola")
print("Hola" == "hola")
print("Hola" > "Hol")
print("Hola" > "Hola")


"""
    and

    X       |Y      |X and Y 
    ----------------------------
    True    |True   |True
    True    |False  |False
    False   |True   |False
    False   |False  |False

***************************************************************

    or

    X       |Y      |X or Y 
    ----------------------------
    True    |True   |True
    True    |False  |True
    False   |True   |True
    False   |False  |False


****************************************************************

    not

    X       |not X   
    --------------
    True    |False  
    False   |True   
    
    
"""

x = 3
y = 7
z = 10

print(x > y and y > z)
print(x < y and y < z)
print(x < y and z < y)  #True and False -> False
print(x < y or z < y)   #True or False -> True