# Definir una lista de enteros por asignación en el bloque principal.
# Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos.
# Mostrar dicho producto en el bloque principal de nuestro programa.


def producto(lista):
    producto = 1
    for x in range(len(lista)):
        producto = producto * lista[x]
    return producto


lista = [3, 7, 8, 10, 2]
print(f"la lista es: {lista}, y su producto es: {producto(lista)}")
