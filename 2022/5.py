"""Para no cansar a los renos, Papá Noel quiere dejar el máximo número de regalos haciendo el menor número posible de viajes.

Tiene un array de ciudades donde cada elemento es el número de regalos que puede dejar allí. [12, 3, 11, 5, 7]. Por otro lado, el límite de regalos que caben en su saco. Y, finalmente, el número de ciudades máximo que sus renos pueden visitar.

Como no quiere dejar una ciudad a medias, si no puede dejar todos los regalos que son de esa ciudad, no deja ninguno allí.

Crea un programa que le diga la suma más alta de regalos que podría repartir teniendo en cuenta el máximo de regalos que puede transportar y el número máximo de ciudades que puede visitar.

Si no se puede realizar ningún viaje que satisface los requerimientos, el resultado debe ser 0.

A tener en cuenta:
- maxGifts >= 1
- giftsCities.length >= 1
- maxCities >= 1
- El número de maxCities puede ser mayor a giftsCities.length"""


def get_max_gifts(gifts_cities: list[int], max_gifts: int, max_cities: int) -> int:
    def backtrack(gifts_cities, current_gifts, current_cities, index):
        current_cities += 1
        posible_results = []
        
        for i in range(index, len(gifts_cities)):
            gifts = gifts_cities[i]
            actual_gifts = current_gifts + gifts

            if actual_gifts == max_gifts:
                return actual_gifts

            elif actual_gifts > max_gifts:
                continue

            if current_cities < max_cities:
                more_gifts = backtrack(gifts_cities, actual_gifts, current_cities, i + 1)

                if more_gifts > 0: actual_gifts = more_gifts
            
            posible_results.append(actual_gifts)
        
        return max(posible_results) if posible_results else 0
    
    
    return backtrack(gifts_cities, 0, 0, 0)


def test(e, r):
    return e == r


def main():
    gifts_cities = [12, 3, 11, 5, 7]
    max_gifts = 20
    max_cities = 3

    # la suma más alta de regalos a repartir
    # visitando un máximo de 3 ciudades
    # es de 20: [12, 3, 5]

    # la suma más alta sería [12, 7, 11]
    # pero excede el límite de 20 regalos y tendría
    # que dejar alguna ciudad a medias.

    print(test(20, get_max_gifts(gifts_cities, max_gifts, max_cities))) # 20

    print(test(20, get_max_gifts([12, 3, 11, 5, 7], 20, 3))) # 20
    print(test(0, get_max_gifts([50], 15, 1))) # 0
    print(test(50, get_max_gifts([50], 100, 1))) # 50
    print(test(70, get_max_gifts([50, 70], 100, 1))) # 70
    print(test(100, get_max_gifts([50, 70, 30], 100, 2))) # 100
    print(test(100, get_max_gifts([50, 70, 30], 100, 3))) # 100
    print(test(100, get_max_gifts([50, 70, 30], 100, 4))) # 100
    print(test(12, get_max_gifts([12], 20, 2))) # 12


if __name__ == "__main__":
    main()