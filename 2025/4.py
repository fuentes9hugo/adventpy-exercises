"""Los elfos han encontrado el código cifrado que protege la puerta del taller de Santa 🔐.
El PIN tiene 4 dígitos, y está escondido dentro de bloques como estos:

[1++][2-][3+][<]

Escribe una función que descifre el PIN a partir del código.

El código está formado por bloques entre corchetes [...] y cada bloque genera un dígito del PIN.

Un bloque normal tiene la forma [nOP...], donde n es un número (0-9) y después puede haber una lista de operaciones (opcionales).

Las operaciones se aplican en orden al número y son:

+ suma 1
- resta 1
El resultado siempre es un dígito (aritmética mod 10), por ejemplo 9 + 1 → 0 y 0 - 1 → 9.

También existe el bloque especial [<], que repite el dígito del bloque anterior.

Si al final hay menos de 4 dígitos, se debe devolver null."""


def test(expected, received):
    if expected == received:
        return True
    
    return False


def decodeSantaPin(code: str) -> str:
    if code.count("[") < 4:
        return None
    
    digits = [str(n) for n in range(10)]
    operations_map = {
        "+": 1,
        "-": -1
    }
    
    decoded = []
    digit_to_append = 0

    for char in code:
        if char == "]":
            decoded.append(str(digit_to_append))

        elif char in digits:
            digit_to_append = int(char)

        elif char in operations_map:
            digit_to_append = (digit_to_append + operations_map[char]) % 10

    return "".join(decoded)


def main():
    print(test("3144", decodeSantaPin('[1++][2-][3+][<]')))
    # "3144"

    print(test("0944", decodeSantaPin('[9+][0-][4][<]')))
    # "0944"

    print(test(None, decodeSantaPin('[1+][2-]')))
    # null (solo 2 dígitos)
    
    
if __name__ == "__main__":
    main()