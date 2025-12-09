"""Considera una lista/array de ovejas. Cada oveja tiene un nombre y un color.

Haz una función que devuelva una lista con todas las ovejas que sean de color rojo y que además su nombre contenga tanto las letras n Y a, sin importar el orden, las mayúsculas o espacios.
 
Recuerda. Debe contener las dos letras 'a' y 'n' en el nombre. No cuentes ovejas que sólo tenga una de las letras, debe tener ambas."""


def contarOvejas(ovejas):
    ovejas_filtradas = []
    for i, oveja in enumerate(ovejas):
        if oveja["color"] != "rojo":
            continue
        
        nombre_oveja = oveja["name"].lower()
        if "a" in nombre_oveja and "n" in nombre_oveja:
            ovejas_filtradas.append(ovejas[i])
    
    return ovejas_filtradas


def test(expected, received):
    return expected == received


def main():
    ovejas = [
        { "name": 'Noa', "color": 'azul' },
        { "name": 'Euge', "color": 'rojo' },
        { "name": 'Navidad', "color": 'rojo' },
        { "name": 'Ki Na Ma', "color": 'rojo'},
        { "name": 'AAAAAaaaaa', "color": 'rojo' },
        { "name": 'Nnnnnnnn', "color": 'rojo'}
    ]
    print(test([{ "name": 'Navidad', "color": 'rojo' }, { "name": 'Ki Na Ma', "color": 'rojo' }], contarOvejas(ovejas)))


if __name__ == "__main__":
    main()