# Confeccionar una función que reciba tres valores de IMC y nos muestre el mayor de ellos.
# La carga de los valores se realizará por teclado.


def mostrar_mayor_imc(imc1, imc2, imc3):
    print("El mayor índice IMC es:")
    if imc1 > imc2 and imc1 > imc3:
        print(imc1)
    elif imc2 > imc3:
        print(imc2)
    else:
        print(imc3)


def calcular_imc(peso, altura):
    return peso / (altura**2)


def cargar():
    print("Ingrese los datos de tres personas")

    peso1 = float(input("Ingrese el peso (kg) de la primera persona: "))
    altura1 = float(input("Ingrese la altura (m) de la primera persona: "))

    peso2 = float(input("Ingrese el peso (kg) de la segunda persona: "))
    altura2 = float(input("Ingrese la altura (m) de la segunda persona: "))

    peso3 = float(input("Ingrese el peso (kg) de la tercera persona: "))
    altura3 = float(input("Ingrese la altura (m) de la tercera persona: "))

    imc1 = calcular_imc(peso1, altura1)
    imc2 = calcular_imc(peso2, altura2)
    imc3 = calcular_imc(peso3, altura3)

    print(f"IMC de la primera persona: {imc1:.2f}")
    print(f"IMC de la segunda persona: {imc2:.2f}")
    print(f"IMC de la tercera persona: {imc3:.2f}")

    mostrar_mayor_imc(imc1, imc2, imc3)


# Programa principal
cargar()
