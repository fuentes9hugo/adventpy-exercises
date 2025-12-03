"""En el taller de Santa hay un elfo becario que está aprendiendo a envolver regalos 🎁.

Le han pedido que envuelva cajas usando solo texto… y lo hace más o menos bien.

Le pasan dos parámetros:

size: el tamaño del regalo cuadrado
symbol: el carácter que el elfo usa para hacer el borde (cuando no se equivoca 😅)
El regalo debe cumplir:

Debe ser un cuadrado de size x size.
El interior siempre está vacío (lleno de espacios), porque el elfo "aún no sabe dibujar el relleno".
Si size < 2, devuelve una cadena vacía: el elfo lo intentó, pero se le perdió el regalo.
El resultado final debe ser un string con saltos de línea \n.
Sí, es un reto fácil… pero no queremos que despidan al becario. ¿Verdad?"""


def drawGift(size, symbol):
    if size < 2:
        return ""
    
    gift = []
    for row in range(size):
        if row not in (0, size - 1):
            gift.append(f"{symbol}" + " " * (size - 2) + f"{symbol}")
            continue

        gift.append(f"{symbol}" * size)

    return "\n".join(gift)


def main():
    g1 = drawGift(4, '*')
    print(g1)
    """
    ****
    *  *
    *  *
    ****
    """

    g2 = drawGift(3, '#')
    print(g2)
    """
    ###
    # #
    ###
    """

    g3 = drawGift(2, '-')
    print(g3)
    """
    --
    --
    """

    g4 = drawGift(1, '+')
    print(g4)
    # ""  pobre becario…


if __name__ == "__main__":
    main()