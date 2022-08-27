# Strings

cadena1 = 'soY la pRimer cadena'
cadena2 = 'segunda cadena al rescate'

# Método upper
# print(cadena1)
# cadena1_en_mayusculas = cadena1.upper()
# cadena1 = cadena1.upper()
# print(cadena1)
# print(cadena1_en_mayusculas)

# Método lower
# cadena1_en_mayusculas_en_minusculas = cadena1_en_mayusculas.lower()
# cadena1_en_mayusculas_en_minusculas = cadena1.lower()
# print(cadena1_en_mayusculas_en_minusculas)

# Método capitalize
# cadena1_capitaliciada = cadena1.capitalize()
# cadena1_capitaliciada = cadena1_en_mayusculas.capitalize()
# print(cadena1_capitaliciada)

# Método title
# cadena1_titleada = cadena1.title()
# cadena1_titleada = cadena1_en_mayusculas.title()
# print(cadena1_titleada)

# Método count
# cadena1 = 'soY la pRimer cadena'
# print(cadena1.count('oy'))
# print(cadena1.count('oY'))
# print(cadena1.count('a', 2, 16))

# Método find
# cadena1 = 'soY la pRimer oY cadena'
# print(cadena1.find('oy'))
# print(cadena1.find('oY'))
# print(cadena1.find('oY', 2, 17))

# Método rfind
# print(cadena1.rfind('oy'))
# print(cadena1.rfind('oY'))
# print(cadena1.rfind('oY', 1, 4))

# Método split
# cadena2 = 'segunda acAdena al arescate'
# print(cadena2.split())
# cadena2_spliteada = cadena2.split('a a')
# print(cadena2_spliteada)
# print(cadena2.split(' a'))

# Método join
# print(' uni con esto '.join(cadena2_spliteada))
# print('<?>'.join(['superman']))
# print('<?>'.join(['superman', 'batman']))
# print('<?>'.join(['superman', 'batman', 'mujer maravilla']))
# pepe = 'valor'
# otro = 'dato'
# print('[////]'.join([pepe, otro]))

# Método strip
# palabra_repetida = 'cadena cadena cadena cadena cadena'
# palabra_repetida2 = f'   {palabra_repetida}   '
# print(palabra_repetida2)
# print(palabra_repetida2.strip())
# palabra_repetida2 = f'pepito{palabra_repetida}pepito'
# print(palabra_repetida2)
# print(palabra_repetida2.strip('pepito'))

# Método replace
# print(palabra_repetida)
# print(palabra_repetida.replace('cadena', 'otra'))
# print(palabra_repetida.replace('cadena', 'otra', 3))


# Listas

# lista1 = ['primera', 'lista', 1]
# lista2 = ['segunda', 'lista', 2]
# lista_numeros = ['5','1','2','3','4','10']

# Método clear
# lista1 = []
# lista2.clear()
# print(lista1)
# print(lista2)

# Método extend
# print(lista1 + lista2)
# print(lista1)
# lista1 += lista2
# lista1.extend(lista2)
# lista1.extend('otro')
# print(lista1)

# Método insert
# lista2 = ['segunda', 'lista', 2]
# dicc = {
#     'llave': 'valor'
# }
# print(lista2)
# lista2.insert(1, dicc)
# print(lista2)
# lista2.insert(3, [45, 35, 25])
# lista2.insert(3, 'string')
# print(lista2)

# Método reverse
# lista2 = ['segunda', 'lista', 2]
# print(lista2)
# lista2.reverse()
# lista2 = lista2[::-1]
# print(lista2)

# Método sort
# lista_numeros = [5,1,2,3,4,10]
# lista_numeros1 = ['5','1','2','3','4','10']
# lista_numeros.sort()
# lista_numeros.sort(reverse=True)
# print(lista_numeros)
# lista_numeros1.sort()
# lista_numeros1.sort(reverse=True)
# print(lista_numeros1)

# ejercicio - colecciones 1 (20min)
# Utilizando todo lo que sabes sobre cadenas, listas y
# sus métodos internos, transforma este texto:

texto = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista'

# Gordon lanzó su curva...
# - Strawberry ha fallado por un pie! -gritó Joe Castiglione.
# - Dos pies -le corrigió Troop.
# - Strawberry menea la cabeza como disgustado… -agrega el comentarista.

# texto_v2 = texto.replace('&', '\n')
# primera_ubicacion = texto_v2.find('\n')
# segunda_ubicacion = texto_v2.find('\n', primera_ubicacion+1)
# tercera_ubicacion = texto_v2.rfind('\n')
# texto_v3 = texto_v2[:primera_ubicacion+1].capitalize() + '- ' + texto_v2[primera_ubicacion+1:segunda_ubicacion+1].capitalize() + '- ' + texto_v2[segunda_ubicacion+1:tercera_ubicacion +1].capitalize() + '- ' + texto_v2[tercera_ubicacion+1:].capitalize()
# texto_v4 = texto_v3.replace('troop', 'Troop').replace('joe', 'Joe').replace('castiglione', 'Castiglione')
# lista_oraciones = texto_v4.split('\n')
# lista_oraciones[0] += '...'
# lista_oraciones[1] += '.'
# lista_oraciones[2] += '.'
# lista_oraciones[-1] += '.'
# print('\n'.join(lista_oraciones))


# parte de v2
# texto = texto.replace('&', '...\n- ', 1)
# texto = texto.replace('&', '.\n- ', 2) + '.'
# print(texto)


# break

# Conjuntos
# numero1 = 1
# numero2 = numero1
# numero1 += 2
# print(numero1)
# print(numero2)

conjunto1 = {1, 'conjunto1', (1, True)}
conjunto2 = {2, 'conjunto2', (1, True)}

# posiciones en disco |15|25|14|10|  |
#                     |  |  |  |  |  |  

# guarda {1, 'conjunto1', (1, True)} en la posicion 15 de disco
# conjunto1 <--- posicion del disco 15


# Método copy
# conjunto3 = conjunto1
# conjunto3 = conjunto1.copy()
# print(conjunto3)
# conjunto1.add(456)
# print(conjunto3)

# # listas o tuplas -->> lista2 = lista[:] / tupla2 = tupla[:]
# lista1 = [1,2,3,4,5]
# lista2 = lista1
# lista2 = lista1[:]
# print(lista2)
# lista1.append(45)
# print(lista2)

# conjunto3 = conjunto1.copy()
# print(conjunto3)
# conjunto1.add('otro dato')
# print(conjunto1)
# print(conjunto3)


# Método isdisjoint (distintos)
# conjunto1 = {1, 'conjunto1', (1, True)}
# iterable2 = (2, 'conjunto2', (2, True))
# # el primero tiene que ser un set... el segundo un iterable
# print(conjunto1.isdisjoint(iterable2))

# Método issubset
# conjunto1 = {1, 'conjunto1', (1, True)}
# iterable2 = (1, 'conjunto1', (1, True), 45)
# print(conjunto1.issubset(iterable2))

# Método issuperset
# conjunto1 = {1, 'conjunto1', (1, True), 45}
# iterable2 = (1, 'conjunto1', (1, True), 523)
# print(conjunto1.issuperset(iterable2))

# Método union
# conjunto3 = conjunto1.union(iterable2)
# print(conjunto1)
# print(conjunto3)

# Método difference
# print(conjunto1.difference(iterable2))

# Método difference_update
# conjunto1.difference_update(iterable2)
# print(conjunto1)

# Método intersection
# print(conjunto1.intersection(iterable2))
# print(conjunto1)

# Método intersection_update
# print(conjunto1.intersection_update(iterable2))
# print(conjunto1)


# Diccionarios

# diccionario1 = {'estado': 'Activo', 'deporte': 'Paddle'}
# diccionario2 = {'deporte': 'Paddle'}

# Método get
# valor = diccionario1['estado']
# valor = diccionario1['ricardo']
# valor = diccionario1.get('ricardo', 123)
# print(valor)

diccionario1 = {'estado': 'Activo', 'deporte': 'Paddle'}
# print('estado' in diccionario1)
# print('Activo' in diccionario1)

# Método keys
# print(diccionario1.keys())
# print(list(diccionario1.keys()))
# for llave in diccionario1.keys():
#     print(llave)

# Método values
# print(diccionario1.values())
# print(list(diccionario1.values()))
# for valor in diccionario1.values():
#     print(valor)

# Método items
# print(diccionario1.items())
# for llave, valor in diccionario1.items():
#     print(llave)
#     print(valor)
#     print()

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# for (pepito, ricardo) in auto.items():
#     print(pepito, ricardo)
#     print()


# ejercicio - colecciones 2 (30min)
# A partir de una lista realizar las siguientes tareas sin modificar la lista original:

# lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

# 1. Borrar los elementos duplicados
# 2. Ordenar la lista de mayor a menor
# 3. Eliminar todos los números impares
# 4. Realizar una suma de todos los números que quedan
# 5. Añadir como primer elemento de la lista la suma realizada
# 6. Devolver la lista modificada
# 7. Finalmente, después de ejecutar la función, comprueba que la suma de todos 
# los números a partir del segundo, concuerda con el primer número de la lista



lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

# 1. Borrar los elementos duplicados
sin_duplicados = list(set(lista))

# 2. Ordenar la lista de mayor a menor
sin_duplicados.sort()
sin_duplicados.reverse()

# 3. Eliminar todos los números impares
lista_sin_impares = []
for valor in sin_duplicados:
    if valor % 2 == 1:
        continue
    else:
        lista_sin_impares.append(valor)

# 4. Realizar una suma de todos los números que quedan
suma = sum(lista_sin_impares)

# 5. Añadir como primer elemento de la lista la suma realizada
lista_sin_impares.insert(0, suma)

# 6. Devolver la lista modificada
print(lista_sin_impares)


# 7. Finalmente, después de ejecutar la función, comprueba que la suma de todos 
# los números a partir del segundo, concuerda con el primer número de la lista
suma_total = sum(lista_sin_impares[1:])
print(suma_total)
