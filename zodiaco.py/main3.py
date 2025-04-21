def leer_posicion(pieza):
    while True:
        try:
            fila, col = map(int, input(f"{pieza.capitalize()} - Ingresa fila y columna (1-8): ").split())
            if 1 <= fila <= 8 and 1 <= col <= 8:
                return fila, col
            print("Coordenadas fuera de rango.")
        except: print("Entrada no válida.")

def puede_capturar(torre, alfil):
    return "La torre puede capturar al alfil." if torre[0] == alfil[0] or torre[1] == alfil[1] else \
           "El alfil puede capturar a la torre." if abs(torre[0] - alfil[0]) == abs(torre[1] - alfil[1]) else \
           "Ninguna pieza puede capturar a la otra."

# Obtener posiciones
torre = leer_posicion("torre")
alfil = leer_posicion("alfil")

# Resultados
print(puede_capturar(torre, alfil))
