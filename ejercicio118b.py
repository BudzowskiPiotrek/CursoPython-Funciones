# Desarrollar un programa que permita ingresar el lado de un cuadrado.
# Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.
# Implementa un return.


def mostrar_perimetro(lado):
    per = lado * 4
    return per  


def mostrar_superficie(lado):
    sup = lado * lado
    return sup  


def cargar_dato():
    lado = int(input("Ingrese el valor del lado de un cuadrado: "))
    respuesta = input(
        "¿Quiere calcular el perímetro o la superficie? [ingresar texto: perimetro/superficie]: "
    )
    if respuesta == "perimetro":
        perimetro = mostrar_perimetro(lado)  
        return f"El perímetro es: {perimetro}"
    elif respuesta == "superficie":
        superficie = mostrar_superficie(lado)  
        return f"La superficie es: {superficie}"
    else:
        return "Opción no válida. Debe ingresar 'perimetro' o 'superficie'."


# Programa principal
resultado = cargar_dato()  
print(resultado)  
