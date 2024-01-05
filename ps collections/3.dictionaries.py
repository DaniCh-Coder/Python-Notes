# Creando un diccionario
familia = { 
            'Dani' : "Daniel Christello",
             'Dan' : "Daniela Lopez Guevara",
             'Galo': "Galo Christello"
}

# Imprimiento una clase
print(familia)

# Imprimiendo un elemento de una diccionario por su clave
print(familia['Dani'])  # Las claves que no exiten dan error

# Agregando un elemento a un diccionario
familia['Coco'] = 'Coco Christello'

# Listando la clase completa
print(familia)

# Creando otra clasae con números
numeros = { 
            1 : "Número 1",
            2 : "Número 2",
            3 : "Número 3"
}

# Imprimiento la clase 
print(numeros)

# Imprimiendo un elemento de una clase por su clave
print(numeros[1])  # Las claves que no exiten dan error

# Agregando un elemento a una clase
numeros[4] = 'Número 4'

# Listando la clase completa
print(numeros)

# Iteracciones con diccionarios
print(f"Imprimiendo las claves del diccionario familia:")
for familiar in familia:
    print(familiar)

print(f"Imprimiendo las claves del diccionario numeros:")
for numero in numeros:
    print(numero)

print(f"Imprimiendo el contenido de ambos diccionarios:")
for familiar in familia:
    print(f"{familiar} : {familia[familiar]}.")

for numero in numeros:
    print(f"{numero} : {numeros[numero]}.")       