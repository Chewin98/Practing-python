"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

def anagrama(primera, segunda):
    if primera == segunda:
        print("no es un anagrama, son la misma palabra")
    elif len(primera) != len(segunda):
        print("no es un anagrama por que tienen cantidad de letreas diferentes")
    else:
        palabra = list(primera)
        anagrama = list(segunda)
        
        palabra.sort()
        anagrama.sort()
        
        if palabra != anagrama:
            print(f"{primera} y {segunda} no son un anagrama")
        else:
            print(f"la palabra {primera} y {segunda} si son anagramas")


anagrama("todos", "sodot")