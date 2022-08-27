
nombre = input('¿Ingresa tu nombre con la inicial en mayúsucula? = ')
preferencia = input('¿Cual es tu preferencia, Marvel o Capcom? = ')

if 'A' >= nombre[0] <= 'M' and (preferencia[0] == 'M' or preferencia[0] == 'm'):
    print('Tu grupo es el A Marvel')
elif 'N' <= nombre[0] <= 'Z' and (preferencia[0] == 'C' or preferencia[0] == 'c'):
    print('Tu grupo es el A Capcom')  
else:
    print('Tu grupo es el B')