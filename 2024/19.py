"""¡Se acerca el día para repartir regalos! Necesitamos apilar los regalos que transportaremos en el trineo 🛷 y para eso los vamos a meter en cajas 📦.

Los regalos se pueden meter en 4 cajas distintas, donde cada caja soporta 1, 2, 5, 10 de peso y se representan así:

    _
1: |_|
    _____
2: |_____|
    _____
5: |     |
   |_____|
     _________
10: |         |
    |_________|

# Representación en Python:
boxRepresentations = {
  1: [" _ ", "|_|"],
  2: [" ___ ", "|___|"],
  5: [" _____ ", "|     |", "|_____|"],
  10: [" _________ ", "|         |", "|_________|"]
}

Tu misión es que al recibir el peso de los regalos, uses las mínimas cajas posibles y que, además, las apiles de menos peso (arriba) a más peso (abajo). Siempre alineadas a la izquierda.

Además, ten en cuenta que al apilarlas, se reusa el borde inferior de la caja.

Nota: ¡Ten cuidado con los espacios en blanco! No añadas espacios en blanco a la derecha de una caja si no son necesarios."""


def distributeWeight(weight: int) -> str:
    box_representations = {
        1: [" _ ", "|_|"],
        2: [" ___ ", "|___|"],
        5: [" _____ ", "|     |", "|_____|"],
        10: [" _________ ", "|         |", "|_________|"]
    }

    def boxes(weight):
        while weight > 0:
            for box in reversed(box_representations.keys()):
                if box <= weight:
                    weight -= box
                    yield box, weight
                    break
    
    final_boxes = []
    last_box_top = ""
    for box, w in boxes(weight):
        box = box_representations[box]
        if not final_boxes and w != 0:
            final_boxes.append("\n".join(box[1:]))
            last_box_top = box[0]
            continue
        
        box_len = len(box[-1])
        box[-1] += last_box_top[box_len:]
        final_boxes.append("\n".join(box[1:])) if w != 0 else final_boxes.append("\n".join(box))
        last_box_top = box[0]

    final_boxes.reverse()
    
    return "\n".join(final_boxes)


def main():
    print(distributeWeight(1))
    # Devuelve:
    #  _
    # |_|

    print(distributeWeight(2))
    # Devuelve:
    #  ___
    # |___|

    print(distributeWeight(3))
    # Devuelve:
    #  _
    # |_|_
    # |___|

    print(distributeWeight(4))
    # Devuelve:
    #  ___
    # |___|
    # |___|

    print(distributeWeight(5))
    # Devuelve:
    #  _____
    # |     |
    # |_____|

    print(distributeWeight(6))
    # Devuelve:
    #  _
    # |_|___
    # |     |
    # |_____|

    print(distributeWeight(7))

    print(distributeWeight(18))

    print(distributeWeight(121))


if __name__ == "__main__":
    main()