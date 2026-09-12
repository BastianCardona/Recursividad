# Ejercicio 1:
## a. ) Por qué es un problema recursivo ?
Un ciclo *for* funciona bien cuando sabemos de antemano cuántas veces hay que repetir algo o cuando se recorre una estructura "plana" como una lista o arreglo.
Lo primero es que **desconocemos la profundidad de los directorios** ya sean 0, 5 o 20 niveles de directorios anidados un ciclo *for* necesita saber el número 
de directorios de antemano. Y es naturalmente recursivo debido a que una carpeta/directorio contiene dentro de si misma más carpetas/directorios; por lo cual
la definición se repite a sí misma en una escala menor, por eso es recursivo. Finalmente no hay una forma natural de **"aplanar"** con un solo ciclo ya que
sería como simular la recursión a mano; lo cual es ineficiente y con un solo *for* se recorrería un nivel, necesitaríamos conocer la profundidad y hacer un ciclo
dentro de otro y otro y así sucesivamente.
## b. ) Escriban el pseudocódigo de una función recursiva calcularEspacio(carpeta)
función calcularEspacio(carpeta):
    si carpeta.subcarpetas está vacío: // CASO BASE sin subcarpetas
        return sumaTamañoArchivos(carpeta) 
    espacioTotal = sumaTamañoArchivos(carpeta)   // archivos propios de esta carpeta
    para cada subcarpeta en carpeta.subcarpetas:
        espacioTotal = espacioTotal + calcularEspacio(subcarpeta)   // llamada recursiva
    return espacioTotal

## c. ) Tracen la pila de llamadas para una estructura de ejemplo con 3 niveles de subcarpetas que ustedes mismos propongan
El punto c está en el archivo de `exploración_carpetas.py`.