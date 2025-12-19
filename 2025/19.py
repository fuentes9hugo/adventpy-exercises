"""¡El GPS del trineo se ha vuelto loco! 😱 Papá Noel tiene los tramos de su viaje, pero están todos desordenados.

Tu misión es reconstruir la ruta completa desde el origen hasta el destino final.

Ten en cuenta: El primer elemento del array es siempre el primer tramo del viaje. A partir de ahí, debes ir conectando los destinos con los siguientes orígenes.

🔎 A tener en cuenta:

- No hay rutas duplicadas ni ciclos en el camino de Papá Noel.
- Puede haber tramos que no pertenezcan a la ruta; estos deben ignorarse."""


def revealSantaRoute(routes: list[list[str]]) -> list[str]:
    routes_map = {route[0]: route[1] for route in routes}

    corrected_routes = []
    next_route = routes[0][0]

    while next_route:
        corrected_routes.append(next_route)
        next_route = routes_map.get(next_route)
    
    return corrected_routes


def test(expected, received):
    return expected == received


def main():
    print(test(['MEX', 'CAN', 'UK', 'GER'], revealSantaRoute([
        ['MEX', 'CAN'],
        ['UK', 'GER'],
        ['CAN', 'UK']
    ])))
    # → ['MEX', 'CAN', 'UK', 'GER']

    print(test(['USA', 'BRA', 'UAE', 'JPN', 'PHL'], revealSantaRoute([
        ['USA', 'BRA'],
        ['JPN', 'PHL'],
        ['BRA', 'UAE'],
        ['UAE', 'JPN'],
        ['CMX', 'HKN']
    ])))
    # → ['USA', 'BRA', 'UAE', 'JPN', 'PHL']

    print(test(['STA', 'HYD'], revealSantaRoute([
        ['STA', 'HYD'],
        ['ESP', 'CHN']
    ])))
    # → ['STA', 'HYD']

    print(test(['A', 'B'], revealSantaRoute([["A", "B"], ["C", "D"], ["E", "F"], ["G", "H"]])))
    # → ['A', 'B']


if __name__ == "__main__":
    main()