"""Dos elfos están jugando una batalla por turnos. Cada uno tiene un mazo de movimientos que se representan como un string donde cada carácter es una acción.

A Ataque normal: causa 1 punto de daño si no es bloqueado
B Bloqueo: bloquea un ataque normal (A)
F Ataque fuerte: causa 2 puntos de daño, no puede ser bloqueado
Ambos elfos comienzan con 3 puntos de vida. El primer elfo que llegue a 0 puntos de vida o menos pierde y la batalla termina inmediatamente (no se siguen procesando más movimientos).

Reglas por ronda

Si ambos usan ataque (A o F), ambos reciben daño según el tipo.
B bloquea A, pero no bloquea F.
Todo se resuelve simultáneamente.
Tu tarea

Devuelve el resultado de la batalla como un número:

1 → si el Elfo 1 gana
2 → si el Elfo 2 gana
0 → si empatan (ambos llegan a 0 a la vez o terminan con la misma vida)"""


def elfBattle(elf1: str, elf2: str) -> int:
    elf1_health, elf2_health = 3, 3
    def attack(attacker, defender):
        if attacker == "A" and defender != "B":
            return 1
        
        elif attacker == "F":
            return 2
        
        return 0

    for elf1_attk, elf2_attk in zip(elf1, elf2):
        elf2_health -= attack(elf1_attk, elf2_attk)
        elf1_health -= attack(elf2_attk, elf1_attk)

        if elf1_health <= 0 or elf2_health <= 0:
            break
    
    if elf1_health == elf2_health or elf1_health <= 0 and elf2_health <= 0:
        return 0
    
    elif elf1_health > elf2_health:
        return 1
    
    return 2


def test(expected, received):
    return expected == received


def main():
    print(test(0, elfBattle('A', 'B')))
    # Ronda 1: A vs B -> Elfo 2 bloquea
    # Resultado: Elfo 1 = 3 de vida
    #            Elfo 2 = 3 de vida
    # → 0

    print(test(1, elfBattle('F', 'B')))
    # Ronda 1: F vs B -> Elfo 2 recibe 2 de daño (F no se bloquea)
    # Resultado: Elfo 1 = 3 de vida
    #            Elfo 2 = 1 de vida
    # → 1

    print(test(0, elfBattle('AAB', 'BBA')))
    # R1: A vs B → Elfo 2 bloquea
    # R2: A vs B → Elfo 2 bloquea
    # R3: B vs A → Elfo 1 bloquea
    # Resultado: Elfo 1 = 3, Elfo 2 = 3
    # → 0

    print(test(1, elfBattle('AFA', 'BBA')))
    # R1: A vs B → Elfo 2 bloquea
    # R2: F vs B → Elfo 2 recibe 2 de daño (F no se bloquea)
    # R3: A vs A → ambos -1
    # Resultado: Elfo 1 = 2, Elfo 2 = 0
    # → 1

    print(test(1, elfBattle('AFAB', 'BBAF')))
    # R1: A vs B → Elfo 2 bloquea
    # R2: F vs B → Elfo 2 recibe 2 de daño (F no se bloquea)
    # R3: A vs A → ambos -1 → Elfo 2 llega a 0 ¡Batalla termina!
    # R4: no se juega, ya que Elfo 2 no tiene vida
    # → 1

    print(test(2, elfBattle('AA', 'FF')))
    # R1: A vs F → Elfo 1 -2, Elfo 2 -1
    # R2: A vs F → Elfo 1 -2, Elfo 2 -1 → Elfo 1 llega a -1
    # → 2


if __name__ == "__main__":
    main()