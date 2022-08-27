# def nombre_funcion(param1, param2):
#     var1 = 5
    # ==================================
    # return param1 + param2 + var1
    # ==================================
    # suma = param1 + param2 + var1
    # return suma
    # ==================================
    # if suma > 30:
    #     return 'Es mayor a 30'
    # else:
    #     return 'Es menor a 30'
    # ==================================
    # if suma > 30:
    #     return 'Es mayor a 30'
    # return 'Es menor a 30'


# print(nombre_funcion)
# print(nombre_funcion(5, 25))
# print(nombre_funcion(1, 21))

# ================================================================================
# ================================================================================

# Argumento y Parámetros
# def sumar(num1, num2):
#     return num1 + num2

# print(sumar(1, 5))
# print(sumar(5, 1))

# ================================================================================
# ================================================================================

# Argumentos x posición
# def restar(num1, num2):
#     return num1 - num2

# primera_ejecucion = restar(1, 5)
# print(f'Primera ejecución: {primera_ejecucion}')
# segunda_ejecucion = restar(5, 1)
# print(f'Segunda ejecución: {segunda_ejecucion}')

# ================================================================================
# ================================================================================

# Argumentos por nombre
# def restar(num1, num2):
#     return num1 - num2

# primera_ejecucion = restar(1, 5)
# print(f'Primera ejecución: {primera_ejecucion}')
# segunda_ejecucion = restar(num2=5, num1=1)
# print(f'Segunda ejecución: {segunda_ejecucion}')

# Otro ejemplo
# def devuelva_iterable(var1, var2, var3, var4, var5):
#     return (var1, var2, var3, var4, var5)

# print(devuelva_iterable(1,2,3,4,5))
# print(devuelva_iterable(4,3,1,5,2))
# print(devuelva_iterable(var4=4,var3=3,var1=1,var5=5,var2=2))
# print(devuelva_iterable(1,2,3,var5=5,var4=4))
# print(devuelva_iterable(var2=2,var4=4,3,1,5))
# print(devuelva_iterable(var2=2,3,4,var1=1,5))
# print(devuelva_iterable(1,2,4,var3=3))

# ================================================================================
# ================================================================================

# Llamadas sin argumentos
# def restar(num1, num2):
#     return num1 - num2
# primera_ejecucion = restar(15, 1)
# print(primera_ejecucion)

# def restar(num1=5, num2=1):
#     return num1 - num2
# primera_ejecucion = restar()
# print(primera_ejecucion)

# def restar(num1, num2=1):
#     return num1 - num2
# primera_ejecucion = restar(15,5)
# print(primera_ejecucion)

# def restar(num1=5, num2=1):
#     return num1 - num2
# primera_ejecucion = restar(num2=10,num1=4)
# print(primera_ejecucion)

# Parámetros por defecto
# def devuelva_iterable(var1=1, var2=2, var3=3, var4=4, var5=5):
#     return (var1, var2, var3, var4, var5)

# print(devuelva_iterable(1,2,3,4,5))
# print(devuelva_iterable(1,2,3,4))
# print(devuelva_iterable(1,2,3))
# print(devuelva_iterable(1,2))
# print(devuelva_iterable(1))
# print(devuelva_iterable())
# print(devuelva_iterable(5))
# print(devuelva_iterable(5,15))
# print(devuelva_iterable(var3=5,var5=15))
# print(devuelva_iterable(5,var5=15))
# print(devuelva_iterable(var5=15))

# print('pepe', 'fort', 'se', 'fue', 'de', 'viaje')
# print('pepe', 'fort', 'se', 'fue', 'de', 'viaje', sep=',')
# print('pepe', 'fort', 'se', 'fue', 'de', 'viaje', sep=',', end='\n')
# print('ricardo', 'fort', 'se', 'fue', 'de', 'viaje', sep=',', end='( estoy al final de mi print )')
# print('ricardo', 'fort', 'se', 'fue', 'de', 'viaje', sep=',', end=' ')
# print('ricardo', 'fort', 'se', 'fue', 'de', 'viaje', end='))))((((')

# ================================================================================
# ================================================================================

# break

# ================================================================================
# ================================================================================

# Argumentos x valor y referencia

# Recordatorio
# posiciones en disco |15|25|14|10|  |
#                     |  |  |  |  |  |

# guarda {1, 'conjunto1', (1, True)} en la posicion 15 de disco
# conjunto1 <--- posicion del disco 15

# ================================================================================
# ================================================================================

# Paso por valor
# def cambio(valor):
#     print(valor)
#     valor = 'otro valor'
#     print(valor)

# valor = 'pepe'
# cambio(valor)
# print(valor)

# ================================================================================
# ================================================================================

# Paso por referencia
# def cambio(dato_compuesto):
#     dato_compuesto.pop()
#     print(dato_compuesto)

# dato_compuesto = [15,True,'otro valor']
# cambio(dato_compuesto)
# print(dato_compuesto)
# datos_compuesto2 = dato_compuesto
# dato_compuesto2 = dato_compuesto[:]
# cambio(dato_compuesto2)
# print(dato_compuesto)

# ================================================================================
# ================================================================================

# def cambio():
#     global valor
#     valor = 'pepe'

# valor = 15
# cambio()
# print(valor)

# Simular uno con el otro
# def cambio(valor):
#     valor = 'otro valor'
#     return valor

# valor = 15
# valor = cambio(valor)
# print(valor)


# def cambio(dato_compuesto):
#     dato_compuesto += ['otro valor']

# dato_compuesto = [15,True]
# cambio(dato_compuesto)
# print(dato_compuesto)

# ================================================================================
# ================================================================================

# Argumentos indeterminados
# *args - **kwargs
 
# ================================================================================
# ================================================================================

# *args
# def sumar(num1, num2, num3, num4, num5):
#     return sum([num1, num2, num3, num4, num5])

# suma = sumar(1,5,1,2,3)
# print(suma)

# def sumar(*args):
#     print(type(args))
#     print(args)
#     return sum(args)

# suma = sumar(1,5,1,2,3,13,12,41,4,13,14,23,54,5,34,52,34,21)
# print(suma)


# def unir(*valores):
#     print(' '.join(valores))
        
# unir('hola', 'pepe', 'como', 'va')

# def devuelva_iterable(*args):
#     # print(type(args))
#     return args[:15]

# # devuelva_iterable(1)
# print(devuelva_iterable(1,1,2,3,4,1,2,3,1,2,3,1,2,3,1,4,2,2,3,1,2,3,1,2,3,1,1))
# print(devuelva_iterable(1,1,2,3,2,3,1,2,3,1,1))

# ================================================================================
# ================================================================================

# **kwargs
# def generar_presentacion(nombre='Pepe', apellido='Grillo', edad=80, profesion='MIAAAAAMIIIIIIIIIIIIIII'):
#     return f'Buenas, soy {nombre} {apellido}. Tengo {edad} años. Mi profesion es {profesion}.'


def generar_presentacion(**kwargs):
    print(type(kwargs))
    print(kwargs)
    presentacion = f'Buenas, soy {kwargs.get("nombre", "Pepe")} {kwargs.get("apellido", "Grillo")}. Tengo {kwargs.get("edad", "80")} años. Mi profesion es {kwargs.get("profesion", "grillo")}.'
    # if 'pepe' in kwargs.keys():
    #     presentacion += kwargs['pepe']
    return presentacion

presentacion = generar_presentacion(apellido='Forti', profesion1='MIAAAAAMIIIIIIIIIIIIIII', profesion2='MIAAAAAMIIIIIIIIIIIIIII', profesion='MIAAAAAMIIIIIIIIIIIIIII', profesion3='MIAAAAAMIIIIIIIIIIIIIII', profesion4='MIAAAAAMIIIIIIIIIIIIIII')
print(presentacion)

# ================================================================================
# ================================================================================

# Ej reloj (sin tiempo asignado)

# ================================================================================
# ================================================================================

# Recursividad

# def funcion():
#     funcion()
    
# funcion()

# ================================================================================
# ================================================================================

# Sin retorno
# def cuenta_regresiva(numero):
#     print(numero)
#     numero -= 1
#     if numero > 0:
#         cuenta_regresiva(numero)
#     else:
#         print("Boooooooom!")
#     print("Fin de la función", numero)
    
    
# cuenta_regresiva(5)

# ================================================================================
# ================================================================================

# Con retorno
# def factorial(numero):
#     print(("Valor inicial ->"),numero)
#     if numero > 1:
#         numero *= factorial(numero -1)
#     print(("valor final ->"),numero)
#     return numero

# print(factorial(5))

# ================================================================================
# ================================================================================

# Funciones integradas (built-in)

# int
# print(int('1'))

# float
# print(float('1.5'))
# print(float(True))

# str
# print(type(str(1)))

# round
# print(round(1.5))
# print(round(1.4))
# print(round(1.6))

# help()
# help(print)
# help(len)

# ================================================================================
# ================================================================================

# Revisión del desafio