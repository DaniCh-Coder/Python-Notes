# list-comprehension - lista de compresión
# formato: [acción] en [rango]

# Generar números con una lista de comprensión
# formato [número] en [rango 0-9]
numeros = [i for i in range(10)] # to generate the nombes form 0 to 9
print(numeros)

# Generar números cuadrados
# formato: [acción] en [rango]
# formato [cuadrado de un numero i] en [rango de 0 a 9]
num_cuad = [i*i for i in range(10)]
print(num_cuad)

# Generar coordenadas (ejemplo (x, y))
# Generar pares de numeros en una lista de tuplas
# formato: [acción] en [rango]
# formato: [(i, i*i)] en [rango de 0 a 9]
coordenadas = [(i, i *i) for i in range(10)]
print(coordenadas)

# Generar listas con condiciones
# formato: [acción] en [rango] si [condición] 

# Generar numeros impares
# formato: [número] en [rango de 0 a 9] si [es impar] 
impares = [ i for i in range(10) if i % 2 != 0]
print(impares)

# Aplanar un array tridimensional - matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista = [ number for row in matriz for number in row]
print(lista)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

