"""Las empresas de paquetería 📦 se preparan para la época de fiestas y la locura de envíos que les espera.

La empresa funciona con flotas de furgonetas 🚛 y camiones 🚚. Las flotas tienen un organigrama, ya que existen rangos de nivel de experiencia.

Necesitamos saber el número de paquetes que una persona va a poder gestionar en un día. Para ello se cuenta el número de paquetes que puede llevar esa persona y todos los transportistas que tiene en su equipo. Lo malo es que los datos están almacenados de una forma un poco rara en un array:

El array contiene otros arrays que contienen los datos de cada transportista
transportista[0] -> Nombre/ID del Transportista
transportista[1] -> Paquetes que gestiona en un día
transportista[2] -> Array con sus subordinados

Para que lo veamos en código, tanto el array, como la función de dos parámetros para conseguir el número deseado.

¡Ten cuidado! Como has visto en el segundo ejemplo, el organigrama puede tener diferentes niveles y además nos viene información que puede ser que no necesitemos. Debemos tener en cuenta el parámetro de carrierID para calcular bien el número y contar todo su equipo."""


def countPackages(carriers: list[list], carrierID: str) -> int:
    carriers_map = {carrier[0]: carrier[1:] for carrier in carriers}

    packages_ammount = carriers_map[carrierID][0]

    for subordinate in carriers_map[carrierID][1]:
        packages_ammount += countPackages(carriers, subordinate)
    
    return packages_ammount


def test(expected, received):
    return expected == received


def main():
    carriers = [
        ['dapelu', 5, ['midu', 'jelowing']],
        ['midu', 2, []],
        ['jelowing', 2, []]
    ]

    print(test(9, countPackages(carriers, 'dapelu'))) # 9
    # 5 de dapelu, 2 de midu y 2 de jelowing = 9

    carriers2 = [
        ['lolivier', 8, ['camila', 'jesuspoleo']],
        ['camila', 5, ['sergiomartinez', 'conchaasensio']],
        ['jesuspoleo', 4, []],
        ['sergiomartinez', 4, []],
        ['conchaasensio', 3, ['facundocapua', 'faviola']],
        ['facundocapua', 2, []],
        ['faviola', 1, []]
    ]

    print(test(15, countPackages(carriers2, 'camila'))) # 15
    # 5 de camila, 4 de sergiomartinez, 3 de conchaasensio, 2 de facundocapua y 1 de faviola = 15


if __name__ == "__main__":
    main()