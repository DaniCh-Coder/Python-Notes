# Creación de una clase Rocket
"""
Class Rocket Excercise.
First version of the class. The simplest.
"""
from math import sqrt


class Rocket:
    """Cohete o nave espacial para una simulación de física"""
    def __init__(self):
        """ Posición x, y de cada cohete"""
        self.x = 0
        self.y = 0
    def move_up(self):
        """Move rocket up one point"""
        self.y += 1
    

# Creación de un objeto de clase Rocket. El objeto es rk.
rk = Rocket()

# Mover el objeto rk para arriba
rk.move_up()
print(f'La función "{rk.move_up}" movió el objeto hacia arriba: {rk.y}.')
print(f"Posición (x, y) del cohete: {rk.x, rk.y}.\n")

# Crear una flota de cohetes
flota_cohetes = []
for x in range(0, 5):
    nuevo_cohete = Rocket()
    flota_cohetes.append(nuevo_cohete)

# Armar la list directamente
flota_cohetes = [Rocket() for x in range(0,5)]

# Cada cohete es un objeto con una dirección distinta
for cohete in flota_cohetes:
    print(cohete)

# Creación de una clase Rocket, mejora 1
"""
Class Rocket Excercise.
Segunda versión. Whith optional arguments.
"""
class Rocket:
    """Cohete o nave espacial para una simulación de física"""
    def __init__(self, x=0, y=0):
        """ Posición x, y de cada cohete"""
        self.x = x
        self.y = y
    def move(self, x=0, y=0):
        """Mueve el cohete hacia otro lado"""
        self.x += x
        self.y += y

# Creación de un objeto de clase Rocket. El objeto es rk.
rk = Rocket(0, 100)

# Mover el objeto rk para arriba una posición
rk.move()
print(f'La función "{rk.move}" movió el objeto hacia arriba: {rk.y}.')
print(f"Posición (x, y) del cohete: {rk.x, rk.y}.\n")

# Creo una flota de 3 cohetes
flota_cohetes = [Rocket() for x in range(3)]

# Posiciones iniciales de los cohetes
for cohete in flota_cohetes:
    print(f"{cohete.x, cohete.y}")

for x, cohete in enumerate(flota_cohetes):
    cohete.x = x
    cohete.y = x

# Posiciones iniciales en diagonal
for cohete in flota_cohetes:
    print(f"{cohete.x, cohete.y}")

# Creación de una clase Rocket, mejora 2
"""
Class Rocket Excercise.
Tercera versión of the class. Distancia entre naves.
"""
class Rocket:
    """Cohete o nave espacial para una simulación de física"""
    def __init__(self, x=0, y=0):
        """ Posición x, y de cada cohete"""
        self.x = x
        self.y = y

    def move(self, x=0, y=0):
        """Mueve el cohete hacia arriba 1 punto"""
        self.x += x
        self.y += y
    def distancia(self, otra):
        """Calcula la distancia"""
        return sqrt((self.x - otra.x)**2 + (self.y - otra.y)**2)

# Crea dos cohetes 
cohete_1 = Rocket()
cohete_2 = Rocket(10, 5)

# Calcula la distancia entre cohetes
distancia = round(cohete_1.distancia(cohete_2), 2)
print(f"Los cohetes están a {distancia} puntos de distancia.")