#Escribí un programa que pida al usuario cuantos números quiere introducir.
#Luego lee todos los números y realiza una media aritmética:

print('''
Indique la cantidad de números que desea ingresar      
      ''')
cantidad = int(input('Ingrese cantidad: '))
lista = []
while cantidad != 0:
    numeros = int(input('Ingrese número: '))
    lista.append(numeros)
    cantidad = cantidad - 1
print('La media aritmética de los numeros ingresados es: ', sum(lista)/len(lista))