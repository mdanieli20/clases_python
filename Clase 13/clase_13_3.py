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


# class FordK:
    
#     def __init__(self, color, puertas):
#         self.color = color
#         self.puertas = puertas
        
#     def tocar_bocina(self):
#         print('Pi pi!!')
    
#     def describir_auto(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'
    

# # auto1 = FordK.__init__('Negro', 4)
# auto1 = FordK('Negro', 4)
# auto2 = FordK('Rojo', 2)

# # print(auto1)
# # print(f'Color {auto1.color}')
# # print(f'Cant puertas {auto1.puertas}')
# # auto1.tocar_bocina()
# print(auto1.describir_auto())

# # print(auto2)
# # print(f'Color {auto2.color}')
# # print(f'Cant puertas {auto2.puertas}')
# # auto2.tocar_bocina()
# print(auto2.describir_auto())

# ======================================================
# ======================================================

# Valores por defecto

# class FordK:
    
#     def __init__(self, color='Verde', puertas=5):
#         self.color = color
#         self.puertas = puertas
        
#     def tocar_bocina(self):
#         print('Pi pi!!')
    
#     def describir_auto(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'
    

# auto1 = FordK('Negro', 4)
# auto2 = FordK('Rojo', 2)
# auto3 = FordK(puertas=2)
# auto4 = FordK('Rojo')
# auto5 = FordK()

# print(auto1.color, auto1.puertas)
# print(auto2.color, auto2.puertas)
# print(auto3.color, auto3.puertas)
# print(auto4.color, auto4.puertas)
# print(auto5.color, auto5.puertas)

# *args, **kwargs en constructor


# print(type(auto1))
# print(type(auto2))

# ======================================================
# ======================================================

# Atributo de clase

# class FordK:
  
#     cant_ruedas = 4
    
#     def __init__(self, color='Verde', puertas=5):
#         self.color = color
#         self.puertas = puertas
        
#     def tocar_bocina(self):
#         print('Pi pi!!')
    
#     def describir_auto(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'


# auto1 = FordK('Negro', 4)
# auto2 = FordK('Rojo', 2)
# auto3 = FordK(puertas=2)
# auto4 = FordK('Rojo')
# auto5 = FordK()

# print(auto1.color, auto1.puertas, auto1.cant_ruedas)
# print(auto2.color, auto2.puertas, auto1.cant_ruedas)
# print(auto3.color, auto3.puertas, auto1.cant_ruedas)
# print(auto4.color, auto4.puertas, auto1.cant_ruedas)
# print(auto5.color, auto5.puertas, auto1.cant_ruedas)

# print(type(auto1))
# print(type(auto2))

# print(FordK.cant_ruedas)
# print(FordK.color)

# ======================================================
# ======================================================

# Metodos

# class FordK:
  
#     cant_ruedas = 4
    
#     def __init__(self, color='Verde', puertas=5):
#         self.color = color
#         self.puertas = puertas
#         self.metros_recorridos = 0
#         self.fabricar()
        
#     def tocar_bocina(self):
#         print('Pi pi!!')
#         # self.toco_bocina = True
    
#     def describir_auto(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'

#     def fabricar(self):
#         print(f'Se fabrico un Ford K {self.color} de {self.puertas} puertas.')
        
#     def avanzar(self, metros):
#         print(f'el auto avanzo {metros} metros')
#         self.metros_recorridos += metros


# auto1 = FordK('Negro', 4)
# print(auto1.toco_bocina)
# auto1.tocar_bocina()
# print(auto1.toco_bocina)
# auto1.fabricar()

# auto2 = FordK(puertas=2)
# auto2.fabricar()

# print(auto1)
# print(auto1.color, auto1.puertas, auto1.cant_ruedas)
# auto1.tocar_bocina()
# print(auto1.describir_auto())
# print(auto1.metros_recorridos)
# auto1.avanzar(150)
# print(auto1.metros_recorridos)

# print(auto2)
# print(auto2.color, auto2.puertas, auto1.cant_ruedas)
# auto2.tocar_bocina()
# print(auto2.describir_auto())
# print(auto2.metros_recorridos)
# auto2.avanzar(32)
# print(auto2.metros_recorridos)

# ======================================================
# ======================================================

# Ej 1: Mi primera clase (10min)
'''
Crear una clase para trabajar con una Persona. 
Agregarle 3 atributos de instancia, el constructor y dos métodos. 

Luego instanciar a dos personas.
'''

# ======================================================
# ======================================================


# Metodos especiales (Magic methods)
class Motor:
    def __init__(self, valvulas):
        self.valvulas = valvulas
    
    def __str__(self):
        return f'Este motor es de {self.valvulas} valvulas.'
    
motor = Motor(12)
# print(motor)

class FordK:
  
    cant_ruedas = 4
    
    def __init__(self, color='Verde', puertas=5):
        self.color = color
        self.puertas = puertas
        self.metros_recorridos = 0
        self.fabricar()
    
    def __str__(self):
        return f'Ford K -> puertas: {self.puertas}, color: {self.color}'
        
    def tocar_bocina(self):
        print('Pi pi!!')
    
    def describir_auto(self):
        return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'

    def fabricar(self):
        print(f'Se fabrico un Ford K {self.color} de {self.puertas} puertas.')
        
    def avanzar(self, metros):
        print(f'el auto avanzo {metros} metros')
        self.metros_recorridos += metros


auto1 = FordK('Negro', 4)
# print(auto1)
auto2 = FordK('Negro')

# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1.describir_auto())

# ======================================================
# ======================================================

# class Concesionaria:
    
#     def __init__(self, concesionaria):
#         self.concesionaria = concesionaria
#         self.autos = []
        
#     def __str__(self):
#         return f'Listado de autos en la consecionaria "{self.concesionaria}"'
        
#     def __len__(self):
#         return len(self.autos)
    
#     def agregar_auto(self, auto):
#         if auto:
#             self.autos.append(auto)
#         else:
#             print('Te falto el auto.')

# concesionaria = Concesionaria('Gimenez')
# print(concesionaria)
# print(len(concesionaria))
# concesionaria.agregar_auto(auto1)
# print(len(concesionaria))

# ======================================================
# ======================================================

# class Concesionaria:
    
#     def __init__(self, concesionaria):
#         self.concesionaria = concesionaria
#         self.autos = []
        
#     def __str__(self):
#         return f'Listado de autos en la consecionaria "{self.concesionaria}"'
        
#     def __len__(self):
#         return len(self.autos)
    
#     def agregar_auto(self, auto):
#         if auto:
#             self.autos.append(auto)
#         else:
#             print('Te falto el auto.')
        
#     def __getitem__(self, posicion):
#         try:
#             return self.autos[posicion]
#         except:
#             return 'No se encontro ese auto'

# concesionaria = Concesionaria('Gimenez')
# print(concesionaria)
# concesionaria.agregar_auto(auto1)
# print(concesionaria[0])


# ======================================================
# ======================================================

# class Concesionaria:
    
#     def __init__(self, concesionaria):
#         self.concesionaria = concesionaria
#         self.autos = []
        
#     def __str__(self):
#         return f'Listado de autos en la consecionaria "{self.concesionaria}"'
        
#     def __len__(self):
#         return len(self.autos)
    
#     def agregar_auto(self, auto):
#         if auto and auto.color == 'Negro':
#             self.autos.append(auto)
#         else:
#             print('Te falto el auto de color negro.')
        
#     def __getitem__(self, posicion):
#         try:
#             return self.autos[posicion]
#         except:
#             return 'No se encontro ese auto'
        
#     def __setitem__(self, posicion, nuevo_auto):
#         try:
#             if nuevo_auto.color == 'Negro':
#                 self.autos[posicion] = nuevo_auto
#             else:
#                 print('El auto no es negro.')
#         except:
#             print('No se pudo modificar el auto de la posicion {posicion}.')


# concesionaria = Concesionaria('Gimenez')
# print(concesionaria)
# concesionaria.agregar_auto(auto1)
# print(concesionaria[0])
# concesionaria[0] = auto2
# print(concesionaria[0])

# ======================================================
# ======================================================

class Concesionaria:
    
    def __init__(self, concesionaria):
        self.concesionaria = concesionaria
        self.autos = []
        
    def __str__(self):
        return f'Listado de autos en la consecionaria "{self.concesionaria}"'
        
    def __len__(self):
        return len(self.autos)
    
    def agregar_auto(self, auto):
        if auto and auto.color == 'Negro':
            self.autos.append(auto)
        else:
            print('Te falto el auto de color negro.')
        
    def __getitem__(self, posicion):
        try:
            return self.autos[posicion]
        except:
            return 'No se encontro ese auto'
        
    def __setitem__(self, posicion, nuevo_auto):
        try:
            if nuevo_auto.color == 'Negro':
                self.autos[posicion] = nuevo_auto
            else:
                print('El auto no es negro.')
        except:
            print('No se pudo modificar el auto de la posicion {posicion}.')
        
    def __iter__(self):
        for auto in self.autos:
            yield auto

concesionaria = Concesionaria('Gimenez')
print(concesionaria)
concesionaria.agregar_auto(auto1)
concesionaria.agregar_auto(auto2)

for valor in [1,2,3,4]:
    print(valor)
    
for valor in concesionaria:
    print(valor)


# ======================================================
# ======================================================


# Encapsulamiento

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
