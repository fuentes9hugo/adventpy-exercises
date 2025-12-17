"""Este mes de diciembre hay películas super interesantes en el cine... y tengo que optimizar cómo gasto el dinero.

Mi cine favorito tiene dos posibilidades:

• Entrada de un sólo uso: Cuesta 12$ por cada película.

• Tarjeta de fidelidad: Cuesta 250$ pero que cada vez que vas pagas sólo el 75% del precio del ticket. ¡Lo mejor es que se acumula! Y cada vez que vas, se paga el 75% del precio del ticket que pagaste la última vez.
Ejemplo de cada una al comprar 3 entradas y el precio que pagaría en total:

# Entrada normal: 12$ * 3 = 36$
# Tarjeta fidelidad: 250$ + (12$ * 0,75) +  (12$ * 0,75 * 0,75) + (12$ * 0,75 * 0,75 * 0,75) = 270,8125$

Necesito una función que, al pasarle las veces que voy a ir al cine, me diga si vale la pena comprar la tarjeta fidelidad o no.

La dificultad del reto está en encontrar una fórmula sencilla que nos diga el precio con descuento acumulado para la tarjeta fidelidad."""


def should_buy_fidelity(times: int) -> bool:
    # Coding way
    """normal_ticket = 12 * times
    fidelity = 250
    fidelity_ticket_price = 12 * 0.75
    for _ in range(times):
        fidelity += fidelity_ticket_price
        fidelity_ticket_price *= 0.75
    
    return True if fidelity < normal_ticket else False"""

    # Algebraic way
    return True if 250 + 36 * (1 - 0.75**times) < 12 * times else False


def test(expected, received):
    return expected == received


def main():
    print(test(False, should_buy_fidelity(1))) # false -> Mejor comprar tickets de un sólo uso
    print(test(True, should_buy_fidelity(100))) # true -> Mejor comprar tarjeta fidelidad


if __name__ == "__main__":
    main()