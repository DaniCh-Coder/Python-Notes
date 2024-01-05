# String in python - Type of variable

color_blue = "Blue es azul en español"
color_azul = 'Azul is blue color in english'

print(color_blue)
print(color_azul)

# Función len() devuelve el largo del sting
len(color_azul)
print(len(color_blue), len(color_azul))

# Posiciones en el string
print("Posiciones en strings:")
print(0," ", color_blue[0], color_azul[0])
print(1," ", color_blue[1], color_azul[1])
print(2," ", color_blue[2], color_azul[2])
print(3," ", color_blue[3], color_azul[3])
print(4," ", color_blue[4], color_azul[4])

# Iteraciones sobre strings
input("\nIteraciones sobre strings. Pulse Enter para continuar...")
for letra in color_azul:
    print(letra)

# Cual es el largo de un numero en cantindad de digitos
input("\nUso de string para calcular el largo de los numeros. Presione Enter para continuar...")
digitos = str(1234556789)   # transformamos el numero 123456789 a string
print(123456789)            # imprimimos el numero que estamos analizando
print(len(digitos))         # calculamos e imprimimos la cantidad de digitos

# La función type() nos permite darnos cuenta de que tipo es el dato o varialbe
print("\nUso de type con strings:")
print(type(123456789))
print(type(digitos))

# Concatenación y uniones de strings
input("\nConcatenaciones y uniones de strings. Pulse Enter para continuar...")
# La suma de sting son en realidad concatenaciones
print("Suma de strings")
color_blue_y_azul = color_blue + color_azul
print(color_blue_y_azul)

# Concatenación de strings con join()
input("\nConcatenación y formatero de strings, con join. Presione Enter para continuar...")
# Ejemplo join con una variable string
traduccion = " ".join(color_azul)
print(traduccion)           # A z u l   i s   b l u e   c o l o r   i n   e n g l i s h

# Otro ejemplo join: join siempre espera un iterable string
print("*".join(digitos))    # 1*2*3*4*5*5*6*7*8*9

texto = ("Parrafo 1", "Parrafo 2", "Parrafo 3")
print("\n".join(texto))
# Parrafo 1
# Parrafo 2
# Parrafo 3

# %s %i %f con operador %
entero = 1
flotante = 1.56
texto = "palabra"

print("%i %f %s" % (entero, flotante, texto))   # 1 1.560000 palabra
print("%i-%f-%s" % (entero, flotante, texto))   # 1-1.560000-palabra

# objeto string con .format
print("{} {} {}".format(entero, flotante, texto))                               # 1 1.56 palabra
print("Entero: {}. Flotente: {}. Texto: {}".format(entero, flotante, texto))    # Entero: 1. Flotente: 1.56. Texto: palabra

# Multiplicación de textos
input("\nMultiplicación de textos. Pulse cualquier Enter para continuar...")
print("Perro " * 3)
texto_factor = "{} {} {}".format(entero, flotante, texto) 
print((texto_factor + " ") * 3)

# Alamacenamiento de textos largos
input("\nAlmacenamiento de textos largos. Presione enter para continuar...")
texto_largo = """-> Zombie ipsum brains reversus ab cerebellum viral inferno, brein nam rick mend grimes malum cerveau cerebro. De carne cerebro lumbering animata cervello corpora quaeritis. Summus thalamus brains sit​​, morbo basal ganglia vel maleficia? De braaaiiiins apocalypsi gorger omero prefrontal cortex undead survivor fornix dictum mauris. Hi brains mindless mortuis limbic cortex soulless creaturas optic nerve, imo evil braaiinns stalking monstra hypothalamus adventus resi hippocampus dentevil vultus brain comedat cerebella pitiutary gland viventium. Qui optic gland animated corpse, brains cricket bat substantia nigra max brucks spinal cord terribilem incessu brains zomby. The medulla voodoo sacerdos locus coeruleus flesh eater, lateral geniculate nucleus suscitat mortuos braaaains."""
print(texto_largo)

texto_formateado = """-> Zombie ipsum brains reversus ab cerebellum viral inferno, 
brein nam rick mend grimes malum cerveau cerebro. 
De carne cerebro lumbering animata cervello corpora quaeritis. 
Summus thalamus brains sit​​, morbo basal ganglia vel maleficia? 
De braaaiiiins apocalypsi gorger omero prefrontal cortex undead survivor fornix dictum mauris. 
Hi brains mindless mortuis limbic cortex soulless creaturas optic nerve, 
imo evil braaiinns stalking monstra hypothalamus adventus resi hippocampus dentevil vultus 
brain comedat cerebella pitiutary gland viventium. Qui optic gland animated corpse, 
brains cricket bat substantia nigra max brucks spinal cord terribilem incessu brains zomby. 
The medulla voodoo sacerdos locus coeruleus flesh eater, lateral geniculate nucleus 
suscitat mortuos braaaains."""
print(texto_formateado)

# Creacion de listas, tuplas y diccionarios a partir de strings
input("Listas, Tuplas y Diccionarios a partir de srtrings (con enumerate). Presione enter para continuar...")
# Listas
lista = list(color_azul)
print(lista)
lista = list(enumerate(color_azul))
print(lista)

# Tuplas
tupla = tuple(color_azul)
print(tupla)
tupla = tuple(enumerate(color_azul))
(enumerate(color_azul))
print(tupla)

# Diccionarios
# dicci = dict(color_azul)  # No se puede hacer un diccionario sin enumerate
# print(dicci)              # un diccionario necesita pares de datos para armar el indice y el contenido
dicci = dict(enumerate(color_azul))
(enumerate(color_azul))
print(dicci)

print(color_azul.split(" "))






