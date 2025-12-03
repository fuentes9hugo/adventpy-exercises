"""¡Es hora de poner el árbol de Navidad en casa! 🎄 Pero este año queremos que sea especial. Vamos a crear una función que recibe la altura del árbol (un entero positivo entre 1 y 100) y un carácter especial para decorarlo.

La función debe devolver un string que represente el árbol de Navidad, construido de la siguiente manera:

El árbol está compuesto de triángulos de caracteres especiales.
Los espacios en blanco a los lados del árbol se representan con guiones bajos _.
Todos los árboles tienen un tronco de dos líneas, representado por el carácter #.
El árbol siempre debe tener la misma longitud por cada lado.
Debes asegurarte de que el árbol tenga la forma correcta usando saltos de línea \n para cada línea."""


def createXmasTree(height, ornament):
    tree = ""

    width = (2 * height) - 1
    width_space = width // 2
    ornament_multipier = 1

    for i in range(height):
        tree += "_" * (width_space - i) + f"{ornament}" * ornament_multipier + "_" * (width_space - i) + "\n"
        ornament_multipier += 2

    tree += "_" * width_space + "#" + "_" * width_space + "\n"
    tree += "_" * width_space + "#" + "_" * width_space

    return tree

def main():
    print(createXmasTree(5, '*'), end="\n\n")
    """____*____
       ___***___
       __*****__
       _*******_
       *********
       ____#____
       ____#____"""

    print(createXmasTree(3, '+'), end="\n\n")
    """__+__
       _+++_
       +++++
       __#__
       __#__"""

    print(createXmasTree(6, '@'), end="\n\n")
    """_____@_____
       ____@@@____
       ___@@@@@___
       __@@@@@@@__
       _@@@@@@@@@_
       @@@@@@@@@@@
       _____#_____
       _____#_____"""
    
    print(createXmasTree(1, '*'), end="\n\n")
    """*
       #
       # """
    
    print(createXmasTree(4, '#'), end="\n\n")
    """___#___
       __###__
       _#####_
       #######
       ___#___
       ___#___"""


if __name__ == "__main__":
    main()