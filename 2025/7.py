"""¡Es hora de decorar el árbol de Navidad 🎄! Escribe una función que reciba:

height → la altura del árbol (número de filas).
ornament → el carácter del adorno (por ejemplo, "o" o "@").
frequency → cada cuántas posiciones de asterisco aparece el adorno.
El árbol se dibuja con asteriscos *, pero cada frequency posiciones, el asterisco se reemplaza por el adorno.

El conteo de posiciones empieza en 1, desde la copa hasta la base, de izquierda a derecha. Si frequency es 2, los adornos aparecen en las posiciones 2, 4, 6, etc.

El árbol debe estar centrado y tener un tronco # de una línea al final."""


def drawTree(height, ornament, frequency):
    tree = []
    max_width = (height * 2) - 1
    ornament_to_draw = 1
    for i in range(height):
        chars_to_draw = (i + 1) * 2 - 1
        num_of_spaces = (max_width - chars_to_draw) // 2
        row_to_append = "" + " " * num_of_spaces

        j = 0
        while j != chars_to_draw:
            row_to_append += "*" if ornament_to_draw % frequency != 0 else f"{ornament}"
            ornament_to_draw += 1
            j += 1

        tree.append(row_to_append)
        
    tree.append(" " * (max_width // 2) + "#")
    tree = "\n".join(tree).rstrip("\n")

    return tree


def main():
    print(drawTree(5, 'o', 2))
    #     *
    #    o*o
    #   *o*o*
    #  o*o*o*o
    # *o*o*o*o*
    #     #

    print(drawTree(3, '@', 3))
    #   *
    #  *@*
    # *@**@
    #   #

    print(drawTree(4, '+', 1))
    #    +
    #   +++
    #  +++++
    # +++++++
    #    #

if __name__ == "__main__":
    main()