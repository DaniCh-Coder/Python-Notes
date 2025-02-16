# Manejo de excepciones
# try maneja los errores si aparecen y actúa según lo que se prevea
# try puede controlar distintos tipos de error
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')       # if the input is not converted to int it will rise TypeError
    # year_born = int(input('Year you were born:'))  # if inpunt is converted to int wit will work ok
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

# Si el codigo no tiene errores entonces sale por else: y luego finally.
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print('You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I always run.')

# Otro ejemplo. Olvido de poner * en una lista para desempaquetarla
try:
    def sum_of_five_nums(a, b, c, d, e):
        return a + b + c + d + e

    lst = [1, 2, 3, 4, 5]
    print(sum_of_five_nums(*lst))  # Si coloco *lst da 15. Si coloco lst sin * da error.
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I always run.')