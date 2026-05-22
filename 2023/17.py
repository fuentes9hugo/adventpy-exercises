"""En Rovaniemi, Finlandia 🇫🇮, los trineos 🛷 se alquilan por intervalos de tiempo. Cada intervalo se representa como un array de dos elementos, donde el primer elemento es el inicio del alquiler y el segundo es el final.

Por ejemplo, el array [2, 7] representa un alquiler que comienza en la hora 2 y termina en la hora 7. El problema es que a veces los intervalos se superponen entre sí, haciendo que sea un lío entender de qué hora a qué hora se alquiló el trineo.

Nos piden que, para simplificar la tarea de calcular el tiempo total de alquiler, escribamos una función que fusione todos los intervalos superpuestos y devolver un array de intervalos ordenados.

Puedes asumir que el primer elemento de cada intervalo siempre es menor o igual que el segundo elemento. Pero los intervalos no están necesariamente ordenados.

Los números de horas pueden llegar hasta la cifra 9999."""


def optimizeIntervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals: return []

    intervals = sorted(intervals)

    optimized_intervals = []

    current_lowest = intervals[0][0]
    current_highest = intervals[0][1]

    for i, interval in enumerate(intervals[1:]):
        low, high = interval

        if low > current_highest:
            optimized_intervals.append([current_lowest, current_highest])
            current_lowest = low
            current_highest = high

        if high > current_highest:
            current_highest = high

    optimized_intervals.append([current_lowest, current_highest])
    
    return optimized_intervals


def test(e, r) -> bool:
    return e == r


def main():
    print(test([[2, 8]], optimizeIntervals([
        [5, 8],
        [2, 7],
        [3, 4]
    ]))) # [[2, 8]]

    print(optimizeIntervals([
        [5, 8],
        [2, 7],
        [3, 4]
    ]))

    print(test([[1, 6], [8, 10]], optimizeIntervals([
        [1, 3],
        [8, 10],
        [2, 6]
    ]))) # [[1, 6], [8, 10]]

    print(optimizeIntervals([
        [1, 3],
        [8, 10],
        [2, 6]
    ]))

    print(test([[1, 2], [3, 4], [5, 6]], optimizeIntervals([
        [3, 4],
        [1, 2],
        [5, 6]
    ]))) # [[1, 2], [3, 4], [5, 6]]

    print(optimizeIntervals([
        [3, 4],
        [1, 2],
        [5, 6]
    ]))


if __name__ == "__main__":
    main()