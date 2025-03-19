# Crear una lista de enteros por asignación.
# Definir una función que reciba una lista de enteros y un segundo parámetro de tipo entero.
# Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.


def multiplicar(lista, multi):
    suma = 0
    for x in range(len(lista)):
        suma = suma + (lista[x] * multi)
    return suma
        
        
lista = [3, 7, 8, 10, 2]
multi = 3
suma = multiplicar(lista,multi)
print(suma)