# Sets (se indican con {})
# Ñps set spm colecciones de items.
# Sets son listas aleatoreamente ordenadas. Sets por lo tanto son desordenados.
# Los set s utilizan para almacenar elementos únicos. Los sets descartan los elementos duplicados.
# Sets se indican con {}
# syntax
st = set()
print("Creamos un set 'st' de items")
st = {'item1', 'item2', 'item3', 'item4'}
print(st, "\n")

# Con len() podemos contar la cantidad de elementos.
print(f"'st' es un set que tiene: {len(st)} elementos.\n")
animales = { 'perro', 'gato', 'liebre', 'lobo', 'tigre'}

# Agregar y quitar elementos a un set
# syntax
st.add('item5')               # add permite solo un argumento
st.update(['item6', 'item7']) # update permite varios argumentos
st.remove('item2')            # remove quita un item específico
st.pop()                      # pop quita un item aleatorio
print(f"Luego de agregar y quitar varios items el set queda así:")
print(st)
print("\n")

# Vaciar sets
st.clear()
print(f"Luego de vaciar el set 'st', nos queda así: {st}.")

# Eliminar sets
del st
print(f"Con 'del' st se elimina el set 'st'. Luego de eliminar el set ya no existe mas e imprimirlo daría error.\n")

# Union, Intersección, Diferencia de sets

# Union de sets
input(f"Union e Intersección de sets. Pulse Enter para continuar...")
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(f"'st1' union 'st2' resulta igual a 'st3':")
print(f"{st1} union {st2} = {st3}\n")

# Intersección de sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st3 = st1.intersection(st2) # {'item3', 'item2'}
print(f"'st1' intersección 'st2' resulta igual a 'st3':")
print(f"{st1} intersección {st2} = {st3}\n")

# Diferencia de sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st3 = st1.difference(st2) # {'item1', 'item4'}
st4 = st2.difference(st1) # set()
print(f"Las diferencias entre 'st1' y 'st2' son como siguen:")
print(f"{st1} - {st2} = {st3}\n")
print(f"{st2} - {st1} = {st4}\n")

# Diferencia simétrica de sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2', 'item5'}
st3 = st1.symmetric_difference(st2) # {'item1', 'item4'}
st4 = st2.symmetric_difference(st1) # 
print(f"Las diferencias 'simétricas' entre 'st1' y 'st2' son como siguen:")
print(f"{st1} - {st2} = {st3}\n")
print(f"{st2} - {st1} = {st4}\n")

# Imprimiendo varias veces un set de animales dara como resultado
print(f"Un set se ordena aleatoriamente con un orden distinto con el fué creado. No varía en tiempo de ejecución.")
print(animales)
print(animales)
print("\n")

input("Diferencia entre tuplas, listas y los sets en notación. Pulse Enter para continuar...")
tuple_animales = ('perro', 'perro', 'gato', 'gato', 'liebre', 'lobo', 'tigre')
lista_animales = ['perro', 'perro', 'gato', 'gato', 'liebre', 'lobo', 'tigre']
set_animales   = {'perro', 'perro', 'gato', 'gato', 'liebre', 'lobo', 'tigre'}
print(f"tuple: {tuple_animales}")
print(f"lista: {lista_animales}")
print(f"set: {set_animales}")
print("\n")

input("Convertir una lista en un set. Pulse Enter para continuar...")
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # El orden es random.
print(lst)
print(st)
print('\n')

input("Buscando un item en un set. Pulse enter para continuar...")
st = {'item1', 'item2', 'item3', 'item4'}
si_esta = "item1" in st
print(f"'item1' está en 'st'? {si_esta}")
print(f"'item221' está en 'st'? {'item221' in st}")
print("\n")

