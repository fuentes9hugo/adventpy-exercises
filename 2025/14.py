"""En el Polo Norte, los elfos han simplificado su sistema de almacenamiento para evitar errores.
Ahora guardan los regalos en un objeto mágico con profundidad limitada, donde cada valor aparece una sola vez.

Santa necesita una forma rápida de saber qué camino de claves debe seguir para encontrar un regalo concreto.

Tu tarea es escribir una función que, dado un objeto y un valor, devuelva el array de claves que hay que recorrer para llegar a ese valor.

Reglas:

- El objeto tiene como máximo 3 niveles de profundidad.
- El valor a buscar aparece como mucho una vez.
- El objeto solo contiene otros objetos y valores primitivos (strings, numbers, booleans).
- Si el valor no existe, devuelve un array vacío."""


def findGiftPath(workshop: dict, gift: str | int | bool) -> list[str]:
    for key, value in workshop.items():
        if isinstance(value, dict):
            lower_level = findGiftPath(value, gift)

            if lower_level:
                return [key] + lower_level
        
        if value == gift:
            return [key]
    
    return []


def test(expected, received):
    return expected == received


def main():
    workshop = {
        "storage": {
            "shelf": {
                "box1": 'train',
                "box2": 'switch'
            },
            "box": 'car'
        },
        "gift": 'doll'
    }

    print(test(['storage', 'shelf', 'box1'], findGiftPath(workshop, 'train')))
    # ➜ ['storage', 'shelf', 'box1']

    print(test(['storage', 'shelf', 'box2'], findGiftPath(workshop, 'switch')))
    # ➜ ['storage', 'shelf', 'box2']

    print(test(['storage', 'box'], findGiftPath(workshop, 'car')))
    # ➜ ['storage', 'box']

    print(test(["gift"], findGiftPath(workshop, 'doll')))
    # ➜ ['gift']

    print(test([], findGiftPath(workshop, 'plane')))
    # ➜ []


if __name__ == "__main__":
    main()