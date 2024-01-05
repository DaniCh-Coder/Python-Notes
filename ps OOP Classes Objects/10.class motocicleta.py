# Class motocicleta

class Motocicleta():
    # atributos de clase
    estado = "nueva"
    motor = False
    
    # metodos
    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, 
                 modelo, fecha_fabricación, velocidad_final, peso):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricación = fecha_fabricación
        self.velocidad_final = velocidad_final
        self.peso = peso
    
    def arrancar(self):
        if self.motor:
            print("El motor ya está en marcha.")
        else:
            print("El motor se arranca ahora")
            self.motor = True
    
    def detener(self):
        if self.motor:
            print("Se detiene el motor.")
            self.motor = False
        else:
            print("El motor ya está apagado")

moto1 = Motocicleta("Roja y blanca","45663-FHDY", 10, 2, "Yamaha", "Z1100", "20/05/2020", 310, 199)
print(moto1)

moto2 = Motocicleta(matricula="39475-FIYQI", 
                    peso=178, 
                    color= "verde y azul", 
                    marca="Harley Davison", 
                    modelo="Fat Boy", 
                    numero_ruedas=2, 
                    fecha_fabricación="30/07/2019", 
                    velocidad_final=180,
                    combustible_litros=0
                    )
print(moto2)

moto1.arrancar()
moto2.detener()
moto1.detener()
moto2.arrancar()

moto1.precio = 33000
print(f"El precio de la moto {moto1.marca} es: USD{moto1.precio}.")