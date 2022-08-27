# Escribí un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso.
# Luego debe comprobar si el número se encuentra en la lista de números y notificarlo: numeros = [1, 3, 6, 9]
# 🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)

print('''
Ingresar un número entero que se encuentre entre el 0 y el 9
      ''')
lista = [1, 3, 6, 9]
valor = int(input('Ingresar número: '))

while True:
    if 0 <= valor <= 9:
        if valor in lista:
            print('El número ingresado pertenece a la lista, hasta luego :)')
            break
        else:
            print('El número ingresado no pertenece a la lista, hasta luego :(')
            break
    else:
        print('El número ingresado no se encuentra entre el intervalo 0-9')
        valor = int(input('Ingrese otro número: '))

    