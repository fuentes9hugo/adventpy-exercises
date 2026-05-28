"""¡Santa 🎅 está organizando una gran cena navideña 🫓 y quiere asegurarse de que todos los platos sean únicos y variados!

Te da una lista de platos navideños donde cada elemento consiste en una lista de strings que comienza con el nombre del plato, seguido de todos los ingredientes utilizados para su preparación.

Tienes que escribir una función que agrupe los platos por ingredientes siempre que haya al menos 2 platos que los contengan.

Así que devolvemos un array de arrays donde la primera posición es el nombre del ingrediente y el resto los nombres de los platos.

Tanto la lista de ingredientes como los platos deben estar ordenados alfabéticamente.

Ten en cuenta que:
- Todos los nombres de los platos son diferentes.
- Los nombres de los ingredientes para un plato dado son distintos entre sí.
- Si no hay ingredientes repetidos, devolvemos un array vacío."""


def organizeChristmasDinner(dishes: list[list[str]]) -> list[list[str]]:
    ingredients_map = {}

    for dish, *ingredients in dishes:
        for ingredient in ingredients:
            if ingredient not in ingredients_map: ingredients_map[ingredient] = [dish]
            else: ingredients_map[ingredient].append(dish)
    
    return sorted([ingredient] + sorted(associated_dishes) for ingredient, associated_dishes in ingredients_map.items() if len(associated_dishes) > 1)


def test(e ,r) -> bool:
    return e == r


def main():
    dishes = [
        ["christmas turkey", "turkey", "sauce", "herbs"],
        ["cake", "flour", "sugar", "egg"],
        ["hot chocolate", "chocolate", "milk", "sugar"],
        ["pizza", "sauce", "tomato", "cheese", "ham"],
    ]

    print(organizeChristmasDinner(dishes))
    print(test([
            ["sauce", "christmas turkey", "pizza"],
            ["sugar", "cake", "hot chocolate"]
        ], organizeChristmasDinner(dishes)))

    """
    "sauce" está en 2 platos: "christmas turkey" y "pizza".
    "sugar" está en 2 platos: "cake" y "hot chocolate".
    El resto de ingredientes solo aparecen en un plato, por lo que no los mostramos.

    Enseñamos primero "sauce" porque alfabéticamente está antes que "sugar".
    Y los platos de cada ingrediente también están ordenados alfabéticamente.

    [
    ["sauce", "christmas turkey", "pizza"],
    ["sugar", "cake", "hot chocolate"]
    ]
    """


if __name__ == "__main__":
    main()