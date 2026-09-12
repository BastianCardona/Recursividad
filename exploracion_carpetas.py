"""
Ejercicio 1 - Exploracion de carpetas (recursividad)
-----------------------------------------------------
Calcula el espacio total ocupado por una carpeta que puede contener
archivos y subcarpetas, hasta un nivel desconocido de profundidad.

Caso base: una carpeta sin subcarpetas -> solo se suman sus archivos.
Caso recursivo: se suman los archivos directos + el espacio de cada
                 subcarpeta (calculado con una llamada recursiva).
"""


class Archivo:
    def __init__(self, nombre, tamano_mb):
        self.nombre = nombre
        self.tamano_mb = tamano_mb


class Carpeta:
    def __init__(self, nombre, archivos=None, subcarpetas=None):
        self.nombre = nombre
        self.archivos = archivos if archivos else []
        self.subcarpetas = subcarpetas if subcarpetas else []


    def calcularEspacio(carpeta, nivel=0):
        """Calcula recursivamente el espacio total (en MB) de una carpeta."""
        sangria = "  " * nivel
        print(f"{sangria}-> Entrando a '{carpeta.nombre}'")

        # Sumar el tamano de los archivos directos de esta carpeta
        espacio_total = sum(archivo.tamano_mb for archivo in carpeta.archivos)

        # Caso base: la carpeta no tiene subcarpetas
        if not carpeta.subcarpetas:
            print(f"{sangria}   (sin subcarpetas -> caso base) "
                f"= {espacio_total} MB")
            return espacio_total

        # Caso recursivo: sumar el espacio de cada subcarpeta
        for subcarpeta in carpeta.subcarpetas:
            espacio_total += calcularEspacio(subcarpeta, nivel + 1)

        print(f"{sangria}<- Saliendo de '{carpeta.nombre}' "
            f"= {espacio_total} MB")
        return espacio_total


def construir_ejemplo():
    """Construye la estructura de 3 niveles usada en el ejercicio."""
    vacaciones = Carpeta("Vacaciones", archivos=[Archivo("playa.jpg", 20)])
    fotos = Carpeta("Fotos", archivos=[Archivo("perfil.png", 50)],
                     subcarpetas=[vacaciones])

    tareas = Carpeta("Tareas", archivos=[Archivo("tarea1.docx", 8)])
    documentos = Carpeta("Documentos", archivos=[Archivo("cv.pdf", 5)],
                          subcarpetas=[tareas])

    raiz = Carpeta("Raiz", archivos=[Archivo("readme.txt", 10)],
                   subcarpetas=[fotos, documentos])
    return raiz


if __name__ == "__main__":
    raiz = construir_ejemplo()
    print("=== Traza de la recursividad ===\n")
    total = calcularEspacio(raiz)
    print(f"\n=== Espacio total ocupado: {total} MB ===")