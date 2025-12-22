"""Lara Eloft ha encontrado unos restos élficos en una cueva, cerca del Círculo Polar Ártico, a 8 km al norte de Rovaniemi.

Ahora se encuentra descifrando unas misteriosas cartas que contiene información sobre unos números que le puede hacer llegar al próximo objetivo.

Lara tiene un documento que contiene una serie de números que pueden ser usados para descifrarlos:

Símbolo       Valor
  .             1
  ,             5
  :             10
  ;             50
  !             100

Lara, además, ha notado una cosa. Los símbolos se restan si están inmediatamente a la izquierda de otro mayor. 😱

Tenemos que crear una función que nos pasa una cadena de texto con símbolos y tenemos que transformarlo al número correcto. ¡Ojo! Si encuentras un símbolo que no entendemos, mejor que devolvamos None"""


def decodeNumbers(symbols: str) -> int | None:
    symbols_map = {
        ".": 1,
        ",": 5,
        ":": 10,
        ";": 50,
        "!": 100
    }

    result = 0
    next_sym_value = 0

    for sym in reversed(symbols):
        sym_value = symbols_map.get(sym)

        if not sym_value: return None
        
        result += sym_value * -1 if next_sym_value > sym_value else sym_value
        
        next_sym_value = sym_value

    return result


def test(expected, received):
    return expected == received


def main():
    print(test(3, decodeNumbers('...'))) # 3
    print(test(4, decodeNumbers('.,'))) # 4 (5 - 1)
    print(test(6, decodeNumbers(',.'))) # 6 (5 + 1)
    print(test(8, decodeNumbers(',...'))) # 8 (5 + 3)
    print(test(107, decodeNumbers('.........!'))) # 107 (1 + 1 + 1 + 1 + 1 + 1 + 1 - 1 + 100)
    print(test(49, decodeNumbers('.;'))) # 49 (50 - 1)
    print(test(5, decodeNumbers('..,'))) # 5 (-1 + 1 + 5)
    print(test(95, decodeNumbers('..,!'))) # 95 (1 - 1 - 5 + 100)
    print(test(49, decodeNumbers('.;!'))) # 49 (-1 -50 + 100)
    print(test(300, decodeNumbers('!!!'))) # 300
    print(test(50, decodeNumbers(';!'))) # 50
    print(test(None, decodeNumbers(';.W'))) # NaN


if __name__ == "__main__":
    main()