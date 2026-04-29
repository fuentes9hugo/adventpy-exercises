"""Santa está experimentando con nuevos diseños de regalos y necesita tu ayuda para visualizarlos en 3D.

Tu tarea es escribir una función que, dado un tamaño n (entero), genere un dibujo de un regalo en 3D utilizando caracteres ASCII.

Las líneas de los regalos se dibujan con # y las caras con el símbolo que nos pasan como parámetro.

Importante: Nos han dicho que siempre hay que dejar un salto de línea al final del dibujo.

Nota: Ten en cuenta que, en los tests, la primera línea se ve empujada por el caracter "."""


def drawGift(size: int, symbol: str) -> str:
    if size == 1: return "#\n"

    lines = []

    lines.append(" " * (size - 1) + "#" * size)

    for i in range(1, size - 1):
        spaces = " " * (size - 1 - i)
        front_face = symbol * (size - 2)
        side_face = symbol * (i - 1)

        lines.append(f"{spaces}#{front_face}#{side_face}#")

    lines.append("#" * size + symbol * (size - 2) + "#")

    for i in range(size - 2, 0, -1):
        front_face = symbol * (size - 2)
        side_face = symbol * (i - 1)
        
        lines.append(f"#{front_face}#{side_face}#")

    lines.append("#" * size)

    return "\n".join(lines) + "\n"


def main():
    print(drawGift(4, '+'))
    """
       ####
      #++##
     #++#+#
    ####++#
    #++#+#
    #++##
    ####
    """

    print(drawGift(5, '*'))
    """
        #####
       #***##
      #***#*#
     #***#**#
    #####***#
    #***#**#
    #***#*#
    #***##
    #####
    """

    print(drawGift(1, '^'))
    """
    #
    """


if __name__ == "__main__":
    main()