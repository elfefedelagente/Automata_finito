class AutomataFinito:
    def __init__(self, combinaciones_bloqueadas):
        # Almacenar las combinaciones de letras bloqueadas
        self.combinaciones_bloqueadas = combinaciones_bloqueadas

    def procesar_palabra(self, palabra):
        # Simula el autómata para cada palabra
        for combinacion in self.combinaciones_bloqueadas:
            if combinacion in palabra:
                return False  # La palabra es rechazada
        return True  # La palabra es aceptada

    def filtrar_texto(self, texto):
        palabras = texto.split()
        palabras_filtradas = []

        # Procesar cada palabra a través del autómata
        for palabra in palabras:
            if self.procesar_palabra(palabra):
                palabras_filtradas.append(palabra)

        return ' '.join(palabras_filtradas)

def leer_combinaciones():
    # Combinaciones bloqueadas especificadas en el código
    combinaciones_bloqueadas = ["blo", "el"]
    return combinaciones_bloqueadas

def main():
    # Leer las combinaciones bloqueadas
    combinaciones_bloqueadas = leer_combinaciones()

    # Leer el archivo de entrada
    archivo_entrada = 'entrada.txt'
    archivo_salida = 'salida.txt'

    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as entrada:
            texto = entrada.read()
    except FileNotFoundError:
        print(f"El archivo {archivo_entrada} no se encontró.")
        return

    # Crear el autómata finito con las combinaciones bloqueadas
    automata = AutomataFinito(combinaciones_bloqueadas)

    # Filtrar el texto usando el autómata
    texto_filtrado = automata.filtrar_texto(texto)

    # Guardar el resultado en el archivo de salida
    with open(archivo_salida, 'w', encoding='utf-8') as salida:
        salida.write(texto_filtrado)

    print(f"Texto filtrado guardado en {archivo_salida}")

if __name__ == '__main__':
    main()
