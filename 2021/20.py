"""En la clase de español del pueblo de Laponia han creado un reto a la hora de escribir la carta a Papa Noél 🎅: la carta ✉️ tiene que contener todas las letras del alfabeto.

Desde el taller de Santa 🎅 se han enterado y quieren escribir una función que les diga si realmente la cadena de texto que les llega tiene, efectivamente, todas las letras del abecedario español 🔎.

Hay que tener en cuenta las letras en mayúscula y que las letras con acento y diéresis se consideran iguales. Por ejemplo la á y la ä cuenta como una a.

Vamos a ver unos ejemplos de frases.

Y ya que estás... ¿Cuál es tu pangrama favorito? ¡Compártelo en nuestra comunidad de Discord!"""


def pangram(letter: str) -> bool:
    alphabet = "abcdefghijklmnñopqrstuvwxyz"
    alphabet_set = set(alphabet)
    alphabet += "áéíóúëïü"

    letter = filter(lambda x: x in alphabet, letter.lower())

    correlations = { "á": "a", "é": "e", "ë": "e", "í": "i", "ï": "i", "ó": "o", "ú": "u", "ü": "u" }

    for char in letter:
        if char in correlations: char = correlations[char]

        alphabet_set.discard(char)
    
    return True if not alphabet_set else False


def test(expected, received):
    return expected == received


def main():
    print(test(True, pangram('Extraño pan de col y kiwi se quemó bajo fugaz vaho'))) # true
    print(test(True, pangram('Jovencillo emponzoñado y con walkman: ¡qué figurota exhibes!'))) # true
    print(test(False, pangram('Esto es una frase larga pero no tiene todas las letras del abecedario'))) # false
    print(test(False, pangram('De la a a la z, nos faltan letras'))) # false


if __name__ == "__main__":
    main()