# 1. contidion match
# Condiciones en python
# Proyecto Calculadora solo con condicionales sin funciones ni bucles
print("--- CALCULADORA CON IF, ELSE, ELIF Y MATCH ----")

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

# Se busca que operación introdujo el usuario con el operador condicional match
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
if noerror:
    # Se solicitan los operandos
    num1 = float(input("Especifique el primer operando:"))
    num2 = float(input("Especifique el segundo operando:"))

    # Se realiza la operación
    print("Operación", end=' ')
    match operacion:
        case 1:
            # suma
            resultado = round(num1 + num2, 2)
            print(f"El resultado de {eligio}: {num1} + {num2} es: {resultado}.")
        case 2:
            # resta
            resultado = round(num1 - num2, 2)
            print(f"El resultado de {eligio}: {num1} - {num2} es: {resultado}.")
        case 3:
            # multiplicación
            resultado = round(num1 * num2, 2)
            print(f"El resultado de {eligio}: {num1} * {num2} es: {resultado}.")
        case 4:
            # division
            resultado = round(num1 / num2, 2)
            print(f"El resultado de {eligio}: {num1} / {num2} es: {resultado}.")
        case 5:
            # resto
            resultado = round(num1 % num2, 2)
            print(f"El resultado de {eligio}: {num1} % {num2} es: {resultado}.")
        case 6:
            # exponente
            resultado = round(num1 ** num2, 2)
            print(f"El resultado de {eligio}: {num1} ** {num2} es: {resultado}.")
        case _:
            print("Opción Invalida")
            noerror = False
else:
    print("Por favor vuelva a ejecutar la calculadora")
