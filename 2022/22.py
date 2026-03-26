"""Verifica que todas las secuencias independientes de sistemas de iluminación navideña estén en orden estrictamente creciente. Tenemos dos arrays: systemNames y stepNumbers.

systemNames contiene los nombres de los sistemas de iluminación navideña, y stepNumbers contiene los números de paso de cada sistema.

Debemos verificar que los stepNumbers de cada sistema estén en orden estrictamente creciente. Si esto es cierto, devuelve true; de lo contrario, devuelve false.

Ten en cuenta que:
- La posición del nombre del sistema en systemNames y el número de paso en stepNumbers corresponden al mismo sistema.
- Los pasos en stepNumbers pueden repetirse para diferentes sistemas."""


def checkStepNumbers(systemNames: list[str], stepNumbers: list[int]) -> bool:
    step_map = {}
    for name, num in zip(systemNames, stepNumbers):
        if name in step_map:
            if step_map[name] >= num: return False
        
        step_map[name] = num
    
    return True
    

def test(e, r):
    return e == r


def main():
    systemNames = ["tree_1", "tree_2", "house", "tree_1", "tree_2", "house"]
    stepNumbers = [1, 33, 10, 2, 44, 20]

    print(test(True, checkStepNumbers(systemNames, stepNumbers))) # => true

    # tree_1 tiene los pasos: [1, 2]
    # tree_2 tiene los pasos: [33, 44]
    # house tiene los pasos: [10, 20]

    # true: Los pasos de cada sistema están en orden estrictamente creciente

    print(test(False, checkStepNumbers(["tree_1", "tree_1", "house"], [2, 1, 10]))) # => false

    # tree_1 tiene los pasos: [2, 1]
    # house tiene los pasos: [10]

    # false: tree_1 tiene los pasos de forma decreciente


if __name__ == "__main__":
    main()