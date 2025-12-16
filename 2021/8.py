"""Invertir en criptomonedas es casi un deporte de riesgo. El otro día hackearon Bitmart y ha hecho que el valor de Bitcoin, y otras monedas, bajase un 25%.

Vamos a escribir una función que reciba la lista de precios de una criptomoneda en un día y debemos devolver la ganancia máxima que podríamos sacar si compramos y vendemos la inversión el mismo día.

La lista de precios es un array de números y representa el tiempo de izquierda a derecha. Por lo que ten en cuenta que no puedes comprar a un precio que esté a la derecha de la venta y no puedes vender a un precio que esté a la izquierda de la compra.

Si ese día no se puede sacar ningún beneficio, tenemos que devolver -1 para evitar que hagamos una locura:"""


def maxProfit(prices: list) -> int:
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    return max_profit if max_profit > 0 else -1


def test(expected, received):
    return expected == received


def main():
    pricesBtc = [39, 18, 29, 25, 34, 32, 5]
    print(test(16, maxProfit(pricesBtc))) # -> 16 (compra a 18, vende a 34)

    pricesEth = [10, 20, 30, 40, 50, 60, 70]  
    print(test(60, maxProfit(pricesEth))) # -> 60 (compra a 10, vende a 70)

    pricesDoge = [18, 15, 12, 11, 9, 7]
    print(test(-1, maxProfit(pricesDoge))) # -> -1 (no hay ganancia posible)

    pricesAda = [3, 3, 3, 3, 3]
    print(test(-1, maxProfit(pricesAda))) # -> -1 (no hay ganancia posible)


if __name__ == "__main__":
    main()