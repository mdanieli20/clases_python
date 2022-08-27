# Set ( heterogeneos )

lista = ['soy', 'una', 'lista']
tupla = ('soy', 'una', 'tupla')
conjunto = {'soy', 'un', 'conjunto', 1, True}

# Set vacio
# otros_datos = []
# otros_datos1 = ()
# otros_datos2 = {}
# otros_datos3 = set()
# print(type(otros_datos))
# print(type(otros_datos1))
# print(type(otros_datos2))
# print(type(otros_datos3))

# Asignacion en un set
# lista[1] = 'uno'
# print(lista)
# tupla[1] = 'uno'
# print(tupla)
# conjunto[1] = 'uno'
# print(conjunto)

# print(lista[1])
# print(tupla[1])
# print(conjunto[1])


# Objetos mutables y los sets
# prueba = {1, 2, 3, 'hola', 'como', 'estas'}
# otra_prueba = ((1,2,3), [6,7,8])
# otra_prueba1 = {(1,2,3), [6,7,8]}

# print(otra_prueba)
# print(otra_prueba1)

# Set generado con iterables
# lista_prueba = [1, 2, 3, 'hola', 'como', 'estas', ['otra', 'lista']]
# lista_prueba = [1, 2, 3, 'hola', 'como', 'estas']
# conjunto_prueba = set(lista_prueba)
# conjunto_prueba2 = set(range(10))
# print(type(lista_prueba))
# print(type(conjunto_prueba))
# print(type(conjunto_prueba2))
# print(conjunto_prueba2)

# No se repiten valores
# lista = [1,2,3,4,5,6,6,6,6,1,2,3]
# conjunto = {1,2,3,4,5,6,6,6,6,1,2,3}
# print(lista)
# print(conjunto)



# auto = {'v8', 'Negro', (6, 'blindadas')}
# print(auto)

# Método add
# lista = [1,2,3,4,5,6,6,6,6,1,2,3]
# auto.add('descapotable')
# auto.add(lista)
# print(auto)

# Método update
# lista = ['soy', 'una', 'lista']
# tupla = ('soy', 'una', 'tupla')
# cadena = 'soy una cadena'
# rango = range(15)
# auto.update(lista)
# print(auto)
# auto.update(tupla)
# print(auto)
# auto.add(cadena)
# auto.update(cadena)
# print(auto)
# auto.update(rango)
# print(auto)

# Función len
# print(len(auto))

# Método discard
# auto.discard('lista')
# print(auto)
# auto.discard(543)
# print(auto)

# Método remove ( discard pero con generacion de error )
# auto.remove('tupla')
# print(auto)
# auto.remove(543)
# print(auto)

# .difference_update nos permite eliminar de a muchos pero siempre se le pasa un set
# auto.difference_update(utilizar un iterable)
# auto.difference_update(('tupla', 'lista'))
# print(auto)

# Operador in
auto = {'lista', 'Negro', (6, 'blindadas'), 'soy', 'v8', 'tupla', 'una'}
# for dato in auto:
#     print(dato)
# print('descapotable' in auto)
# print('caño de escape' not in auto)
# lista = [1,2,3,4]
# print(1 in lista)

# Método clear
# print(auto)
# auto = 'soy un texto'
# auto = set()
# auto.clear()
# print(auto)

# Método pop
# valor = auto.pop()
# print(auto)
# print(valor)

# while len(auto): 
#     print(auto)
#     auto.pop()
    
# Ej Sets (10min)
# Programa las siguientes instrucciones de forma ordenada sobre la variable grupo:
# Añade los usuarios: Ana, Ramón, Marta, Eric, David
# Elimina los usuarios: Mario, Miguel, Esteban

# grupo = {'Miguel', 'Blanca', 'Mario', 'Andrés'}


# BREAK


# Diccionarios

dicc = {}

# Las claves/llaves/keys pueden ser cualquier valor inmutable
# los valores/values pueden ser cualquier valor posible

# dicc1 = {
#     clave: valor,
#     clave2: valor2,
#     clave3: valor3,
#     ...
# }

# Anidamiento
# dicc2 = {
#     clave: dicc1,
#     clave2: valor2,
#     clave3: valor3,
#     ...
# }

# dicc = {
#     0: ['soy', 'una', 'lista'],
#     'tupla': ('soy', 'una', 'tupla'),
#     ('tupla', 'llave'): 'la tupla es mi llave'
# }


# auto = {'v8', 'Negro', (6, 'blindadas')}
auto = ['v8', 'Negro', (6, 'blindadas')]
# print(auto)
auto = {
    'motor': 'v8', 
    'color': 'Negro',
    'vidrios': (6, 'blindadas'),
    # 'vidrios': [6, 'blindadas'], # ****
    'pasajeros': 4,
}
# print(auto)

# auto['vidrios'][1] = 'otra cosa' # ****

# Acceso, mutabilidad, asignación, agregado de valores
# print(auto['motor'])
auto['motor'] = 'v12'
# print(auto)
# print(auto['motor'])

# palabra = 'pasajeros'

auto['pasajeros'] += 2
# auto[palabra] += 2
# print(auto)

auto['caja de cambios'] = 'automatica'
print(auto)

# Método update
# pepe = (1, 2)
# auto.update({pepe: 'valor1', 'llave2': 'valor2', 'motor': 'v8'})
# auto.update((('llave1', 'valor1'), ('llave2', 'valor2'), ('motor', 'v12')))
# print(auto)

# Función len
# print(len(auto))

# Función del
# del auto['color']
# del auto['ricardo']
# print(auto)

# Operador in
# print('motor' in auto)
# print('v12' in auto)
# print('v12' not in auto)

# Método clear
# auto.clear()
# auto = {}
# print(auto)

# Método pop
# valor = auto.pop()
# valor = auto.pop('color')
# auto.pop('color')
# auto.pop('ricardo')
# valor = auto.pop('ricardo')
valor = auto.pop('ricardo', 'este valor sale por defecto si no se encuentra la llave buscada')
# valor = auto.pop('ricardo', 'este valor sale por defecto si no se encuentra la llave buscada', 'qweqweqweqwe')
# valor = auto.pop('ricardo', input('dame un dato'))
# valor = auto.pop('color', 'la llave color no se encontro')
# valor = auto.pop(input('dame la key...?'), [1,2,3,45])
# print(auto)
# print(valor)


# cuanto_falta = {
#     113: '24min',
#     125: '15min',
#     'recoleta': '10min',
# }

# valor = cuanto_falta.pop(145, '10min')
# cuanto_falta.pop(145, '')
# print(valor)

# Ej Dics (10min)
# Programa las siguientes instrucciones de forma ordenada sobre la variable animales:
# Inicialmente el diccionario es: animales = {"elefante": ""}
# Añade al diccionario las claves perro, tigre y mono con sus respectivos valores “Bobby”,  “Peepe” y “Homero”
# Modificá las claves elefante y delfin con los valores “Trompis”y “Manolo” respectivamente