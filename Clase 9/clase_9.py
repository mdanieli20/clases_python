var= 'Hola'
def contar_letras(texto):
    cant_letras = 0
    for letra in texto:
        cant_letras += 1
    return cant_letras

print(len('Hola'))
print(contar_letras('Hola'))
print(contar_letras(var))

