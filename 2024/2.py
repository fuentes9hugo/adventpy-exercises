"""Santa Claus 🎅 quiere enmarcar los nombres de los niños buenos para decorar su taller 🖼️, pero el marco debe cumplir unas reglas específicas. Tu tarea es ayudar a los elfos a generar este marco mágico.

Reglas:

Dado un array de nombres, debes crear un marco rectangular que los contenga a todos.
Cada nombre debe estar en una línea, alineado a la izquierda.
El marco está construido con * y tiene un borde de una línea de ancho.
La anchura del marco se adapta automáticamente al nombre más largo más un margen de 1 espacio a cada lado."""


def createFrame(names):
    longest_name_num = len(max(names, key=len))
    frame = "*" * (longest_name_num + 4) + "\n"
    for i, name in enumerate(names):        
        frame += f"* {name}" + " " * (longest_name_num - len(name)) + " *\n"

    frame += "*" * (longest_name_num + 4)

    return frame

def main():
    print(createFrame(['midu', 'madeval', 'educalvolpz']))
    """***************
       * midu        *
       * madeval     *
       * educalvolpz *
       ***************"""

    print(createFrame(['midu']))
    """********
       * midu *
       ********"""

    print(createFrame(['a', 'bb', 'ccc']))
    """*******
       * a   *
       * bb  *
       * ccc *
       *******"""

    print(createFrame(['a', 'bb', 'ccc', 'dddd']))
    """********
       * a    *
       * bb   *
       * ccc  *
       * dddd *
       ********"""


if __name__ == "__main__":
    main()