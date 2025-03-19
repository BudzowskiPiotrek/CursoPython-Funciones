# Desarrollar una función que reciba una lista de string y nos retorne
# el que tiene más caracteres. Si hay más de uno con dicha cantidad de
# caracteres debe retornar el que tiene un valor de componente más baja.
# En el bloque principal iniciamos por asignación la lista de string:


def mascaracteres(palabras):
    mayor = 0
    for x in range(len(palabras)):
        if len(palabras[x]) > len(palabras[mayor]):
            mayor = x
    return palabras[mayor]


palabras = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:", mascaracteres(palabras))
