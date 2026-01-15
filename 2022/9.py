"""Una empresa que fabrica luces de Navidad nos ha pedido que le echemos una mano.

Tienen unas tiras led que son como un Array. Cada posición es un led y puede ser estar encendido (1) o apagado (0).

Cada 7 segundos, los leds cambian de estado de esta forma:
- Si el led está apagado, se enciende si el led de su izquierda (index - 1) estaba encendido antes.
- Si el led está encendido, se mantiene siempre encendido.

Nos han pedido un programa que nos diga cuantos segundos deben pasar hasta que todos los leds están encendidos. Los segundos se expresan en un número entero.

A tener en cuenta
- El array siempre tendrá al menos un led encendido.
- El array puede tener cualquier longitud.
- Si todos los leds están encendidos, el tiempo es 0."""

def countTime(leds: list[int]) -> int:
    time_ammount = 0
    while not all(led == 1 for led in leds):
        # leds_to_change = [i for i in range(len(leds)) if leds[-1 + i] == 1 and leds[i] == 0]
        
        for index in [i for i in range(len(leds)) if leds[-1 + i] == 1 and leds[i] == 0]:
            leds[index] = 1

        time_ammount += 7
    
    return time_ammount

def test(e, r):
    return e == r


def main():
    leds = [0, 1, 1, 0, 1]
    print(test(7, countTime(leds))) # 7
    # 7 segundos ya que en el primer cambio
    # todas las luces se encendieron
    # 0s: [0, 1, 1, 0, 1]
    # 7s: [1, 1, 1, 1, 1]

    print(test(21, countTime([0, 0, 0, 1]))) # 21
    # 21 segundos ya que necesita tres cambios:
    # 0s: [0, 0, 0, 1]
    # 7s: [1, 0, 0, 1]
    # 14s: [1, 1, 0, 1]
    # 21s: [1, 1, 1, 1]

    print(test(28, countTime([0, 0, 1, 0, 0]))) # 28
    # 28 segundos ya que necesita cuatro cambios:
    # 0s: [0, 0, 1, 0, 0]
    # 7s: [0, 0, 1, 1, 0]
    # 14s: [0, 0, 1, 1, 1]
    # 21s: [1, 0, 1, 1, 1]
    # 28s: [1, 1, 1, 1, 1]


if __name__ == "__main__":
    main()