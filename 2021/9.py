"""En la fábrica de Papa Noél 🎅 se acerca el día especial... y todavía tenemos un montón de cosas por contar. 😅

Por suerte a Mark Zucktheelf 🧝 se le ha ocurrido crear una función que permita agrupar un array, que puede ser de valores u objetos, a través de una función o de una propiedad.

Nos trae un montón de ejemplos:

Como ves, la función groupBy recibe una colección (array) y una función o una propiedad, y devuelve un objeto con claves que son los valores de la función ejecutada pasando como argumento cada elemento o de la propiedad por cada elemento. Luego los valores son un array de los valores que tengan la misma llave.

La dificultad del reto está más en comprender la función que en la implementación. ¡Suerte!"""


import math
from datetime import datetime


def group_by(collection, it):
    result = {}
    
    for item in collection:
        # 1. Determinamos la clave
        # Si 'it' es una función, la ejecutamos pasando el item / Si 'it' no es función, asumimos que es una clave de diccionario (propiedad)
        key = it(item) if callable(it) else item[it]
        
        # 2. Inicializamos la lista si la clave no existe
        if key not in result:
            result[key] = []
        
        # 3. Agregamos el item a su grupo
        result[key].append(item)
        
    return dict(sorted(result.items()))


def main():
    # --- Ejemplo 1: Números y Math.floor ---
    # En Python pasamos la función math.floor
    print(group_by([6.1, 4.2, 6.3], math.floor))
    # Salida: {6: [6.1, 6.3], 4: [4.2]}


    # --- Ejemplo 2: Strings y longitud ---
    # Usamos la función 'len' en lugar de la string 'length'
    print(group_by(['one', 'two', 'three'], len))
    # Salida: {3: ['one', 'two'], 5: ['three']}


    # --- Ejemplo 3: Objetos (Diccionarios) y propiedad 'age' ---
    users = [{'age': 23}, {'age': 24}]
    print(group_by(users, 'age'))
    # Salida: {23: [{'age': 23}], 24: [{'age': 24}]}


    # --- Ejemplo 4: Timestamps y Año ---
    timestamps = [1397639141184, 1363223700000]
    # Lambda para obtener el año (dividimos por 1000 porque Python usa segundos, JS milisegundos)
    get_year = lambda ts: datetime.fromtimestamp(ts / 1000).year

    print(group_by(timestamps, get_year))
    # Salida: {2014: [1397639141184], 2013: [1363223700000]}


    # --- Ejemplo 5: Libros y Rating ---
    books = [
    { 'title': 'JavaScript: The Good Parts', 'rating': 8 },
    { 'title': 'Aprendiendo Git', 'rating': 10 },
    { 'title': 'Clean Code', 'rating': 9 },
    ]
    print(group_by(books, 'rating'))
    # Salida agrupa correctamente por el rating 8, 9 y 10.


if __name__ == "__main__":
    main()