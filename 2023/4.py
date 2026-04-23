"""En el taller de Santa 🎅, algunos mensajes navideños han sido escritos de manera peculiar: las letras dentro de los paréntesis deben ser leídas al revés

Santa necesita que estos mensajes estén correctamente formateados. Tu tarea es escribir una función que tome una cadena de texto y revierta los caracteres dentro de cada par de paréntesis, eliminando los paréntesis en el mensaje final.

Eso sí, ten en cuenta que pueden existir paréntesis anidados, por lo que debes invertir los caracteres en el orden correcto.

Notas:
- Las cadenas de entrada siempre estarán bien formadas con paréntesis que coinciden correctamente, no necesitas validarlos.
- En el mensaje final no deben quedar paréntesis.
- El nivel máximo de anidamiento es 2."""


def decode(message: str) -> str:
    while "(" in message:
        start_bracket = message.rfind("(")
        end_bracket = message.find(")", start_bracket)
        # end_bracket = start_bracket + message[start_bracket:].find(")")

        # reversed string it's the same as => message[start_bracket + 1:end_bracket][::-1]
        message = message[:start_bracket] + message[end_bracket - 1:start_bracket:-1] + message[end_bracket + 1:]

    return message



def test(e, r) -> bool:
    return e == r


def main():
    a = decode('hola (odnum)')
    print(test("hola mundo", (a))) # hola mundo

    b = decode('(olleh) (dlrow)!')
    print(test("hello world!", (b))) # hello world!

    c = decode('sa(u(cla)atn)s')
    print(test("santaclaus", (c))) # santaclaus

    # Paso a paso:
    # 1. Invertimos el anidado -> sa(ualcatn)s
    # 2. Invertimos el que queda -> santaclaus


if __name__ == "__main__":
    main()