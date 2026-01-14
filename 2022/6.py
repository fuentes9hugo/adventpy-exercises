"""Una pareja de entusiastas de la navidad ha creado una empresa de adornos navideños. El primer adorno que quieren fabricar es un cubo que se pone en los árboles.

El problema es que tienen que programar la máquina y no saben cómo hacerlo. Nos han pedido ayuda para lograrlo.

Para crear los cubos se le pasa un número con el tamaño deseado al programa y este devuelve un string con el diseño de ese tamaño. Por ejemplo, si le pasamos un 3, el programa debe devolver un cubo de 3x3x3.

A tener en cuenta:

- Fíjate bien en los espacios en blanco que hay en el cubo.
- El cubo tiene que ser simétrico.
- Asegúrate de usar los símbolos correctos.
- Cada nueva línea del cubo debe terminar con un salto de línea (\n) excepto la última."""


def createCube(size: int) -> str:
    cube_top = []
    cube_bottom = []
    reversed_i = size
    for i in range(size):
        cube_top.append(" " * reversed_i + "/\\".strip() * (i + 1) + "_\\" * size)
        cube_bottom.append(" " * (i + 1) + "\\/" * reversed_i + "_/" * size)
        reversed_i -= 1
    
    cube = "\n".join(cube_top) + "\n" + "\n".join(cube_bottom)
    return cube
    

def main():
    cube = createCube(3)
    #   /\_\_\_\
    #  /\/\_\_\_\
    # /\/\/\_\_\_\
    # \/\/\/_/_/_/
    #  \/\/_/_/_/
    #   \/_/_/_/
    
    print(cube)
    # Como ves el cubo tiene tres caras visualmente. Los símbolos que se usan para construir las caras del cubo son: /, \, _ y (espacio en blanco).

    # Otros ejemplos de cubos:

    cubeOfOne = createCube(1)
    # /\_\
    # \/_/
    
    print(cubeOfOne)
    cubeOfTwo = createCube(2)
    #  /\_\_\
    # /\/\_\_\
    # \/\/_/_/
    #  \/_/_/
    
    print(cubeOfTwo)


if __name__ == "__main__":
    main()