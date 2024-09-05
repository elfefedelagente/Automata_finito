


def filtrarPalabras(oracion, combinaciones):
    
    palabras = oracion.split()

    palabrasFiltradas = [palabra for palabra in palabras if all(comb not in palabra for comb in combinaciones)]

    return ' '.join(palabrasFiltradas)


print(filtrarPalabras("el establo esta cerrado", ["blo", "el"]))