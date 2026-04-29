"""Están encendiendo las luces de Navidad 🎄 en la ciudad y, como cada año, ¡hay que arreglarlas!

Las luces son de dos colores: 🔴 y 🟢 . Para que el efecto sea el adecuado, siempre deben estar alternadas. Es decir, si la primera luz es roja, la segunda debe ser verde, la tercera roja, la cuarta verde, etc.

Nos han pedido que escribamos una función adjustLights que, dado un array de strings con el color de cada luz (representados con los emojis 🔴 para el rojo y 🟢 para el verde), devuelva el número mínimo de luces que hay que cambiar para que estén los colores alternos."""


def adjustLights(lights: list[str]) -> int:
    lights_len = len(lights)    
    chars = ('🟢', '🔴')

    correct_lights = [[chars[(j-i) % 2] for j in range(lights_len)] for i in range(2)]

    differences = [0, 0]

    for i, i_lights in enumerate(correct_lights):
        for i_light, light in zip (i_lights, lights):
            if i_light != light: differences[i] += 1

    return min(differences)


def test(e, r) -> bool:
    return e == r


def main():
    print(test(1, adjustLights(['🟢', '🔴', '🟢', '🟢', '🟢'])))
    # -> 1 (cambias la cuarta luz a 🔴)

    print(test(1, adjustLights(['🔴', '🔴', '🟢', '🔴', '🟢'])))
    # -> 1 (cambia la primera luz a verde)

    print(test(2, adjustLights(['🔴', '🔴', '🟢', '🟢', '🔴'])))
    # -> 2 (cambias la segunda luz a 🟢 y la tercera a 🔴)

    print(test(0, adjustLights(['🟢', '🔴', '🟢', '🔴', '🟢'])))
    # -> 0 (ya están alternadas)

    print(test(1, adjustLights(['🔴', '🔴', '🔴'])))
    # -> 1 (cambias la segunda luz a 🟢)


if __name__ == "__main__":
    main()