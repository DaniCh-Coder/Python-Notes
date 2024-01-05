# This is a python file to practice variables in python scripts
# in corrects variables
# notese que todos los escritos luego del caracter "#" son comentarios

# Empecemos con el manejo de variables y sus nombres con varios ejemplos
nombre_variable = 1 
nombre_variable = 'variablecon nombre en string'
Nombre = 2
num = 3
Num1 = 'es el numero uno en un strng'

# it is not recomended using special Characters related to lenguages like ó ú
# let see one sample
frase_bienvenida = "------++++++++   PRIMER DÍA DE PYTHON +++++------------------------------++++++++++++++-----------------------------------"
print(frase_bienvenida)

# snake-case: minusculas preferentemente sin caracteres linguisticos
# reasignación de variables variable 2 contienen el mismo dato que variable 1
variable_1 = "Hola"
variable_2 = variable_1
print(variable_2)

a = "Este es mi valor inicial"
print (a)

# Introducir una variable desde la consola
a = input("Introduce tu nombre por favor: ")
print("Hola:", a, ". Gracias por introducir tu nombre")

# Concatenación con coma o con operador '+'

print("\n    Bienvenido/a" , a + "!.")  # Notese que con el operador "," se agregan espacios.
print("\n    Bienvenido/a" + a + "!!.") # Notese que con el operador "+" no se agregan espacios.
print("\n----------------------------------------------------------------------------------------------------------------------------------------\n")
frase_1 = "Tu nmbre es"
frase_2 = "y eres bienvenido!!!\n\n"
print(frase_1, a,  frase_2) # concatenado con comas para que queden espacios

# Ejemplos de reasignación de variables
a = "rojo"
b = "naranja"
c = "azul"
d = "verde"

# Colocar en a el valor de d
a = d
print("a y d:", a, d)
print("\n")
print("\n----------------------------------------------------------------------------------------------------------------------------------------\n")

