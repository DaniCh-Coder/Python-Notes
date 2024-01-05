# functions funciones
# Ejemplos de funciones

# 1. Una función simple que salude
# esta función usa dos parametros: nombre y edad.
def saludar(nombre, edad):
    print(f"Hola {nombre}!. Tu edad es: {edad}.")

# En cada llamada a la función le indicamos los valores de los parametros
print(f"Llamamos a la función saludar pasandole los valores de dos parametros: nombre y edad.")
saludar("Galo", 11)

# Los argumentos posicionales se interpretan por su orden
# Los argumentos clave llevan el nombre del parametro=

# Si no se conoce el orden exacto de los parametros si pueden especificar con el nombre
saludar(edad = 51, nombre ="Dan")

# Si no especifico el orden de los parametros la función los interpreta de primero a ultimo
saludar(61, "Dani")
        
# 2. Una función simple con return()
def suma(num1, num2):
    return num1 + num2

# La llamada con numeros hace la suma de los mismos
print(f"suma de dos numeros: {suma(3,5)}")

# La llamada con stings hace la concatenacion de los dos strings
print(f"suma de dos numeros: {suma('ho','la')}")
      
# 3. Una función que agrega elementos a una lista
# se define la función
def agrega_elementos(lista, elemento):
    lista.append(elemento)
    return lista

# se crea una lista
colores = ["rojo"]

# se pide el ingreso de los colores y se llama a la función
print(f"Por favor agregue colores a esta lista de colores (o 'salir'): {colores}")
while True:
    color = input("Ingrese color: ")
    if color == 'salir':
        break
    agrega_elementos(colores, color)

print(f"La sista quedó de la siguiente manera:")
print(colores, "\n")

# 4. Calculadora con funciones
# definiciones de funciones de operaciones
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multi(a, b):
    return a * b

def divi(a, b):
    return a / b

def resto(a, b):
    return a % b

def expon(a, b):
    return a ** b

print("--- CALCULADORA CON IF, ELSE, ELIF, MACH Y FUNCIONES ----")

otravez = 'S'   # variable de iteracción para hacer otro cálculo
# se haran calculos mientras otra vez sea distinto de 'N' o 'n'
while otravez != 'N' and otravez != 'n':
    # Se busca que operación introdujo el usuario con el operador condicional match

    # Menú de opciones para el usuario
    print("Por favor, indique qe operación desea realizar")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo")
    print("6. Exponente")

    # Solicita al usuario que indique la operación que desea
    operacion = int(input("Indique por favor el número de operción y pulse enter: "))

    # Se ingroduce el concepto de control de error
    noerror = True

    print("Operación", end=' ')
    match operacion:
        case 1:
            print("Suma ")
            eligio = "sumar"
        case 2:
            print("Resta ")
            eligio = "restar"
        case 3:
            print("Multiplicación")
            eligio = "multiplicar"
        case 4:
            print("División ")
            eligio = "dividir"
        case 5:
            print("Módulo ")
            eligio = "módulo"
        case 6:
            print("Exponente ")
            eligio = "exponente"
        case _:
            print("Opción Invalida")
            eligio = "mal"
            noerror = False

    # Si la operación elegida es correcta se procede con el cálculo
    if noerror:     # Sin error. Se solicitan los operandos
            num1 = float(input("Especifique el primer operando:"))
            num2 = float(input("Especifique el segundo operando:"))

            # Se realiza la operación
            print("Operación", end=' ')
            match operacion:
                case 1:
                    # suma
                    print(f"El resultado de {eligio}: {num1} + {num2} es: {suma(num1, num2)}.")
                case 2:
                    # resta
                    print(f"El resultado de {eligio}: {num1} - {num2} es: {resta(num1, num2)}.")
                case 3:
                    # multiplicación
                    print(f"El resultado de {eligio}: {num1} * {num2} es: {multi(num1, num2)}.")
                case 4:
                    # division
                    print(f"El resultado de {eligio}: {num1} / {num2} es: {divi(num1, num2)}.")
                case 5:
                    # resto
                    print(f"El resultado de {eligio}: {num1} % {num2} es: {resto(num1, num2)}.")
                case 6:
                    # exponente
                    print(f"El resultado de {eligio}: {num1} ** {num2} es: {expon(num1, num2)}.")
                case _:
                    print("Opción Invalida")
                    noerror = False
    else:   # Hay error en la opción elegida
        print("Por favor vuelva a intentar")

    otravez = input("Desea hacer otro cálculo? (S/N): ")



# Esta son funciones de control de error
def error(msg):
    msg = "ERROR: " + msg
    print(msg, file=sys.stderr)
    return 1

def error(msg):
    from sys import stderr, exit
    print(msg, file=stderr)
    exit(1)