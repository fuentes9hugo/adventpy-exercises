"""Ya hemos empaquetado cientos de regalos 🎁… pero a un elfo se le ha olvidado revisar si el regalo, representado por un asterisco *, está dentro de la caja.

La caja tiene un regalo (*) y cuenta como dentro de la caja si:

Está rodeada por # en los bordes de la caja.
El * no está en los bordes de la caja.
Ten en cuenta entonces que el * puede estar dentro, fuera o incluso no estar. Y debemos devolver true si el * está dentro de la caja y false en caso contrario."""


def inBox(box):
    for row in box[1:-1]:
        if row[0] == "#" and row[-1] == "#" and "*" in row:
            return True
         
    return False


def main():
    print(inBox([
        "###",
        "#*#",
        "###"
    ])) # ➞ true

    print(inBox([
        "####",
        "#* #",
        "#  #",
        "####"
    ])) # ➞ true

    print(inBox([
        "#####",
        "#   #",
        "#  #*",
        "#####"
    ])) # ➞ false

    print(inBox([
        "#####",
        "#   #",
        "#   #",
        "#   #",
        "#####"
    ])) # ➞ false


if __name__ == "__main__":
    main()