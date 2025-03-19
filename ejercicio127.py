# Definir por asignación una lista de enteros en el bloque principal del programa.
# Elaborar tres funciones, la primera recibe la lista y retorna la suma de todos sus elementos,
# la segunda recibe la lista y retorna el mayor valor y la última recibe la lista y retorna el menor.


def sumarizar(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma + lista[x]
    return suma


def mayor(lista):
    mayor = lista[0]
    for x in range(1, len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]
    return mayor


def menor(lista):
    menor = lista[0]
    for x in range(1, len(lista)):
        if lista[x] < menor:
            menor = lista[x]
    return menor


# bloque principal del programa

listavalores = [10, 56, 23, 120, 94]
print("Contenido de la Lista es:")
print(listavalores)
print("La suma de contenido de la lista es: ", sumarizar(listavalores))
print("El numero mayor de la lista es: ", mayor(listavalores))
print("el numero menor de la lista es: ", menor(listavalores))
