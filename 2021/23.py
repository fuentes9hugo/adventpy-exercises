"""Estamos en la fábrica de Santa Claus 🎅 creando regalos como si no hubiera un mañana.

Pensábamos que no íbamos a llegar pero Jelf Bezos ha tenido una idea genial para aprovechar las máquinas y optimizar al máximo la creación de regalos. 🎁

La configuración de las máquinas es un string. Podemos reconfigurarla para que haga otro regalo y, para ello, podemos cambiar cada carácter por otro.

Pero tiene limitaciones 🥲: al reemplazar el carácter se debe mantener el orden, no se puede asignar al mismo carácter a dos letras distintas (pero sí a si mismo) y, claro, la longitud del string debe ser el mismo.

Necesitamos una función que nos diga si podemos reconfigurar una máquina para que de un regalo pueda pasar a fabricar otro según las reglas mencionadas. Lo mejor es que veamos un ejemplo."""


def canReconfigure(from_gift: str, to_gift: str) -> bool:
    if len(from_gift) != len(to_gift): return False

    from_to = {}
    to_from = {}
    for char_from, char_to in zip(from_gift, to_gift):
        if char_from in from_to and from_to.get(char_from) != char_to or char_to in to_from and to_from.get(char_to) != char_from:
            return False

        from_to[char_from] = char_to
        to_from[char_to] = char_from

    return True


def test(expected, received):
    return expected == received


def main():
    from_gift = 'BAL'
    to_gift   = 'LIB'
    print(test(True, canReconfigure(from_gift, to_gift))) # true
    """ la transformación sería así:
    B -> L
    A -> I
    L -> B
    """

    from_gift = 'CON'
    to_gift   = 'JUU'
    print(test(False, canReconfigure(from_gift, to_gift))) # false
    """ no se puede hacer la transformación:
    C -> J
    O -> U
    N -> FALLO
    """

    from_gift = 'XBOX'
    to_gift   = 'XXBO'
    print(test(False, canReconfigure(from_gift, to_gift))) # false
    """ no se puede hacer la transformación:
    X -> X
    B -> X (FALLO, no mantiene el orden de transformación y la B no puede asignarse a la X que ya se asignó a otra) 
    O -> B
    X -> O (FALLO, la X no puede asignarse a la O que ya se asignó a la X)
    """

    from_gift = 'XBOX'
    to_gift   = 'XOBX'
    print(test(True, canReconfigure(from_gift, to_gift))) # true

    from_gift = 'MMM'
    to_gift   = 'MID'
    print(test(False, canReconfigure(from_gift, to_gift))) # false
    """ no se puede hacer la transformación:
    M -> M (BIEN, asigna el mismo carácter a si mismo)
    M -> I (FALLO, asigna el mismo carácter a dos letras distintas)
    M -> D (FALLO, asigna el mismo carácter a dos letras distintas)
    """

    from_gift = 'AA'
    to_gift   = 'MID'
    print(test(False, canReconfigure(from_gift, to_gift))) # false -> no tiene la misma longitud


if __name__ == "__main__":
    main()