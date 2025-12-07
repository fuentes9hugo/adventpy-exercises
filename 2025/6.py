"""En el taller de Santa, los elfos han encontrado una montaña de guantes mágicos totalmente desordenados. Cada guante viene descrito por dos valores:

hand: indica si es un guante izquierdo (L) o derecho (R)
color: el color del guante (string)
Tu tarea es ayudarles a emparejar guantes: Un par válido es un guante izquierdo y uno derecho del mismo color.

Debes devolver una lista con los colores de todos los pares encontrados. Ten en cuenta que puede haber varios pares del mismo color."""


def matchGloves(gloves):
    organized_gloves = {}
    for glove in gloves:
        if glove["color"] not in organized_gloves:
            organized_gloves[glove["color"]] = [0, 0]

        if glove["hand"] == "L":
            organized_gloves[glove["color"]][0] += 1

        else:
            organized_gloves[glove["color"]][1] += 1

    gloves_matched = [] # gloves[:] = [] -> Generalmente es mejor no modificar los argumentos
    for key, value in organized_gloves.items():
        gloves_to_append = [key] * min(value)
        gloves_matched.extend(gloves_to_append)

    return gloves_matched


def test(expected, received):
    return expected == received


def main():
    gloves = [
        { "hand": 'L', "color": 'red' },
        { "hand": 'R', "color": 'red' },
        { "hand": 'R', "color": 'green' },
        { "hand": 'L', "color": 'blue' },
        { "hand": 'L', "color": 'green' }
    ]

    print(test(["red", "green"], matchGloves(gloves)))
    # ["red", "green"]

    gloves2 = [
        { "hand": 'L', "color": 'gold' },
        { "hand": 'R', "color": 'gold' },
        { "hand": 'L', "color": 'gold' },
        { "hand": 'L', "color": 'gold' },
        { "hand": 'R', "color": 'gold' }
    ]

    print(test(["gold", "gold"], matchGloves(gloves2)))
    # ["gold", "gold"]

    gloves3 = [
        { "hand": 'L', "color": 'red' },
        { "hand": 'R', "color": 'green' },
        { "hand": 'L', "color": 'blue' }
    ]

    print(test([], matchGloves(gloves3)))
    # []

    print(test(["blue", "blue"], matchGloves([
        { "hand": 'R', "color": 'blue' },
        { "hand": 'L', "color": 'blue' },
        { "hand": 'R', "color": 'blue' },
        { "hand": 'L', "color": 'blue' },
        { "hand": 'L', "color": 'blue' }
    ])))
    # ["blue", "blue"]

    print(test(["green", "red"], matchGloves([
        { "hand": 'R', "color": 'green' },
        { "hand": 'L', "color": 'red' },
        { "hand": 'R', "color": 'red' },
        { "hand": 'L', "color": 'green' },
        { "hand": 'L', "color": 'red' }
    ])))
    # ["green", "red"]

    print(test([], matchGloves([
        { "hand": 'L', "color": 'green' },
        { "hand": 'L', "color": 'red' },
        { "hand": 'L', "color": 'red' },
        { "hand": 'L', "color": 'green' },
        { "hand": 'L', "color": 'red' }
    ])))
    # []

    print(test(["silver", "silver"], matchGloves([
        { "hand": 'L', "color": 'silver' },
        { "hand": 'L', "color": 'silver' },
        { "hand": 'R', "color": 'silver' },
        { "hand": 'R', "color": 'silver' },
        { "hand": 'R', "color": 'silver' }
    ])))
    #["silver", "silver"]


if __name__ == "__main__":
    main()