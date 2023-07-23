# Inicio del scope global
var = 10

def foo():
    #Inicio del scope de foo
    var = 17 #No modifica var globales, lo que hace es crear una nueva var, esta vez en el scope de foo y le asigna ese nombre var
    var_foo = 5
    print("En el scope de foo var vale", var)
    if(True):
        #No tiene un un scope
        var_foo = -10
    print("En el scope de foo var_foo vale", var_foo)    
    #Fin del scope de foo
    return var

print("En el scope global var vale", var)
var = foo() #Puedo modificarla solo en el scop global
print("En el scope global var vale", var)
# print("En el scope global var_foo vale", var_foo) #OJO que en este punto var_foo no existe mas
# Fin del scope global