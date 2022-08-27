
# EJERCICIO 1 //
# CONSIGNA:
# Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura.
# Calcula el área de un rectángulo de 15 de base y 10 de altura.
# 🖐 Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.

# def area_rectangulo(base=15, altura=10):
#     return int(base) * int(altura)
# print('El area del rectangulo es: ', area_rectangulo())
# #print('El area del rectangulo es: ', area_rectangulo(int(input('Ingrese el valor de base: ')), int(input('Ingrese el valor de la altura: '))))


# EJERCICIO 2 //
# CONSIGNA:
# Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. 
# Calcula el área de un círculo de 5 de radio.
# 🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. 
# Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.
# import math
# print(math.pi)
# import math
# def area_circulo(radio=5):
#     return (radio ** 2) * math.pi
# print('El área del círculo es: ', "{:.2f}".format(area_circulo()))
# #Dejo opción para poder ingresar el radio
# #print('El área del círculo es: ', "{:.2f}".format(area_circulo(int(input('Ingrese el valor del radio: ')))))


# EJERCICIO 3 //
# CONSIGNA:
# Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:
# 1 - Si el primer número es mayor que el segundo, debe devolver 1.
# 2 - Si el primer número es menor que el segundo, debe devolver -1.
# 3 - Si ambos números son iguales, debe devolver un 0.
# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

# def relacion(num1, num2):
#     if num1 > num2:
#         return 1
#     elif num1 < num2:
#         return -1
#     elif num1 == num2:
#         return 0
    
# def comprueba(relacion):
#     if  relacion == 1:
#         print('El primer número es mayor que el segundo')
#     elif relacion == -1:
#         print('El primer número es menor que el segundo')
#     elif relacion == 0:
#         print('Ambos números son iguales')

# comprueba(relacion(5, 10))
# comprueba(relacion(10, 5))
# comprueba(relacion(5, 5))

# #Dejo una opcion comentada por si se requiere ingresar por consola los numeros a comparar
# #comprueba(relacion(int(input('Ingrese el primer numero: ')), int(input('Ingrese el segundo numero: '))))


# EJERCICIO 4 //
# CONSIGNA:
# Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:
# 🖐 Ayuda: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2
# Comprueba el punto intermedio entre -12 y 24

# def intermedio(num1, num2):
#     return (num1 + num2) / 2

# print('El número intermedio entre -12 y 24 es: ', int(intermedio(-12, 24)))
# #Dejo una opcion comentada donde podriamos ingresar por consola ambos números
# #print('El número intermedio entre ambos es: ', int(intermedio(int(input('Ingrese un número: ')), int(input('Ingrese el segundo número: ')))))


# EJERCICIO 5 //
# CONSIGNA:
# Realizá una función llamada recortar() que reciba tres parámetros.
# El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior.
# La función tendrá que cumplir lo siguiente:
# 1 - Devolver el límite inferior si el número es menor que éste.
# 2 - Devolver el límite superior si el número es mayor que éste.
# 3 - Devolver el número sin cambios si no se supera ningún límite.
# # Comprueba el resultado de recortar 15 entre los límites 0 y 10

# def recortar(num, lim_inf, lim_sup):
#     if num < lim_inf:
#         return lim_inf
#     elif num > lim_sup:
#         return lim_sup
#     elif lim_inf <= num <= lim_sup:
#         return num
   
# print('El resultado de recortar 15 entre los límites 0 y 10 es: ', recortar(5, 0, 10))

# # Dejo comentada opcion que permite ingresar valores por consola
# # num = int(input('Ingrese un número: '))
# # lim_inf = int(input('Ingrese el límite inferior: '))
# # lim_sup = int(input('Ingrese el límite superior: '))
# # print('El resultado de recortar ' + str(num) + ' entre los límites ' + str(lim_inf) + ' y ' + str(lim_sup) + ' es: ', recortar(num, lim_inf, lim_sup))



# EJERCICIO 6 //
# CONSIGNA:
# Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
# La primera con los números pares, y la segunda con los números impares:
# 🖐 Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()
# Por ejemplo:
# pares, impares = separar([6,5,2,1,7])
# print(pares)   # valdría [2, 6]
# print(impares)  # valdría [1, 5, 7]

def separar(*arg):
    pares = []
    impares = []
    for i in arg:
        if i % 2 != 0:
            impares.append(i)
        else:
            pares.append(i)
    pares.sort()
    impares.sort()
    return pares, impares

#pares, impares = separar([6,5,2,1,7])
pares, impares = separar(10,33,1,2,8,4,5)
print(pares)
print(impares)
        
    

