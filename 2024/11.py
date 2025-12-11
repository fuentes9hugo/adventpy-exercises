"""El Grinch ha hackeado 🏴‍☠️ los sistemas del taller de Santa Claus y ha codificado los nombres de todos los archivos importantes. Ahora los elfos no pueden encontrar los archivos originales y necesitan tu ayuda para descifrar los nombres.

Cada archivo sigue este formato:

Comienza con un número (puede contener cualquier cantidad de dígitos).
Luego tiene un guion bajo _.
Continúa con un nombre de archivo y su extensión.
Finaliza con una extensión extra al final (que no necesitamos).
Ten en cuenta que el nombre de los archivos pueden contener letras (a-z, A-Z), números (0-9), otros guiones bajos (_) y guiones (-).

Tu tarea es implementar una función que reciba un string con el nombre de un archivo codificado y devuelva solo la parte importante: el nombre del archivo y su extensión."""


def decodeFilename(filename: str) -> str:
    return filename[filename.find("_") + 1 : filename.rfind(".")]


def test(expected, received):
    return expected == received


def main():
    print(test("sleighDesign.png", decodeFilename('2023122512345678_sleighDesign.png.grinchwa')))
    # ➞ "sleighDesign.png"

    print(test("chimney_dimensions.pdf", decodeFilename('42_chimney_dimensions.pdf.hack2023')))
    # ➞ "chimney_dimensions.pdf"

    print(test("elf-roster.csv", decodeFilename('987654321_elf-roster.csv.tempfile')))
    # ➞ "elf-roster.csv"

    print(test("magic_wand-blueprint.jpg", decodeFilename("2024120912345678_magic_wand-blueprint.jpg.grinchbackup")))
    # ➞ "magic_wand-blueprint.jpg"

    print(test("trainSchedule.txt", decodeFilename("51231_trainSchedule.txt.extra")))
    # ➞ "trainSchedule.txt"


if __name__ == "__main__":
    main()