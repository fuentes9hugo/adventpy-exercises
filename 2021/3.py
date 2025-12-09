"""El Grinch está abriendo las cartas que iban a Santa Claus y las está dejando hechas un lío. 😱

Las cartas son una cadena de texto que incluyen regalos y paréntesis ().

Para saber si una carta es válida ✅, debes comprobar que los paréntesis cierran correctamente y que, además, no vayan vacíos.

¡Pero ojo! Porque el Grinch ha dejado llaves { y corchetes [ dentro de los paréntesis que hacen que no sean válidas. Por suerte sólo los ha dejado en medio de los paréntesis...

Crea una función que pasándole el texto de la carta, devuelva true si es válida y false si no lo es. ¡Y acaba con la travesura del Grinch!"""


def isValid(letter: str):
    if "{" in letter or "[" in letter:
        return False
    
    splitted_letter = letter.split()
    for gift in splitted_letter:
        if ("(" in gift and ")" not in gift) or ("(" not in gift and ")" in gift):
            return False
        
        gift = gift.replace("(", "").replace(")", "")
        if not gift:
            return False
        
    return True


def test(expected, received):
    return expected == received


def main():
    print(test(True, isValid("bici coche (balón) bici coche peluche")))
    print(test(True, isValid("(muñeca) consola bici")))
    print(test(False, isValid("bici coche (balón bici coche")))
    print(test(False, isValid("peluche (bici [coche) bici coche balón")))
    print(test(False, isValid("(peluche {) bici")))
    print(test(False, isValid("() bici")))


if __name__ == "__main__":
    main()