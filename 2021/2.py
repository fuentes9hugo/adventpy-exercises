"""Te ha llegado una carta ✉️ con todos los regalos que debes preparar. El tema es que es una cadena de texto y es muy difícil de leer 😱. ¡Menos mal que han puesto cada regalo separado por espacio! (aunque ten cuidado, porque al ser niños, igual han colado más espacios de la cuenta)

Encima nos hemos dado cuenta que algunas palabras vienen con un _ delante de la palabra, por ejemplo _playstation, que significa que está tachado y no se tiene que contar.

Transforma el texto a un objeto que contenga el nombre de cada regalo y las veces que aparece.

Ten en cuenta que los tests pueden ser más exhaustivos... 😝 ¡Cuidado con contar espacios vacíos!"""


def listGifts(letter):
    splitted_letter = letter.split()
    gifts_list = {}
    for gift in splitted_letter:
        if gift[0] == "_":
            continue

        if gift not in gifts_list:
            gifts_list[gift] = 0
        
        gifts_list[gift] += 1
    
    return gifts_list


def test(expected, received):
    return expected == received


def main():
    carta = 'bici coche balón _playstation bici coche peluche'
    expected = {
        "bici": 2,
        "coche":2,
        "balón":1,
        "peluche": 1
    }
    print(test(expected, listGifts(carta)))


if __name__ == "__main__":
    main()