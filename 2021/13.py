"""¡Hay demasiados regalos 🎁! Y envolverlos es una locura...

Vamos a crear una función que pasándole un array de regalos, nos devuelva otro array pero donde todos los regalos han sido envueltos con asteriscos tanto por arriba como por los lados.

Sólo tienes que tener en cuenta unas cosillas ✌️:

Si el array está vacío, devuelve un array vacío
Los regalos son emojis 🎁... por lo que tenlo en cuenta a la hora de contar su longitud...
Por suerte, cada posición del array siempre tiene la misma longitud..."""


def wrapGifts(gifts):
    width = len(max(gifts, key=len))
    wrap_limit = "*" * (width + 2)
    gifts_wrapped = [wrap_limit if i == -1 or i == len(gifts) else "*" + gifts[i] + "*" for i in range(-1, len(gifts) + 1)]
    
    return "\n".join(gifts_wrapped)


def main():
    print(wrapGifts(["#", "#"]))
    """Resultado:
    [ '****',
    '*📷*',
    '*⚽️*',
    '****'
    ]
    """

    print(wrapGifts(["##", "##"]))
    """Resultado:
    [ '******',
    '*🏈🎸*',
    '*🎮🧸*',
    '******'
    ]
    """

    print(wrapGifts(["####"]))
    """Resultado:
    [ '****',
    '*📷*',
    '****'
    ]
    """


if __name__ == "__main__":
    main()