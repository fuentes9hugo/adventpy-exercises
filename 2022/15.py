"""Una pareja está poniendo el árbol de navidad. El chico es un motivado de los adornos navideños y quiere que quede perfectamente equilibrado. Tiene tres tipos de decoraciones:
- Bolas de colores : B
- Regalos pequeños : R
- Piñas de pino : P

El árbol de navidad es un triángulo que hay que generar. Ya tienen la base montada, que sería la primera fila, y a partir de ahí tienen que ir colocando las decoraciones hacía arriba siguiendo una fórmula.

Arriba coloca  :     P     R     B     P
Si abajo tiene :    P P   B P   R P   B R

Las combinaciones también son al revés. Por ejemplo, si abajo es B P, arriba es R. Pero también será R si abajo es P B. También si abajo tienes dos veces la misma letra, arriba será la misma letra. Por ejemplo, si abajo es B B, arriba es B.

Con estas reglas, podríamos ver el árbol que generaríamos con la base B P R P:

   R
  P B
 R B B
B P R P

Escribe un programa que reciba el string B P R P y devuelva un array con la representación del árbol.

Ten en cuenta que:
- El programa recibe siempre la cadena de texto que representa la base del árbol.
- Hay que generar el árbol completo, es decir, la base y las filas que se generan a partir de ella, hasta arriba.
- Hay que seguir la fórmula para saber qué decoración colocar en cada posición."""


from collections import deque


def decorateTree(base: str) -> list[str]:
    ornaments = {"B", "P", "R"}
    base_map = {orn_1 + orn_2: orn_1 if orn_1 == orn_2 else (ornaments - {orn_1, orn_2}).pop() for orn_1 in ornaments for orn_2 in ornaments}

    tree = [base.split(" ")]

    while len(tree[-1]) > 1:
        level = []
        for i in range(len(tree[-1]) - 1):
            level.append(base_map[tree[-1][i] + tree[-1][i+1]])
        
        tree.append(level)
    
    return [" ".join(row) for row in reversed(tree)]


def test(e, r):
    return e == r


def main():
    print(test(["R", "P B", "R B B", "B P R P"], decorateTree('B P R P')))
    # [
    # 'R',
    # 'P B',
    # 'R B B',
    # 'B P R P'
    # ]

    print(test(['B', 'B B'], decorateTree('B B'))) # ['B', 'B B']


if __name__ == "__main__":
    main()