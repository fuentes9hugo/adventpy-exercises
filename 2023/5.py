"""Santa 🎅 está probando su nuevo trineo eléctrico, el CyberReindeer, en una carretera del Polo Norte. La carretera se representa con una cadena de caracteres, donde:
- . = Carretera
- S = Trineo de Santa
- * = Barrera abierta
- | = Barrera cerrada

Ejemplo de carretera: S...|....|.....

Cada unidad de tiempo, el trineo avanza una posición a la derecha. Si encuentra una barrera cerrada, se detiene hasta que la barrera se abra. Si está abierta, la atraviesa directamente.

Todas las barreras empiezan cerradas, pero después de 5 unidades de tiempo, se abren todas para siempre.

Crea una función que simule el movimiento del trineo durante un tiempo dado y devuelva un array de cadenas representando el estado de la carretera en cada unidad de tiempo:

El resultado es un array donde cada elemento muestra la carretera en cada unidad de tiempo.

Ten en cuenta que si el trineo está en la misma posición que una barrera, entonces toma su lugar en el array.

Los elfos se inspiraron en este reto de Code Wars."""


def cyberReindeer(road: str, time: int) -> list[str]:
    result = [road]

    road = list(road)
    s_pos = road.index("S")

    road_len = len(road)

    current_step = "."

    for i in range(1, time):
        if s_pos == road_len - 1: break

        if i == 5:
            for step in range(road_len):
                if road[step] == "|": road[step] = "*"

        next_step = road[s_pos + 1]
        
        if next_step == "|" and i < 5:
            result.append("".join(road))
            continue

        road[s_pos] = current_step
        road[s_pos + 1] = "S"
        
        current_step = next_step

        result.append("".join(road))

        s_pos += 1

    return result


def test(e, r) -> bool:
    return e == r


def main():
    road = 'S..|...|..'
    time = 10 # unidades de tiempo
    result = cyberReindeer(road, time)

    expected_result = [
        'S..|...|..',
        '.S.|...|..',
        '..S|...|..',
        '..S|...|..',
        '..S|...|..',
        '...S...*..',
        '...*S..*..',
        '...*.S.*..',
        '...*..S*..',
        '...*...S..',
    ]

    print(test(expected_result, result))
    print(result)

    """ -> result:
    [
    'S..|...|..', // estado inicial
    '.S.|...|..', // avanza el trineo la carretera
    '..S|...|..', // avanza el trineo la carretera
    '..S|...|..', // el trineo para en la barrera
    '..S|...|..', // el trineo para en la barrera
    '...S...*..', // se abre la barrera, el trineo avanza
    '...*S..*..', // avanza el trineo la carretera
    '...*.S.*..', // avanza el trineo la carretera
    '...*..S*..', // avanza el trineo la carretera
    '...*...S..', // avanza por la barrera abierta
    ]
    """


if __name__ == "__main__":
    main()