"""Los elfos 🧝🧝‍♂️ de Santa Claus han encontrado un montón de botas mágicas desordenadas en el taller. Cada bota se describe por dos valores:

type indica si es una bota izquierda (I) o derecha (R).
size indica el tamaño de la bota.
Tu tarea es ayudar a los elfos a emparejar todas las botas del mismo tamaño que tengan izquierda y derecha. Para ello, debes devolver una lista con los pares disponibles después de emparejar las botas.

¡Ten en cuenta que puedes tener más de una zapatilla emparejada del mismo tamaño!"""


def organizeShoes(shoes: list[dict]) -> list[int]:
    organized_shoes = {}
    for shoe in shoes:
        if shoe["size"] not in organized_shoes:
            organized_shoes[shoe["size"]] = [0, 0]
        
        if shoe["type"] == "I":
            organized_shoes[shoe["size"]][0] += 1
        
        else:
            organized_shoes[shoe["size"]][1] += 1
    
    shoes[:] = []
    for key, value in organized_shoes.items():
        shoes_to_append = [key] * min(value)
        shoes.extend(shoes_to_append)
            
    return shoes


def main():
    shoes = [
        { "type": 'I', "size": 38 },
        { "type": 'R', "size": 38 },
        { "type": 'R', "size": 42 },
        { "type": 'I', "size": 41 },
        { "type": 'I', "size": 42 }
    ]

    print(organizeShoes(shoes))
    # [38, 42]

    shoes2 = [
        { "type": 'I', "size": 38 },
        { "type": 'R', "size": 38 },
        { "type": 'I', "size": 38 },
        { "type": 'I', "size": 38 },
        { "type": 'R', "size": 38 }
    ]
    print(organizeShoes(shoes2))
    # [38, 38]

    shoes3 = [
        { "type": 'I', "size": 38 },
        { "type": 'R', "size": 36 },
        { "type": 'R', "size": 42 },
        { "type": 'I', "size": 41 },
        { "type": 'I', "size": 43 }
    ]

    print(organizeShoes(shoes3) )
    # []


if __name__ == "__main__":
    main()