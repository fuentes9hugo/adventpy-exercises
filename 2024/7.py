"""¡El grinch 👹 ha pasado por el taller de Santa Claus! Y menudo desastre ha montado. Ha cambiado el orden de algunos paquetes, por lo que los envíos no se pueden realizar.

Por suerte, el elfo Pheralb ha detectado el patrón que ha seguido el grinch para desordenarlos. Nos ha escrito las reglas que debemos seguir para reordenar los paquetes. Las instrucciones que siguen son:

Recibirás un string que contiene letras y paréntesis.
Cada vez que encuentres un par de paréntesis, debes voltear el contenido dentro de ellos.
Si hay paréntesis anidados, resuelve primero los más internos.
Devuelve el string resultante con los paréntesis eliminados, pero con el contenido volteado correctamente.
Nos ha dejado algunos ejemplos:"""


def test(expected, received):
    if expected == received:
        return True
    
    return False


def fixPackages(packages):
    while "(" in packages:
        last_bracket_in = packages.rfind("(")
        first_bracket_out = packages.find(")")

        packages = packages[:last_bracket_in] + packages[last_bracket_in + 1:first_bracket_out][::-1] + packages[first_bracket_out + 1:]

        # Versión más visual
        """
        reversed_chain = packages[last_bracket_in + 1:first_bracket_out][::-1]
        packages = packages[:last_bracket_in] + packages[last_bracket_in + 1:first_bracket_out][::-1] + packages[first_bracket_out + 1:]
        """

    return packages


def main():
    print(test("abcde", fixPackages('a(cb)de')))
    # ➞ "abcde"
    # Volteamos "cb" dentro de los paréntesis

    print(test("agdefcbh", fixPackages('a(bc(def)g)h')))
    # ➞ "agdefcbh"
    # 1º volteamos "def" → "fed", luego volteamos "bcfedg" → "gdefcb"

    print(test("abcighfedjk", fixPackages('abc(def(gh)i)jk')))
    # ➞ "abcighfedjk"
    # 1º volteamos "gh" → "hg", luego "defhgi" → "ighfed"

    print(test("acbe", fixPackages('a(b(c))e')))
    # ➞ "acbe"
    # 1º volteamos "c" → "c", luego "bc" → "cb"

    print(test("acdgfebh", fixPackages('a(b(cd(efg)))h')))
    # ➞ "acdgfebh"

    print(test("defihgcba", fixPackages('(abc(def(ghi)))')))
    # ➞ "defihgcba"


if __name__ == "__main__":
    main()