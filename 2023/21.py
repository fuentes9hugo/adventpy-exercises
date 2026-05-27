"""Los elfos están recibiendo mensajes binarios extraños desde Marte 🪐. ¿Los extraterrestres están tratando de comunicarse con ellos? 👽

El mensaje que llega es un array de 0s y 1s. Parece que han encontrado un patrón… Para asegurarse, quieren encontrar el segmento más largo de la cadena donde el número de 0s y 1s sea igual.

Ten en cuenta que si hay más de un patrón equilibrado, debes devolver el más largo y el primero que encuentres de izquierda a derecha.

Dicen que si encuentran el patrón, podrán enviar un mensaje de vuelta a Marte 🚀. Parece ser que tienen que enviarlos a https://mars.codes."""


def findBalancedSegment(message: list[int]) -> list[int]:
    accumulated = 0

    accumulated_map = {accumulated: -1}

    longest_range = []
    max_length = 0

    for i, num in enumerate(message):
        accumulated += -1 if num == 0 else 1

        if accumulated not in accumulated_map:
            accumulated_map[accumulated] = i
        
        else:
            first_index = accumulated_map[accumulated] + 1
            current_length = i - first_index + 1

            if current_length > max_length:
                max_length = current_length
                longest_range = [first_index, i]

    return longest_range


def test(e, r) -> bool:
    return e == r


def main():
    print(findBalancedSegment([1, 1, 0, 1, 1, 0, 1, 1]))
    #                                |________|
    #  posición del segmento:          [2, 5]
    #  más largo equilibrado
    #  de 0s y 1s
    print(test([2, 5], findBalancedSegment([1, 1, 0, 1, 1, 0, 1, 1])))

    print(findBalancedSegment([1, 1, 0]))
    #                             |__|
    #                            [1, 2]
    print(test([1, 2], findBalancedSegment([1, 1, 0])))

    print(findBalancedSegment([1, 1, 1]))
    #  no hay segmentos equilibrados: []
    print(test([], findBalancedSegment([1, 1, 1])))


if __name__ == "__main__":
    main()