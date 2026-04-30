"""En el taller de Santa, los elfos aman los acertijos 🧠. Este año, han creado uno especial: un desafío para formar un palíndromo navideño.

Un palíndromo es una palabra que se lee igual hacia adelante y hacia atrás. Los elfos quieren saber si es posible formar un palíndromo haciendo, como mucho, un intercambio de letras.

Crea una función getIndexsForPalindrome que reciba una cadena de caracteres y devolverá:
- Si ya es un palíndromo, un array vacío.
- Si no es posible, null.
- Si se puede formar un palíndromo con un cambio, un array con las dos posiciones (índices) que se deben intercambiar para poder crearlo.

Si se puede formar el palíndromo con diferentes intercambios, siempre se debe devolver el primero que se encuentre."""


def getIndexsForPalindrome(word: str) -> list[int] | None:
    if word == word[::-1]: return []
    
    for i, char_1 in enumerate(word):
        for j, char_2 in enumerate(word[i + 1:], start=i+1):
            list_word = list(word)
            list_word[i], list_word[j] = list_word[j], list_word[i]
            new_word = "".join(list_word)

            if new_word == new_word[::-1]: return [i, j]
    
    return None


def test(e, r) -> bool:
    return e == r


def main():
    print(test([], getIndexsForPalindrome('anna'))) # []
    print(test([0, 1], getIndexsForPalindrome('abab'))) # [0, 1]
    print(test(None, getIndexsForPalindrome('abac'))) # null
    print(test([], getIndexsForPalindrome('aaaaaaaa'))) # []
    print(test([1, 3], getIndexsForPalindrome('aaababa'))) # [1, 3]
    print(test(None, getIndexsForPalindrome('caababa'))) # null


if __name__ == "__main__":
    main()