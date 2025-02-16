# funciones lambda o anonimas
# no llevan nombre
# solo pueden tener una expresiones
# pueden tener muchos parametros

# Se define una función de manera clásica
def multiplicación(num1, num2):
    return num1* num2

# Se define una función de manera anonima
lambda num1, num2 : num1 * num2

# La función lambda tambien se puede almacenar en una variable
multiplicacion = lambda num1, num2 : num1 * num2

# Uso de la función lamda
print(multiplicacion(1,2))

# la función lambda se puede usar directamente
print((lambda num1, num2 : num1 * num2) (2, 2))

# Una forma de presentar el resultado en la consola dentro de la función
(lambda num1, num2 : print(num1 * num2)) (3, 2)

# 1. calculadora de área de un círculo en dos líneas de código
radio = int(input("Introduca por favor el radio del circulo cuya área quiere calcular: "))
# la funcion lambda sería como sigue
# la función es: lambda radio : 3.1416 * radio * radio
# y su uso es (lambda radio : 3.1416 * radio * radio)(radio)
# Uso directamente la función en la salida de la consola
print(f"El área del circulo es: {(lambda radio : 3.1416 * radio * radio)(radio)}")

# 2. En que lugar está el azul en la lista de colores
colores = ["rojo", "azul", "verde", "amarillo"]
# armando la función lambda paso a paso
# lugar = colores.index("azul")
# (lambda color : colores.index(color))("azul")
(lambda color : print(f"El color está en la posición: {colores.index(color)}."))("azul")
