"""Estás en un mercado muy especial en el que se venden árboles de Navidad 🎄. Cada uno viene decorado con una serie de adornos muy peculiares, y el precio del árbol se determina en función de los adornos que tiene.

*: Copo de nieve - Valor: 1
o: Bola de Navidad - Valor: 5
^: Arbolito decorativo - Valor: 10
#: Guirnalda brillante - Valor: 50
@: Estrella polar - Valor: 100
Normalmente se sumarían todos los valores de los adornos y ya está…

Pero, ¡ojo! Si un adorno se encuentra inmediatamente a la izquierda de otro de mayor valor, en lugar de sumar, se resta su valor."""


def calculatePrice(ornaments: str) -> int:
    ornaments_values = {
        "*": 1,
        "o": 5,
        "^": 10,
        "#": 50,
        "@": 100
    }

    total_value = 0
    last_value = 0

    for char in reversed(ornaments):
        if char not in ornaments_values:
            return None
        
        current_value = ornaments_values[char]

        if current_value < last_value:
            total_value -= current_value
        
        else:
            total_value += current_value
        
        last_value = current_value
    
    return total_value


def test(expected, received):
    return expected == received


def main():
    print(test(3, calculatePrice('***')))  # 3   (1 + 1 + 1)
    print(test(4, calculatePrice('*o')))   # 4   (5 - 1)
    print(test(6, calculatePrice('o*')))   # 6   (5 + 1)
    print(test(5, calculatePrice('*o*')))  # 5  (-1 + 5 + 1) 
    print(test(6, calculatePrice('**o*'))) # 6  (1 - 1 + 5 + 1) 
    print(test(8, calculatePrice('o***'))) # 8   (5 + 3)
    print(test(94, calculatePrice('*o@')))  # 94  (-5 - 1 + 100)
    print(test(49, calculatePrice('*#')))   # 49  (-1 + 50)
    print(test(300, calculatePrice('@@@')))  # 300 (100 + 100 + 100)
    print(test(50, calculatePrice('#@')))   # 50  (-50 + 100)
    print(test(None, calculatePrice('#@Z')))  # undefined (Z es desconocido)


if __name__ == "__main__":
    main()