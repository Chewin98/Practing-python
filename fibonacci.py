"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci(inicio,final):
    anterior = 0
    actual = inicio
    siguiente = inicio + 1
    while (actual <= final):
        print(actual)
        actual = siguiente
        siguiente = actual + anterior
        anterior = actual
    print("fin!")

fibonacci(0,50)