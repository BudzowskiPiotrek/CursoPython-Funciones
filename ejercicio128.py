# Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros.
# Implementar una función que imprima el mayor y el menor valor de la lista.


def mayor_menor(lista):
    mayor = lista[0]
    menor = lista[0]
    for x in range(1, len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]
        else:
            if lista[x] < menor:
                menor = lista[x]
    print("El numero mayor de la lista es: ", mayor)
    print("El numero menor de la lista es: ", menor)


# bloque principal

lista = []
for x in range(5):
    valor = int(input("Ingrese valor:"))
    lista.append(valor)
mayor_menor(lista)
