# Loops Bucles For While


# Armado de un bucle sencillo for
for i in range(5):
    print(f"El valor del bucle es: {i}.")
# decreasing for
for n in range (1,0, -1):
    print(n)

# Armado de un bucle del 5 al 10 for
for i in range(5, 10):
    print(f"El valor del bucle es: {i}.")

print(f"El bucle de arriba va del 0 al 4 y el segundo bucle va del 5 al 10.")
print(f"Entre los dos bucles de arriba se va del 0 al 0. 10 elementos en total.\n\n")

# Bucle sencillo con saltos de a 3 for
for i in range(1, 10, 3):
    print(f"El valor del bucle es: {i}.")

print(f"El bucle de arriba va del 1 al 10 salntando de a 3, llegando solo hasta el 7.")
print(f"Los saltos son 1, 4, 7. El siguiente daría 10 y NO lo incluye!.\n\n")

# Bucle sencillo con saltos de a -2 for
for i in range(10, 4, -2):
    print(f"El valor del bucle es: {i}.")

print(f"El bucle de arriba va del 10 al 4 saltando de a -2, llegando solo hasta el 6.")
print(f"Los saltos son 10, 8, 6. El siguiente daría 4 pero NO lo incluye!.\n\n")

# Bucles con elementos de una lista for
colores = ["rojo", "azul", "verde", "amarillo"]
print(f"La lista de colores es: {colores}.\n")
print("Listado de colores con bucle for:")
for color in colores:
    print(color)

print(f"\n\n")

# Creación de un bucle sencillo while
i = 0
while i <= 10:
    print(f"El valor del bucle es: {i}.")
    i+= 1
print(f"El bucle de arriba va del 0 al 10.\n\n")

# Creación de un bucle hasta romperlo
while True: 
    salida = input("Introduce 'salir' para finalizar el bucle while True por favor: ")
    if salida == 'salir':
        break
print(f"Gracias!\n\n")

