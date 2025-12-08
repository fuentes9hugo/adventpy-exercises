"""Santa 🎅 quiere saber cuál es la primera letra no repetida en el nombre de un juguete 🎁.

Escribe una función que reciba un string y devuelva la primera letra que no se repite, ignorando mayúsculas y minúsculas al contar, pero devolviendo la letra tal como aparece en el string.

Si no hay ninguna, devuelve una cadena vacía ("")."""


def findUniqueToy(toy: str) -> str:
    toy_lower = toy.lower()
    for i, char in enumerate(toy_lower):
        if toy_lower.count(char) == 1:
            return toy[i]
    
    return ""


def test(expected, received):
    return expected == received


def main():
    print(test("G", findUniqueToy('Gift'))) # 'G'
    # ℹ️ La G es la primera letra que no se repite
    # y la devolvemos tal y como aparece

    print(test("", findUniqueToy('sS'))) # ''
    # ℹ️ Las letras se repiten, ya que no diferencia mayúsculas

    print(test("i", findUniqueToy('reindeeR'))) # 'i'
    # ℹ️ La r se repite (aunque sea en mayúscula)
    # y la e también, así que la primera es la 'i'

    # Más casos:
    print(test("", findUniqueToy('AaBbCc'))) # ''
    print(test("a", findUniqueToy('abcDEF'))) # 'a'
    print(test("F", findUniqueToy('aAaAaAF'))) # 'F'
    print(test("T", findUniqueToy('sTreSS'))) # 'T'
    print(test("z", findUniqueToy('z'))) # 'z'


if __name__ == "__main__":
    main()