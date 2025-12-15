"""Santa Claus 🎅 está revisando la lista de regalos que debe entregar esta Navidad. Sin embargo, algunos regalos faltan, otros están duplicados, y algunos tienen cantidades incorrectas. Necesita tu ayuda para resolver el problema.

Recibirás dos arrays:

received: Lista con los regalos que Santa tiene actualmente.
expected: Lista con los regalos que Santa debería tener.
Tu tarea es escribir una función que, dado received y expected, devuelva un objeto con dos propiedades:

missing: Un objeto donde las claves son los nombres de los regalos faltantes y los valores son las cantidades que faltan.
extra: Un objeto donde las claves son los nombres de los regalos extra o duplicados y los valores son las cantidades que sobran.
Ten en cuenta que:

Los regalos pueden repetirse en ambas listas.
Las listas de regalos están desordenadas.
Si no hay regalos que falten o sobren, las propiedades correspondientes (missing o extra) deben ser objetos vacíos."""


def fixGiftList(received: list[str], expected: list[str]) -> dict[str, int]:
    match = False
    received_not_match = []
    for gift_received in received:
        for gift_expected in expected:
            if gift_received == gift_expected:
                match = True
                expected.remove(gift_expected)
                break
        if match:
            match = False
            continue
        received_not_match.append(gift_received)

    gifts_to_fix = {
        "missing": {},
        "extra": {}
    }

    for gift in expected:
        if gift not in gifts_to_fix["missing"]:
            gifts_to_fix["missing"][gift] = expected.count(gift)
            
    for gift in received_not_match:
        if gift not in gifts_to_fix["extra"]:
            gifts_to_fix["extra"][gift] = received_not_match.count(gift)
    
    return gifts_to_fix


def test(expected, received):
    return expected == received


def main():
    print(test({ "missing": { "ball": 1 }, "extra": { "car": 1 } }, fixGiftList(['puzzle', 'car', 'doll', 'car'], ['car', 'puzzle', 'doll', 'ball'])))
    # Devuelve:
    # {
    #   missing: { ball: 1 },
    #   extra: { car: 1 }
    # }

    print(test({ "missing": { "ball": 1, "kite": 1 }, "extra": { "train": 1 } }, fixGiftList(
    ['book', 'train', 'kite', 'train'],
    ['train', 'book', 'kite', 'ball', 'kite']
    )))
    # Devuelve:
    # {
    #   missing: { ball: 1, kite: 1 },
    #   extra: { train: 1 }
    # }

    print(test({ "missing": { "puzzle": 1, "car": 2 }, "extra": {} }, fixGiftList(
    ['bear', 'bear', 'car'],
    ['bear', 'car', 'puzzle', 'bear', 'car', 'car']
    )))
    # Devuelve:
    # {
    #   missing: { puzzle: 1, car: 2 },
    #   extra: {}
    # }

    print(test({ "missing": {}, "extra": {} }, fixGiftList(['bear', 'bear', 'car'], ['car', 'bear', 'bear'])))
    # Devuelve:
    # {
    #   missing: {},
    #   extra: {}
    # }


if __name__ == "__main__":
    main()