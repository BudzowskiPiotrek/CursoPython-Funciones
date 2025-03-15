# Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales.
# Llamarla desde el bloque principal del programa 3 veces con string distintos.
# Implementa un return.


def cantidad_vocales(palabra):
    vocales = "aeiou"
    cant = sum(1 for letra in palabra if letra in vocales)
    return cant  


# Bloque principal
for palabra in ["Cocacola", "Pepsi", "Banana"]:
    cantidad = cantidad_vocales(palabra)  
    print(f"{palabra} tiene: {cantidad} vocales")
