# https://www.seas.es/blog/informatica/agregacion-vs-composicion-en-diagramas-de-clases-uml/
# Slides

# Definiendo e instanciar una clase
'''
class Auto:
    ... # pass
    
auto1 = Auto()
auto2 = Auto()
'''

# def funcion():
#     return 'valor'

# valor = funcion()
# print(valor)

# class ClaseAuto: # PascalCase
#     ...

# auto1 = ClaseAuto()
# auto2 = ClaseAuto()

# print(funcion)
# print(ClaseAuto)
# print(auto1)
# print(auto2)

# Atributos

# De instancia
'''
class Auto:
    
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca
'''

# class FordK:
    
#     def __init__(self, color, puertas):
#         self.color = color
#         self.puertas = puertas

# # auto1 = FordK()
# # auto2 = FordK()
# auto1 = FordK('Negro', 4)
# auto2 = FordK('Rojo', 2)

# print(auto1)
# print(f'Color {auto1.color}')
# print(f'Cant puertas {auto1.puertas}')
# print(auto2)
# print(f'Color {auto2.color}')
# print(f'Cant puertas {auto2.puertas}')


class FordK:
    
    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas
        
    def tocar_bocina(self):
        print('Pi pi!!')
    
    def describir_auto(self):
        return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'
    

# auto1 = FordK()
# auto2 = FordK()
auto1 = FordK('Negro', 4)
auto2 = FordK('Rojo', 2)

# print(auto1)
# print(f'Color {auto1.color}')
# print(f'Cant puertas {auto1.puertas}')
# auto1.tocar_bocina()
print(auto1.describir_auto())

# print(auto2)
# print(f'Color {auto2.color}')
# print(f'Cant puertas {auto2.puertas}')
# auto2.tocar_bocina()
print(auto2.describir_auto())



# class ClaseAuto:

#     def __init__(self, modelo='uno', marca='fiat'):
#         self.modelo = modelo
#         self.marca = marca
        

# auto1 = ClaseAuto()
# auto2 = ClaseAuto('k', 'ford')
# auto3 = ClaseAuto(modelo='siena', marca='fiat')
# auto_prueba = ClaseAuto()

# print(auto1.marca, auto1.modelo)
# print(auto2.marca, auto2.modelo)
# print(auto3.marca, auto3.modelo)
# print(auto_prueba.marca, auto_prueba.modelo)


# print(type(auto1))
# print(type(auto2))

# y self? que es self?

# De clase
'''
class Auto:
    
    uso = 'familiar'
    
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca
'''
# class ClaseAuto:
    
#     uso = 'familiar'
#     cant_ruedas = 4
    
#     def __init__(self, modelo, marca):
#         self.modelo = modelo
#         self.marca = marca

# auto1 = ClaseAuto('uno', 'fiat')
# auto2 = ClaseAuto('k', 'ford')
# auto3 = ClaseAuto('up', 'volkswagen')

# print(auto1.marca, auto1.uso, auto1.cant_ruedas)
# print(auto2.marca, auto2.uso, auto2.cant_ruedas)
# print(auto3.marca, auto3.uso, auto3.cant_ruedas)

# Metodos

'''
class Auto:
    
    uso = 'familiar'
    
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca
        self.fabricar()

    def fabricar(self):
        print(f'Se fabrico un {self.marca} {self.modelo})
        
    def arrancar(self):
        print('Prrrrum')
        
    def avanzar(metros):
        print(f'el auto avanzo {metros} metros')
'''
# class ClaseAuto:
    
#     uso = 'familiar'
    
#     def __init__(self, modelo, marca):
#         self.modelo = modelo
#         self.marca = marca
#         self.ubicacion = [0,0]
#         self.fabricar()

#     def fabricar(self):
#         print(f'Se fabrico un {self.marca} {self.modelo}')
        
#     def arrancar(self):
#         print('Prrrrum')
        
#     def avanzar(self, metros):
#         print(f'el auto avanzo {metros} metros')
#         self.ubicacion[0] += 15

# auto1 = ClaseAuto('uno', 'fiat')
# auto2 = ClaseAuto('k', 'ford')
# auto3 = ClaseAuto('up', 'volkswagen')

# print(auto1.marca, auto1.uso)
# auto1.arrancar()
# auto1.avanzar(15)
# auto1.fabricar()
# print(auto2.marca, auto2.uso)
# print(auto3.marca, auto3.uso)

# Ej 1: Mi primera clase (10min)
'''
Crear una clase para trabajar con una Persona. 
Agregarle 3 atributos de instancia, el constructor y dos métodos. 

Luego instanciar a dos personas.
'''

# Metodos especiales (Magic methods)
# class Motor:
#     def __init__(self, valvulas):
#         self.valvulas = valvulas
    
#     def __str__(self):
#         return f'Este motor es de {self.valvulas} valvulas.'
    
# motor12 = Motor(12)
# motor6 = Motor(6)
# motor8 = Motor(8)
# # print(motor1)

# class Auto:
    
#     uso = 'familiar'
#     cant_fabricados = 0
    
#     def __init__(self, modelo, marca, motor):
#         Auto.cant_fabricados += 1
#         self.numero_de_fabricacion = self.cant_fabricados
#         self.disponible = False
#         self.modelo = modelo
#         self.marca = marca
#         self.motor = motor
#         self.fabricar()

#     def fabricar(self):
#         # Auto.uso = 'ejecutivo'
#         print(f'Se fabrico un {self.marca} {self.modelo} {self.uso}')
        
#     def arrancar(self):
#         print('Prrrrum')
        
#     def avanzar(metros):
#         print(f'el auto avanzo {metros} metros')

# print(Auto.cant_fabricados)
# auto1 = Auto('falcon', 'ford', motor8)
# print(auto1.numero_de_fabricacion)
# print(Auto.cant_fabricados)
# auto2 = Auto('uno', 'fiat', motor6)
# print(auto2.numero_de_fabricacion)
# print(Auto.cant_fabricados)
# print(auto1.numero_de_fabricacion)


# class AutosEnConcesionaria:
    
#     def __init__(self, concesionaria):
#         self.concesionaria = concesionaria
#         self.autos = []
    
#     def agregar_auto(self, auto):
#         if auto:
#             self.autos.append(auto)
#         else:
#             print('Te falto el auto.')
        
#     def __str__(self):
#         return f'Listado de autos en la consecionaria "{self.concesionaria}"'
        
#     def __len__(self):
#         return len(self.autos)
        
#     def __getitem__(self, posicion):
#         for auto in self.autos:
#             if auto.numero_de_fabricacion == posicion:
#                 return auto
#         else:
#             print('No existe ese auto.')
        
#     def __setitem__(self, posicion, nuevo_auto):
#         for indice, auto in enumerate(self.autos):
#             if auto.numero_de_fabricacion == posicion:
#                 self.autos[indice] = nuevo_auto
#                 return
#         else:
#             print('No existe ese auto.')
        
#     def __iter__(self):
#         for auto in self.autos:
#             yield auto

# autos_concesionaria = AutosEnConcesionaria('Fort')

# ejemplo str
# print(autos_concesionaria)

# ejemplo len
# print(len(autos_concesionaria))
# autos_concesionaria.agregar_auto(auto1)
# autos_concesionaria.agregar_auto(auto2)
# print(len(autos_concesionaria))

# ejemplo getitem
# lista = [1,2,3]
# lista[1]

# print(autos_concesionaria[2])

# ejemplo setitem
# lista = [1,2,3]
# lista[1] = 5

# autos_concesionaria[1] = auto2
# print(autos_concesionaria[2])

# ejemplo iter
# for auto in autos_concesionaria:
#     print(auto)


# class Auto:
#     def __init__(self, modelo, marca, patente):
#         self.modelo = modelo
#         self._marca = marca
#         self.__patente = patente
        
#     def get_patente(self):
#         if self._marca == 'fiat':
#             return self.__patente
#         else:
#             return 'no se puede mostrar, estas limitado'
        
#     def set_patente(self, nuevo_valor):
#         if self._marca == 'fiat':
#             self.__patente = nuevo_valor
#         else:
#             print('no se puede mostrar, estas limitado')
        

# auto1 = Auto('uno', 'fiat', 'asd 123')
# auto1 = Auto('uno', 'ford', 'asd 123')
# print(auto1.modelo)
# print(auto1._marca)
# print(auto1.__patente)
# print(auto1._Auto__patente)
# print(auto1.get_patente())
# print(auto1.set_patente('qwe 456'))
# print(auto1.get_patente())
