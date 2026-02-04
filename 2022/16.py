"""Papá Noel está empezando a recibir un montón de cartas pero tienen un montón de problemas de formato. Para mejorar la lectura, va a escribir un programa que, dado un texto, lo formatea de acuerdo a las siguientes reglas:
- Eliminar espacios al inicio y al final
- Eliminar múltiples espacios en blanco y dejar sólo uno
- Dejar un espacio después de cada coma
- Quitar espacios antes de coma o punto
- Las preguntas sólo deben terminar con un signo de interrogación
- La primera letra de cada oración debe estar en mayúscula
- Poner en mayúscula la palabra "Santa Claus" si aparece en la carta
- Poner un punto al final de la frase si no tiene puntuación

Las cartas las escriben inglés y aquí tenemos un ejemplo.

Atener en cuenta:
- No te tienes que preocupar por los signos de puntuación que no sean coma, punto o interrogación.
- Asegúrate de respetar los saltos de línea y espacios originales."""


def fixLetter(letter: str) -> str:
    letter = letter.strip()

    new_letter = [letter[0].upper()]

    for char in letter[1:]:
        if new_letter[-1] in (" ", ", ", ". ") and char == " ": continue

        if char == "," or char == "." : char += " "

        if char in (", ", ". ") and new_letter[-1] == " " or char == "?" and new_letter[-1] == "?": new_letter.pop()

        if new_letter[-1] == ". ": char = char.upper()

        if len(new_letter) >= 2:
            if new_letter[-2] == "?" or new_letter[-2] == "!":
                char = char.upper()

        new_letter.append(char)
    
    if new_letter[-1] != "?" and new_letter[-1] != "!": new_letter.append(".")

    return "".join(new_letter).replace("santa", "Santa").replace("claus", "Claus")


def test(expected, received):
    return expected == received


def main():
    print(test("Hello, how are you? Do you know if Santa Claus exists? I really hope he does! Bye.", fixLetter(" hello,  how are you??     do you know if santa claus exists?  i really hope he does!  bye  ")))
    # Hello, how are you? Do you know if Santa Claus exists? I really hope he does! Bye.

    print(test("Hi Santa Claus. I'm a girl from Barcelona, Spain. Please, send me a bike. Is it possible?", fixLetter("  Hi Santa claus. I'm a girl from Barcelona , Spain . please, send me a bike.  Is it possible?")))
    # Hi Santa Claus. I'm a girl from Barcelona, Spain. Please, send me a bike. Is it possible?

if __name__ == "__main__":
    main()