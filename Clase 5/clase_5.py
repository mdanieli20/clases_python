# While ( no se conoce cantidad de iteraciones )

# valor = 2
# otro_dato = 1
# while valor:
#     print(f'Valor: {valor * otro_dato}')
#     if otro_dato == 15:
#         valor = 0
#     otro_dato += 1
    

# Bucle infinito
# while True:
#     print('No salimos mas de aca...')

# Fujo de ejecucion
# condicion = 0
# condicion = 5
# while condicion:
#     condicion -= 1
#     valor1 = 5
#     valor2 = 2
#     suma = valor1 * valor2 + condicion
#     print(f'La suma dio de resultado {suma}')
#     # condicion -= 1

# variable = 'Aca ya estamos fuera del bucle'
# print(variable)

# Ej 1 (10 min)
# Escribir un programa que le pregunte al usuario números hasta que ingrese el 0, 
# cuando lo haga mostrar por pantalla la suma de todos los números ingresados.

# Break

# condicion = 10
# while condicion:
#     valor1 = 5
#     valor2 = 2
#     suma = valor1 * valor2 * condicion
#     if suma == 20:
#         break
#     print(f'La suma dio de resultado {suma}')
#     condicion -= 1

# variable = 'Aca ya estamos fuera del bucle'
# print(variable)


# Revismos el codigo
# c = -3
# while True:
#     c += 1
#     if c == 2:
#         print('ahora que c vale 2 salimos')
#         break
#     print('c vale ', c)


# While - Else

# condicion = 10
# while condicion:
#     valor1 = 5
#     valor2 = 2
#     suma = valor1 * valor2 * condicion
#     if suma == 20:
#         break
#     print(f'La suma dio de resultado {suma}')
#     condicion -= 1
# else: # nunca pasa por este bloque de codigo porque se corta el while con el break
#     print('pase por el else')

# variable = 'Aca ya estamos fuera del bucle'
# print(variable)


# Continue

# condicion = 10
# while condicion:
#     valor1 = 5
#     valor2 = 2
#     suma = valor1 * valor2 * condicion
#     condicion -= 1
#     if suma == 20:
#         continue
#     print(f'La suma dio de resultado {suma}')

# variable = 'Aca ya estamos fuera del bucle'
# print(variable)


# Pass

# condicion = 10
# while condicion:
#     valor1 = 5
#     valor2 = 2
#     suma = valor1 * valor2 * condicion
#     if suma == 20:
#         pass
#     print(f'La suma dio de resultado {suma}')
#     condicion -= 1

# variable = 'Aca ya estamos fuera del bucle'
# print(variable)


# Usos del pass


# if True:
#     pass # ...
# print('estoy fuera del if')

# nombre = input('Ingrese nombre')
# if nombre == '****':
#     pass

# For ( se conoce cantidad de iteraciones )

# condicion = 10
# while condicion:
#     valor1 = 5
#     valor2 = 2
#     suma = valor1 * valor2 * condicion
#     print(f'La suma dio de resultado {suma}')
#     condicion -= 1

# indice = 0
# # dato_de_la_lista = 5
# lista = [10,9,8,7,6,5,4,3,2,1]
# for dato_de_la_lista in lista:
#     valor1 = 5
#     valor2 = 2
#     suma = valor1 * valor2 * dato_de_la_lista
#     print(f'La suma dio de resultado {suma}')
#     lista[indice] = dato_de_la_lista * 2
#     indice += 1

# variable = 'Aca ya estamos fuera del bucle'
# print(variable)
# print(lista)


# Enumerate

# dato_de_la_lista = 5
# lista = [10,9,8,7,6,5,4,3,2,1]
# for valores_devueltos in enumerate(lista):
#     print(valores_devueltos)
# for indice, valor_de_la_lista in enumerate(lista):
#     valor1 = 5
#     valor2 = 2
#     suma = valor1 * valor2 * valor_de_la_lista
#     print(f'La suma dio de resultado {suma}')
#     lista[indice] = valor_de_la_lista * 2

# variable = 'Aca ya estamos fuera del bucle'
# print(variable)
# print(lista)

# tupla = ('ricado', 4, True)
# nombre, edad, pelado = tupla
# print(tupla)
# print(nombre)
# print(edad)
# print(pelado)

# Range


# lista = [10,9,8,7,6,5,4,3,2,1]
# for valor_de_la_lista in lista:
#     valor1 = 5
#     valor2 = 2
#     suma = valor1 * valor2 * valor_de_la_lista
#     print(f'La suma dio de resultado {suma}')
    
# range(<valor final sin incluirlo>)
# range(<valor incial incluido>, <valor final sin incluirlo>)
# range(<valor incial incluido>, <valor final sin incluirlo>, <salto>)
# for numero in range(9, 5, -2):
# for numero in range(5, 9, 2):
#     valor1 = 5
#     valor2 = 2
#     suma = valor1 * valor2 * numero
#     print(f'La suma dio de resultado {suma}')

# variable = 'Aca ya estamos fuera del bucle'
# print(variable)


# For - Else
# For - break/continue/pass

# for numero in range(5, 9):
#     # if numero == 7:
#     #     break
#     # if numero == 7:
#     #     continue
#     if numero == 7:
#         pass
#     print(numero)
# else:
#     print('pase por el else')
    
# print(list(range(5, 9)))



# Ej 2 (15 min)
# Haremos el siguiente listado de ejercicios:
# Escribir un programa que enumere los países de la siguiente lista:
# paises = ['Canada', 'USA', 'Mexico', 'Australia', Argentina, China, India]
# Crear un bucle que sume los pares del 0 al 100
# Imprimir por pantalla los números del 1 al 10 al revés
# Pedirle a un usuario que ingrese un número, y devolver los dígitos totales del número
# Por ejemplo, si el número es 75869, la salida debería ser 5.
# Nota:
# Para imprimir por pantalla al reves se debe usar el mayor número, luego el menor, 
# y el paso sería con -1 range(mayor, menor, -1)


# Revisar Entregable
