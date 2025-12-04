"""¡Es hora de seleccionar a los renos más rápidos para los viajes de Santa! 🦌🎄
Santa Claus ha organizado unas emocionantes carreras de renos para decidir cuáles están en mejor forma.

Tu tarea es mostrar el progreso de cada reno en una pista de nieve en formato isométrico.

La información que recibes:

indices: Un array de enteros que representan el progreso de cada reno en la pista:
0: El carril está vacío.
Número positivo: La posición actual del reno desde el inicio de la pista.
Número negativo: La posición actual del reno desde el final de la pista.
length: La longitud de cada carril.
Devuelve un string que represente la pista de la carrera:

Cada carril tiene exactamente length posiciones llenas de nieve (~).
Cada reno se representa con la letra r.
Los carriles están numerados al final con /1, /2, etc.
La vista es isométrica, por lo que los carriles inferiores están desplazados hacia la derecha."""


def test(expected, received):
    if expected == received:
        return True

    return False


def drawRace(indices, length):
    race = ""
    for i, reindeer in enumerate(indices, start=1):
        field = "~" * length
        
        pos = reindeer + length if reindeer < 0 else reindeer
        
        if pos != 0:
            field = field[:pos] + "r" + field[pos + 1:]
        
        race += " " * (len(indices) - i) + field + f" /{i}"
        race += "\n" if i != len(indices) else ""
    
    return race

def main():
    print(test("  ~~~~~~~~~~ /1\n ~~~~~r~~~~ /2\n~~~~~~~r~~ /3", drawRace([0, 5, -3], 10)))
    """
      ~~~~~~~~~~ /1
     ~~~~~r~~~~ /2
    ~~~~~~~r~~ /3
    """

    print(test("   ~~r~~~~~ /1\n  ~~~~~~~r /2\n ~~~~~~~~ /3\n~~~~~r~~ /4", drawRace([2, -1, 0, 5], 8)))
    """
       ~~r~~~~~ /1
      ~~~~~~~r /2
     ~~~~~~~~ /3
    ~~~~~r~~ /4
    """

    print(test("  ~~~r~~~~~~~~ /1\n ~~~~~~~r~~~~ /2\n~~~~~~~~~~r~ /3", drawRace([3, 7, -2], 12)))
    """
      ~~~r~~~~~~~~ /1
     ~~~~~~~r~~~~ /2
    ~~~~~~~~~~r~ /3
    """


if __name__ =="__main__":
    main()