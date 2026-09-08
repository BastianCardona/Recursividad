def busqueda_binaria_recursiva(arreglo, objetivo, izquierda=0, derecha=None):
    if derecha is None:
        derecha = len(arreglo) - 1

    # Caso base 1: no queda rango por revisar -> no se encontró
    if izquierda > derecha:
        return -1

    medio = (izquierda + derecha) // 2

    # Caso base 2: encontramos el objetivo
    if arreglo[medio] == objetivo:
        return medio

    # Caso recursivo: descartamos la mitad que no sirve
    elif arreglo[medio] < objetivo:
        return busqueda_binaria_recursiva(arreglo, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(arreglo, objetivo, izquierda, medio - 1)