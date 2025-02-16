# Listas - List
# Las listas son con corchetes
# Armado de listas - Creating List
lista_colores = ["rojo", "azul", "verde", "amarillo"]
lista_numeros = [10, 45, 55, 76]

# Direcciono primer elemnto de la lista
lis_col = lista_colores[0]
print(f"El primer elemento de la lista colores es: {lis_col}")
lis_num = lista_numeros[0]
print(f"El primer elemento de la lista numeros es: {lis_num}.\n")

# Busco un elemento del primer elemento de la lista
elemento_j = lista_colores[0][2]
print(f"El elemento [0][2] de la lista de colores es {elemento_j}.\n")

# error: print(f"El elemento [0][2] de la lista de numeros es {lista_numeros[0][1]}.\n")
# ojo int is not suscriptable

print(f"El segundo elemento de la lista es: {lista_colores[1]}")
print(f"La jota dentro de rojo la ubico de la siguiente manera: {lista_colores[0][2]}")

# Para acceder de manra inversa utiliza el signo menos
print(f"El ultimo elmento de la lista es: {lista_colores[-1]}")

# Sustitución de elementos de listas
# Sustituyo azul por naranja
lista_colores[1] = "naranja"
print(f"Ahora el segundo elemento de la lista es: {lista_colores[1]}")

# Agregado de elementos en una lista
lista_colores.append("azul")
print(f"Agrego azul. Ahora la lista queda: {lista_colores}")

# Insertar elementos en una lista
lista_colores.insert(2, "violeta")
print(f"Inserto 'violeta' en tercer lugar. Ahora la lista queda: {lista_colores}")

# Eliminar o quitar elementos
lista_colores.pop(2)
print(f"Quito el tercer elemento, ahora la lista queda: {lista_colores}")

# Elimnar rojo
lista_colores.remove("rojo")
print(f"Quito 'rojo', ahora la lista queda: {lista_colores}")


# Vacío la lista por completo
lista_colores.clear()
print(f"Vacío por completo la lista, ahora la lista queda: {lista_colores}")

# Copiar el contenido de una lista
lista_colores = ["rojo", "azul", "verde", "amarillo"]   # lista original
lista_copia = lista_colores.copy()                       # Copia de lista original

# Quedan dos listas distintas
print(f"Listas Original y Copia:\n{lista_colores}\n{lista_copia}\n\n")

# Si vacío copia queda lista_colores original
lista_copia.clear()
print(f"Listas Original y Copia:\n{lista_colores}\n{lista_copia}\n\n")

# Apuntar con una lista a otra es otra cosa
lista_copia = lista_colores
print(f"Listas Original y Copia:\n{lista_colores}\n{lista_copia}\n\n")

# Pero si modifico una lista, también se modifica la otra
lista_copia.clear()
print(f"Listas Original y Copia:\n{lista_colores}\n{lista_copia}\n\n")

# Contar los elementos dentro de una lista
lista_colores = ["rojo", "azul", "verde", "amarillo", "rojo", "azul", "verde", "amarillo", "rojo"]

n_rojos = lista_colores.count("rojo")
n_violeta = lista_colores.count("violeta")
print(f"Cantidades de rojo:{n_rojos} y violeta:{n_violeta}.")

# Ubicar la posición de un elemento con lista.index
p_rojo1 = lista_colores.index('rojo')
p_rojo2 = lista_colores.index('rojo')
p_azul = lista_colores.index('azul')
p_verde = lista_colores.index('verde')
# error!! p_rosa = lista_colores.index('rosa')
# si el elemento no está en la lista devuelve un error
print(f"Posiciones de colores.")
print(f"Rojo:{p_rojo1}, Rojo:{p_rojo2}, Azul:{p_azul}, Verde:{p_verde}\n")

# Invertir las posiciones de una lista con lista.reverse()
print("\nlista.reverse()")
print(lista_colores)
lista_colores.reverse()
print(lista_colores)

# Ordenar una lista con sort()
print("\nlista.sort()")
print(lista_colores)
lista_colores.sort()
print(lista_colores)


# Ordenar una lista al reves con lista.sort(reverse=True)
print("\nlista.sort(reverse=True)")
print(lista_colores)
lista_colores.sort(reverse=True)
print(lista_colores)

# Extender una lista con otra lista
print("\nlista.extend(otra_lista)")
print(lista_colores)
lista_otros_colores = ["naranja", "morado", "marrón"]
lista_colores.extend(lista_otros_colores)
print(lista_colores)

print("\nlista.extend(otra_lista)")
otra_lista=[1, 2, 3, 4, 5]
print(lista_colores)
nueva_lista = lista_colores + otra_lista
print(nueva_lista)
nueva_lista = nueva_lista + [6,7,8,9]
print(nueva_lista)

# Extender una lista con otra lista de caracteres separados
print("\nlista.extend('púrpura')")
lista_colores = lista_colores + ['púrpura']
lista_colores.extend("púrpura")
print(lista_colores)

# Crear una lista usando map() objects with funcions
precios = [ 1.9 , 2.50, 10.0, 15.6]
impuesto = 0.8

def precio_con_impuesto(precios):
    return precios * (1+ impuesto)

preciosmasimpuestos = map(precio_con_impuesto, precios)
print(f"Precios s/impuestos: {precios}.\nPrecios c/impuestos: {list(preciosmasimpuestos)}.\n\n")

# Slice Listas - Elegir elementos de una lista
# Se especifica el primer elemento de una lista, el ultimo y el salto.
nombres = ['bernice', 'cody', 'aaron', 'ever', 'dalia']
primeros3 = nombres[:3]
print(primeros3)
segundos3 = nombres[1:4]
print(segundos3)

# Tomar los ultimos tres elementos de una lista si no conozco el largo
ultimos3 = nombres[len(nombres)-3:len(nombres)]
print(ultimos3, "ultimos tres en orden directo.")

# Tomar los ultimos tres en orden inverso
ultimos3 = nombres[:len(nombres)-4:-1]
print(ultimos3, "ultimos tres en orden inverso.")

# Desempaquetar una lista
nombre1, nombre2, *resto = nombres

# indices en una lista
nombres = ['bernice', 'cody', 'aaron', 'ever', 'dalia']
for nombre in nombres :
    print(nombre.index)

