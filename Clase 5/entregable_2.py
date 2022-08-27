# Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, 
# debe repetirse el proceso hasta que lo introduzca correctamente.

# Numero impar es aquel que al dividirlo por 2 no devuelve un numero entero. Por ende num % 2 debe devolver 0, si el resultado es diferente el numero es impar.

num = int(input('Ingrese un número: '))

while True:
    if num % 2 != 0:
        print ('El número ingresado es impar')
        break
    else:
        print ('El número ingresado es par, ingrese un nuevo número')
        num = int(input('Ingrese un número: '))

