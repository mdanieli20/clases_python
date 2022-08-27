# EJERCICIO 1 //

# Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:

# Mostrar una suma de los dos números.
# Mostrar una resta de los dos números (el primero menos el segundo).
# Mostrar una multiplicación de los dos números.
# Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará.
# En caso de no introducir una opción válida, el programa informará de que no es correcta.

opciones ='''
Opciones:
1 - Suma los valores ingresados.
2 - Resta los valores ingresados.
3 - Multiplica los valores ingresados.
4 - Sale del programa.
5 - Lista las opciones.
'''
print(opciones)

numero1 = int(input('Ingrese el primer número: '))
numero2 = int(input('Ingrese el segundo número: '))
resultado = 0

while True:
    opcion = int(input('Ingrese una opción: '))
    if  opcion <= 0 or opcion >= 6:  
        print('Ingresó una opción no valida')
        continue
    elif opcion == 1:
        resultado = numero1 + numero2
        print('La suma de ambos números es: ', resultado)
        opcion = 4
    elif opcion == 2:
        resultado = numero1 - numero2
        print('La resta de ambos números es: ', resultado)
        opcion = 4
    elif opcion == 3:
        resultado = numero1 * numero2
        print('La multiplicación de ambos números es: ', resultado)
        opcion = 4
    elif opcion == 4:
        break
    elif opcion == 5:
        print(opciones)

