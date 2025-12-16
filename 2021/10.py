"""Para mejorar la productividad de la tienda en la que trabajamos, vamos a crear una pequeña máquina que calcula el mínimo número de monedas que debemos usar para dar el cambio de una compra en metálico.

Las monedas para cambio que puedes usar son estas:

coins[0] = 1 céntimo
coins[1] = 2 céntimos
coins[2] = 5 céntimos
coins[3] = 10 céntimos
coins[4] = 20 céntimos
coins[5] = 50 céntimos

Tenemos que crear una función que recibe el número de céntimos que hay que devolver al cliente y la función nos da un array con la combinación de monedas mínimas que debemos usar para conseguirlo.

La dificultad del reto está en saber utilizar correctamente una estructura que te permita conocer las monedas que tienes disponible para crear el array con la devolución, ya que debes usar siempre el menor número de monedas posible. ¡Suerte 👩‍💻👨‍💻!"""


def get_coins(change: int) -> list[int]:
    give_coins = [0, 0, 0, 0, 0, 0]

    if change == 0: return give_coins

    coins = { 0: 1, 1: 2, 2: 5, 3: 10, 4: 20, 5: 50 }
    
    for key, value in reversed(coins.items()):
        if value <= change:
            coins_num, change = divmod(change, value)
            give_coins[key] += coins_num
        
        if change == 0: break
    
    return give_coins


def test(expected, received):
    return expected == received


def main():
    print(test([1, 0, 0, 0, 0, 1], get_coins(51))) # [1, 0, 0, 0, 0, 1] -> una moneda de 1 céntimo y otra de 50 céntimos
    print(test([1, 1, 0, 0, 0, 0], get_coins(3))) # [1, 1, 0, 0, 0, 0] -> una moneda de 1 céntimo y otra de 2
    print(test([0, 0, 1, 0, 0, 0], get_coins(5))) # [0, 0, 1, 0, 0, 0] -> una moneda de 5 céntimos
    print(test([1, 0, 1, 1, 0, 0], get_coins(16))) # [1, 0, 1, 1, 0, 0] -> una moneda de 1 céntimo, una de 5 y una de 10
    print(test([0, 0, 0, 0, 0, 2], get_coins(100))) # [0, 0, 0, 0, 0, 2] -> dos monedas de 50 céntimos


if __name__ == "__main__":
    main()