# Herencia

# class NombreClase:
#     ...

# class Vehiculo():
#     pass

# class Auto(Vehiculo):
#     pass

# DRY
# class Auto():
#     def __init__(self, marca):
#         self.marca = marca

#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# class Moto():
#     def __init__(self, marca):
#         self.marca = marca

#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# auto = Auto('Ford')
# print(auto.marca)
# auto.descripcion()
# moto = Moto('Mercedes')
# print(moto.marca)
# moto.descripcion()

# class Vehiculo():
#     def __init__(self, marca):
#         self.marca = marca

#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# class Auto(Vehiculo):
#     ...

# class Moto(Vehiculo):
#     ...
    
# class Lancha(Vehiculo):
#     ...

# vehiculo = Vehiculo('Scania')
# print(vehiculo.marca)
# vehiculo.descripcion()
# auto = Auto()
# auto = Auto('Ford')
# print(auto.marca)
# auto.descripcion()
# moto = Moto('BMW')
# print(moto.marca)
# moto.descripcion()
# lancha = Lancha('Mercedes')
# print(lancha.marca)
# lancha.descripcion()

# ======================================================
# ======================================================

# Agregar a las particularidades heredadas

# class Vehiculo():
#     def __init__(self, marca):
#         self.marca = marca

#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# class Auto(Vehiculo):
#     ...
    
# class Lancha(Vehiculo):
#     def anclarse(self):
#         print(f'Anclaje efectuado')

# auto = Auto('Ford')
# print(auto.marca)
# auto.descripcion()
# lancha = Lancha('Mercedes')
# print(lancha.marca)
# lancha.descripcion()
# lancha.anclarse()
# auto.anclarse()

# ======================================================
# ======================================================

# super()

# class Vehiculo():
#     def __init__(self, marca):
#         self.marca = marca
        
#     def arrancar(self):
#         print('Prrrrumm!')
        
#     def avanzar(self, distancia):
#         ...
        
#     def tocar_bocina(self):
#         ...
        
#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# # Uso de *args, **kwargs
# class Auto(Vehiculo):
#     # Forma 1
#     # def __init__(self, color, asientos, marca):
#     #     self.color = color
#     #     self.asientos = asientos
#     #     self.marca = marca
#     # Forma 2
#     def __init__(self, color, asientos, marca):
#         super().__init__(marca)
#         self.color = color
#         self.asientos = asientos
#         self.arrancar()
    
#     def descripcion(self):
#         super().descripcion()
#         print(f'Soy un {type(self).__name__}')

# class Moto(Vehiculo):
#     pass

# auto = Auto('Negro', 4, 'Ford')
# print(auto.marca)
# auto.descripcion()
# moto = Moto('BMW')
# print(moto.marca)
# moto.descripcion()

# print(auto.marca, auto.color, , auto.asientos)
# print(moto.marca, moto.color, , moto.asientos)

# ======================================================
# ======================================================

# BREAK

# ======================================================
# ======================================================


# Herencia multiple (mostrar para pensar)

# class Vehiculo():
#     def __init__(self, marca):
#         self.marca = marca

#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# class VehiculoTerrestre(Vehiculo):
#     def __init__(self, ruedas, cant_ruedas, marca):
#         super().__init__(marca)
#     # def __init__(self, ruedas, cant_ruedas, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#         self.ruedas = ruedas
#         self.cant_ruedas = cant_ruedas

# class Auto(VehiculoTerrestre):
#     ...

# class Lancha(Vehiculo):
#     ...

# # auto = Auto(True, 4, marca='Ford')
# auto = Auto(ruedas=True, cant_ruedas=4, marca='Ford')
# print(auto.marca, auto.ruedas, auto.cant_ruedas)
# auto.descripcion()
# lancha = Lancha('Mercedes')
# print(lancha.marca)

# ======================================================
# ======================================================


# class Animal:
#     def descripcion(self):
#         # print('Soy lo que soy')
#         return 'Soy un animal'
    
# class Mamifero(Animal):
#     ...
    
# class Terrestre:
#     def trotar(self):
#         print(f'{type(self).__name__} trotando')
        
#     def descripcion(self):        
#         return 'Soy terrestre'


# class Acuatico:
#     def nadar(self):
#         print(f'{type(self).__name__} nadando')
        
#     def descripcion(self):
#         return 'Soy acuatico'
    
# class Gato(Mamifero, Terrestre):
#     # def descripcion(self):        
#     #     return 'Soy un gato'
#     ...
    
# class Delfin(Acuatico, Mamifero):
#     ...

# gato = Gato()
# delfin = Delfin()
# print(gato.descripcion())
# gato.trotar()
# delfin.descripcion()
# delfin.trotar()
# delfin.nadar()
# print(gato.descripcion())
# print(delfin.descripcion())

# MRO

# print(Gato.__mro__)

# ======================================================
# ======================================================


# Duck Typing ( leanlo pra tenerlo en cuenta )

# ======================================================
# ======================================================


# Polimorfismo

class Animal:
    def caminar(self):
        print('Soy un animal caminando')

class Perro(Animal):
    def caminar(self):
        print('El perro esta caminando.')
    
class Gato(Animal):
    def caminar(self):
        print('Soy un gato que anda caminando por la calle')
    
class Chancho(Animal):
    ...


def animal_caminando(animal):
    animal.caminar()

perro = Perro()
gato = Gato()
chancho = Chancho()


for animal in [perro, gato, chancho]:
    animal_caminando(animal)