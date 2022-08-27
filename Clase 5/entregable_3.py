#Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:
#Ayuda: Podes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números.

# range(<valor incial incluido>, <valor final sin incluirlo>, <salto>)

numero = 0
impares = []
for numero in range(1,101, 2):
    impares.append(numero)
print ('La suma de los impares es: ', sum(impares))