# Suma, resta multiplicacio con definicines


def digitoUno():
    a = int(input("dime primer digito: "))
    return a


def digitoDos():
    b = int(input("dime primer digito: "))
    return b


def opciones():
    opcion = int(input("Que quieres hacer 1. sumar 2. restar 3 multiplicar: "))
    return opcion


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


a = digitoUno()
b = digitoDos()
opcion = opciones()

if opcion == 1:
    print(suma(a, b))
elif opcion == 2:
    print(resta(a, b))
elif opcion == 3:
    print(multiplicacion(a, b))
