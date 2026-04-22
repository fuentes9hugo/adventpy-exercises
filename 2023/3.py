"""En el taller de Santa, un elfo travieso ha estado jugando en la cadena de fabricación de regalos, añadiendo o eliminando un paso no planificado.

Tienes la secuencia original de pasos en la fabricación original y la secuencia modificada modified que puede incluir un paso extra o faltar un paso.

Tu tarea es escribir una función que identifique y devuelva el primer paso extra que se ha añadido o eliminado en la cadena de fabricación. Si no hay ninguna diferencia entre las secuencias, devuelve una cadena vacía.

A tener en cuenta:
- Siempre habrá un paso de diferencia o ninguno.
- La modificación puede ocurrir en cualquier lugar de la cadena.
- La secuencia original puede estar vacía"""


def findNaughtyStep(original: str, modified: str) -> str:
    original_len = len(original)
    modified_len = len(modified)

    if original_len == modified_len: return ""

    long, short = (original, modified) if original_len > modified_len else (modified, original)

    for long_char, short_char in zip(long, short):
        if long_char != short_char: return long_char

    return long[-1]


def test(e, r) -> bool:
    return e == r


def main():
    original = 'abcd'
    modified = 'abcde'
    print(test("e", findNaughtyStep(original, modified))) # 'e'

    original = 'stepfor'
    modified = 'stepor'
    print(test("f", findNaughtyStep(original, modified))) # 'f'

    original = 'abcde'
    modified = 'abcde'
    print(test("", findNaughtyStep(original, modified))) # ''


if __name__ == "__main__":
    main()