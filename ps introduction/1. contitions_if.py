# Contitions y python
# Hay mas información de condiciones en el manejo de lists
# Empezar por aquí
# Controlamos la edad del usuario
edad = int(input("Itroduzca su edad: "))
print(f"Ud. tiene {edad} años.")

# Primero veamos el control de edad más sencillo
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# Ahora veamos que podemos hacer en función de la edad
if edad >= 18:
    # es mayor de edad puede elegir una bebida alcoholica
    print("Puede elegir entre una de las siguientes bebidas")
    respuesta = input("1. Ron.\n2. Whisky.\n3. Ginebra.\n")
    print("Sirvase, aqui tiene...", " ")

    if respuesta == '1':
        print("un Ron")
    elif respuesta == '2':
        print("un Whisky")
    elif respuesta == '3':
        print("una Ginebra")
    else:
        print("una opción no valida")
else:
    # es menor de edad puede elegir una bebida sin alcohol
    print("Puede elegir entre una de las siguientes bebidas")
    respuesta = input("1. Coca.\n2. Fanta.\n3. Sprite.\n")
    print("Sirvase, aqui tiene...", " ")

    if respuesta == '1':
        print("una Coca")
    elif respuesta == '2':
        print("una Fanta")
    elif respuesta == '3':
        print("una Sprite")
    else:
        print("una opción no valida")
    
