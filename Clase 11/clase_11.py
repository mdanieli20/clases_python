
# type().__name__

# print(5)
# print(type(5))
# print(type(5).__name__)
# print(type(5).__name__ == 'int')
# print(type(5) == int)
# print(type(5.5).__name__ == 'float')
# print(type('5.5').__name__ == 'str')


# ================================================================================
# ================================================================================


# Errores de sintaxis
# print('pepe)
# print('pepe'))
# prnt('pepe')
# print('ricardo
# pepe'))

# if True
#     print('ea ea')
    
# def funcion()
#     print(1)

# ================================================================================
# ================================================================================

# Errores semanticos
# lista = []
# lista.pop()

# print(int(input('Ingrese un numero')))

# ================================================================================
# ================================================================================

# Ej 1
# def dividir(a, b):
#     return a/b

# a y b son numeros por definicion


# def dividir(a, b):
#     if b == 0:
#         return None
#     return a/b

# def dividir(a, b):
#     if b != 0:
#         return a/b

# dividir(5, 0)


# ================================================================================
# ================================================================================

# break

# ================================================================================
# ================================================================================

# Excepciones
# https://docs.python.org/es/3/library/exceptions.html

# ================================================================================
# ================================================================================

# try - except

# def dividir(a, b):
#     try:
#         return a/b
#     except:
#         return 'No se puede dividir por 0.'

# print(dividir(5,1))
# print(dividir(5,0))
# print(dividir('5',0))

# valor = 15
# print(valor)
# try:
#     valor*=15
#     print(valor)
#     valor+=15
#     print(valor)
#     valor/=0
#     print(valor)
#     valor-=5
#     print(valor)
#     valor*=15
#     print(valor)
# except:
#     # ... # pass
#     print('Se genero un error.')
    
# ================================================================================
# ================================================================================

# else

# def dividir(a, b):
#     try:
#         valor = a/b
#     except:
#         print('No se puede dividir por 0.')
#     else:
#         print(f'La division dio como resultado {valor}.')

# dividir(5, 0)
# # dividir(5,1)


# def dividir(a, b, c):
#     try:
#         valor = a/b
#         # valor /= c
#     except:
#         print('No se puede dividir por 0.')
#     else:
#         print(f'La division dio como resultado {valor}.')
#         valor /= c

# try:
#     dividir(5, 1, 'c')
#     # dividir(5,1, 5)
# except:
#     print('Hubo un error en algo de todo esto.')



# def dividir(a, b):
#     try:
#         valor = a/b
#     except:
#         print('No se puede dividir por 0.')
#         # return 'No se puede dividir por 0.'
#     else:
#         print(f'La division dio como resultado {valor}.')
#         # return f'La division dio como resultado {valor}.'

# # print(dividir(5,0))
# dividir(5,0)
# dividir(5,1)


# while(True):
#     try:
#         n = input("Introduce un número: ")
#         m = 4
#         if n == 'n':
#             break  # Importante romper la iteración si todo ha salido bien
#         else:
#             n = float(n)
#         print(f"{n}/{m} = {n/m}")
#     except:
#         print("Ha ocurrido un error, introduce bien el número")
#     else:
#         print("Todo ha funcionado correctamente")
#         break  # Importante romper la iteración si todo ha salido bien

# ================================================================================
# ================================================================================

# finally

# def dividir(a, b):
#     try:
#         valor = a/b
#     except:
#         print('No se puede dividir por 0.')
#         # return 'No se puede dividir por 0.'
#     else:
#         print(f'La division dio como resultado {valor}.')
#         # return f'La division dio como resultado {valor}.'
#     finally:
#         print('Yo te paso por aca si te fue bien en la cuenta o si te fue mal, no me importa nada')

# dividir(5, 0)
# dividir(5, 1)
# print(dividir(5,0))
# print(dividir(5,1))


# f = open('clase_8/test.txt', 'w')
# try:
#     f.write('probando')
#     5/0
#     print('try')
#     # f.close()
# except:
#     print('except')
#     # f.close()
# else:
#     print('else')
#     # f.close()
# finally:
#     f.close()


# ================================================================================
# ================================================================================

# Excepciones multiples


# def dividir(a, b, c):
def dividir(a, b):
    try:
        valor = a/b
        print(valor)
    # except ArithmeticError:
    #     print('paso por el arithmetic')
    except ZeroDivisionError:
        print('No se puede dividir por 0.')
    # except TypeError:
    #     print('No funciona si me pasas strings')
    except Exception as error:
        print(error)
        print('soy el exception de adcentro de la funcion')
    else:
        print(f'La division dio como resultado {valor}.')
        # valor /= c

# dividir(5,1)
# dividir(5,0)
# dividir(5,'c')

try:
    # dividir(5,1)
    # dividir(5, 0)
    dividir(5, 'c')
    # dividir(5, 2, 0)
except Exception:
    print('soy el exception de afuera')




# def dividir(a, b):
#     try:
#         valor = a/b
#     except Exception as error:
#         return f'{type(error).__name__}: {error}'
        # return 'No se puede dividir por 0.'
    # else:
    #     return f'La division dio como resultado {valor}.'
    # finally:
    #     print('Yo te paso por aca si te fue bien en la cuenta o si te fue mal, no me importa nada')

# print(dividir(5,input('Ingrese un numero:')))
# print('pepe')

# ================================================================================
# ================================================================================

# def dividir(a, b):
#     try:
#         valor = a/b
#     except TypeError:
#         print("No se puede dividir el número entre una cadena")
#     except ValueError:
#         print("Debes introducir una cadena que sea un número")
#     except ZeroDivisionError:
#         print("No se puede dividir por cero, prueba otro número")
#     except Exception as e:
#         print("Ha ocurrido un error no previsto", type(e).__name__ )
#     else:
#         print(f'La division dio como resultado {valor}.')
#     finally:
#         print('Yo te paso por aca si te fue bien en la cuenta o si te fue mal, no me importa nada')

# dividir(5,'0')

# ================================================================================
# ================================================================================

# def dividir(a, b):
#     try:
#         valor = a/b
#     except ZeroDivisionError:
#         print("No se puede dividir por cero, prueba otro número")
#     # except TypeError:
#     #     print("No se puede dividir el número entre una cadena")
#     else:
#         print(f'La division dio como resultado {valor}.')
#     finally:
#         print('Yo te paso por aca si te fue bien en la cuenta o si te fue mal, no me importa nada')


# try:
#     dividir(5,'0')
# except Exception as e:
#     print("Ha ocurrido un error no previsto", type(e).__name__ )
# except:
#     print('pase por el except de arafue')
