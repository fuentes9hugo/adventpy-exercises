"""¡Hemos perdido a un reno y falta poco más de una semana para Navidad! 😱

Lo peor es que son tantos que no sabemos cuál es el que nos falta... ¡Qué lío! A ver, Elfon Musk ha hecho inventario y nos pasa un array con los ids de cada reno.

👍 Lo bueno: los ids son números que pueden ir del 0 al 100, no están repetidos y sólo se ha perdido un reno.

👎 Lo malo: la lista está desordenada y podría faltar el último...

Necesitamos una función que al pasarle la lista de ids de renos nos diga inmediatamente cuál es el que falta.

Parece fácil con una complejidad de O(n)... ¿crees que podrías hacerlo mejor?"""


def missingReindeer(ids: list[int]) -> int:
    """
    n = len(ids)
    
    # Suma de Gauss
    expected_sum = n * (n + 1) // 2
    
    actual_sum = sum(ids)
    
    return expected_sum - actual_sum
    """
    
    max_id = max(ids)
    sorted_ids = set(ids)
    for id in range(max_id):
        if id not in sorted_ids:
            return id
    
    return max_id + 1


def test(expected, received):
    return expected == received


def main():
    print(test(1, missingReindeer([0, 2, 3]))) # -> 1
    print(test(4, missingReindeer([5, 6, 1, 2, 3, 7, 0]))) # -> 4
    print(test(2, missingReindeer([0, 1]))) # -> 2 (¡es el último el que falta!)
    print(test(2, missingReindeer([3, 0, 1]))) # -> 2
    print(test(8, missingReindeer([9, 2, 3, 5, 6, 4, 7, 0, 1]))) # -> 8
    print(test(1, missingReindeer([0]))) # -> 1 (¡es el último el que falta!)


if __name__ == "__main__":
    main()