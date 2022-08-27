
# Desafio - Año Bisiesto

# >> Consigna: Realizar una función llamada año_bisiesto:

# Recibirá un año por parámetro
# Imprimirá “El año año es bisiesto” si el año es bisiesto
# Imprimirá “El año año no es bisiesto” si el año no es bisiesto
# Si se ingresa algo que no sea número debe indicar que se ingrese un número.

# >>Información a tener en cuenta al realizar el entregable:

# Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. 
# Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.

def año_bisiesto(año):
    for var in año:
        if var in '0123456789':
            continue
        else:
            print('Solo acepto numeros.')
            return True
    
    if int(año) % 4 == 0 and (int(año) % 100 != 0 or int(año) % 400 == 0):
        print('El año ingresado es bisiesto')
    else:
        print('El año ingresado no es bisiesto')
    return False


error = True
while error:
    error = año_bisiesto(input('ingresar año: '))
