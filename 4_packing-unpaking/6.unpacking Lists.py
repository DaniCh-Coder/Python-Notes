# Unpacking Lists
# A veces es necesario descomponer, dividir o desempaquetar los elementos de una lista
# para esto existe un operador que es el asterisco
# para pack and unpack en listas y tuplas se usa * (uno)
# para pack and unpack en diccionarios se usa ** (dos)
# unpacking
# veamos el efecto de unpacking en una lista 
lst = [1, 2, 3, 4, 5]
print(lst)
print(*lst)

# primero veamos un problema que arroja un error por no usar este operador *
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

# Ejemplo poner * en una lista para desempaquetarla
try:
    def sum_of_five_nums(a, b, c, d, e):
        return a + b + c + d + e

    lst = [1, 2, 3, 4, 5]
    print(sum_of_five_nums(*lst))  # Si coloco *lst da 15. Si coloco lst sin * da error.
except:
    print("error")


