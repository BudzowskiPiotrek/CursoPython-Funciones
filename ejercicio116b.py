# Confeccionar una aplicación que muestre una presentación en pantalla del programa.
# Solicite la carga de un número y nos muestre su tabla de multiplicar del 1 al 10.
# Mostrar finalmente un mensaje de despedida del programa.


def mostrar_mensaje(mensaje):
    print("*************************************************")
    print(mensaje)
    print("*************************************************")


def mostrar_tabla():
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


# Programa principal
mostrar_mensaje("El programa muestra la tabla de multiplicar de un número ingresado.")
mostrar_tabla()
mostrar_mensaje("Gracias por utilizar este programa.")
