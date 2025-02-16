# class clases
# Definición e una clase de tipo taza con sus atributos
class Taza():
    color = 'blanco'
    mensaje = None
    material = 'porcelana'
    limpia = True

# Creamos dos objetos de clase Taza
taza1 = Taza()
taza2 = Taza()

# Los objetos se almacenan en la memoria RAM
print(taza1)
print(taza2)

# Los atributos se acceden con puntos
print(taza1.color, taza1.mensaje, taza1.material, taza1.limpia)
print(taza2.color, taza2.mensaje, taza2.material, taza2.limpia)

# Cambio por completo el estado de la taza 2
taza2.color = "rojo"
taza2.material = "vidrio"
taza2.mensaje = "love"
taza2.limpia = False

# Veamos como queda
print("ahora las tazas quedan así...")
print(taza1.color, taza1.mensaje, taza1.material, taza1.limpia)
print(taza2.color, taza2.mensaje, taza2.material, taza2.limpia)

