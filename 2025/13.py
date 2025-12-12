"""Simula el recorrido de un regalo dentro de una fábrica y devuelve cómo termina. Para ello debes crear una función runFactory(factory).

factory es un string[] donde cada celda puede ser:

> < ^ v movimientos
. salida correcta
Ten en cuenta que todas las filas tienen la misma longitud y que no habrá otros símbolos.

El regalo siempre empieza en la posición (0,0) (arriba a la izquierda). En cada paso lee la celda actual y se mueve según la dirección. Si llega a una celda con un punto (.) significa que ha salido correctamente de la fábrica.

Resultado

Devuelve uno de estos valores:

'completed' si llega a un .
'loop' si visita una posición dos veces
'broken' si sale fuera del tablero"""


def runFactory(factory: list[str]) -> str:
    pass


def test(expected, received):
    return expected == received


def main():
    print(test("completed", runFactory([
        '>>.'
    ]))) # 'completed'

    print(test("broken", runFactory([
        '>>>'
    ]))) # 'broken'

    print(test("loop", runFactory([
        '>><'
    ]))) # 'loop'

    print(test("completed", runFactory([
        '>>v',
        '..<'
    ]))) # 'completed'

    print(test("broken", runFactory([
        '>>v',
        '<<<'
    ]))) # 'broken'

    print(test("completed", runFactory([
        '>v.',
        '^..'
    ]))) # 'completed'

    print(test("loop", runFactory([
        'v.',
        '^.'
    ]))) # 'loop'


if __name__ == "__main__":
    main()