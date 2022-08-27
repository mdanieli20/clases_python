# if / multiples if /anidado de if / else / elif

input1 = int(input('Primer valor: '))
input2 = int(input('Segundo valor: '))
# input3 = int(input('Tercero valor: '))
# input4 = int(input('Cuarto valor: '))

var = 5
var*= 150
var+= 6
var-= 200
var**= 3
var/= 2

# if
# if True:
#     print('Hola, empece con los if')

# if False:
#     print('Hola, empece con los if')
    
# if input1 < input2:
#     print('Hola, empece con los if')

# if input1 > input2:
#     print('Adios')

# if input1 == input2:
#     print('no se nada')

# print('Segui por afuera')

# if input1 < input2 and input1 != input2 - 5:
#     print('me parece raro')

# if input1 < input2:
#     print('input1 es menor')
#     if input1 == input2 - 3:
#         print('input1 es igual a input2 menos 3')


# print('Segui por afuera')


# multiples if


# anidado de if


# break


# else

# if input1 == input2:
#     print('son iguales')
# else:
#     print('no son iguales')

# print('segui por arafue')

# if input1 < input2:
#     print('input1 es menor')
# if input1 == input2:
#     print('son iguales')
#     if input1 < var:
#         print('son menores a var')
#     else:
#         print('no son iguales')
# else:
#     print('no son iguales')
#     if input1 < var:
#         print('son menores a var')
#         if input1 < var:
#             print('son menores a var')
#         else:
#             print('no son iguales')
#     else:
#         print('no son iguales')

# print('segui por arafue')


# if input1 == input2:
#     print('son iguales')
#     if input1 < var:
#         print('son menores a var')
#     else:
#         print('no son iguales')
# else:
#     print('no son iguales')

# print('segui por arafue')


# elif

# if input1 < input2:
#     print('input1 es menor que input2')
# elif input1 == input2:
#     print('son iguales')
# else:
#     print('input2 es menor que input1')

# if input1 < 20:
#     print('es menor a 20')
#     if input1 < 30:
#         print('es menor a 30')
#         if input1 < 40:
#             print('es menor a 40')
#             if input1 < 50:
#                 print('es menor a 50')


# if input1 < 20:
#     print('es menor a 20')
# elif input1 < 30:
#     print('es menor a 30')
# elif input1 < 40:
#     print('es menor a 40')
# elif input1 < 50:
#     print('es menor a 50')
# else:
#     print('no se cumplio ninguna condicion de las anteriores')



if input1 < input2:
    print('input1 es menor que input2')
elif input1 == input2:
    print('son iguales')
    if input1 < 20:
        print('es menor a 20')
    elif input1 < 30:
        print('es menor a 30')
    elif input1 < 40:
        print('es menor a 40')
    elif input1 < 50:
        print('es menor a 50')
    else:
        print('no se cumplio ninguna condicion de las anteriores')
else:
    print('input2 es menor que input1')
    
variable = 0
if input1 < input2:
    variable += 15
elif input1 == input2:
    variable += 24
    if input1 < 20:
        variable *= 15
    elif input1 < 30:
        variable /= 15
    elif input1 < 40:
        variable **= 15
    elif input1 < 50:
        variable -= 15
    else:
        print('no se cumplio ninguna condicion de las anteriores')
else:
    print('input2 es menor que input1')

# =================================================================================================
# =================================================================================================

# Ej 1: Mayoría de edad (5min)
# Escribir un programa que le pregunte al usuario su edad y
# muestre por pantalla si es mayor de edad o no.


# Ej 2: Marvel vs Capcom (20min)
# Un curso se ha dividido en dos grupos: A y B de acuerdo al nombre y a 
# una preferencia (Marvel o Capcom). 
# El grupo A está formado por fans de Marvel con un nombre anterior a la M y 
# los fans de Capcom con un nombre posterior 
# a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y preferencia, 
# y muestre por pantalla el grupo que le corresponde.
