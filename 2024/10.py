"""Los elfos programadores están creando un pequeño ensamblador mágico para controlar las máquinas del taller de Santa Claus.

Para ayudarles, vamos a implementar un intérprete sencillo que soporte las siguientes instrucciones mágicas:

MOV x y: Copia el valor x (puede ser un número o el contenido de un registro) en el registro y
INC x: Incrementa en 1 el contenido del registro x
DEC x: Decrementa en 1 el contenido del registro x
JMP x y: Si el valor del registro x es 0 entonces salta a la instrucción en el índice y y sigue ejecutándose el programa desde ahí.
Comportamiento esperado:
Si se intenta acceder, incrementar o decrementar a un registro que no ha sido inicializado, se tomará el valor 0 por defecto.
El salto con JMP es absoluto y lleva al índice exacto indicado por y.
Al finalizar, el programa debe devolver el contenido del registro A. Si A no tenía un valor definido, retorna undefined.

Nota: Los registros que no han sido inicializados previamente se inicializan a 0."""


def test(expected, received):
    return True if expected == received else False


def compile(instructions: list[str]):
    registers = {}

    def is_number(chain: str):
        if len(chain) > 1 or chain.isdigit():
            return True
        
        return False
    
    def move(copy, paste):
        if type(copy) == str:
            registers[paste] = registers[copy]

        else:
            registers[paste] = copy
    
    
    def jump(reg, jump_to, index):
        return jump_to - 1 if reg not in registers or registers[reg] == 0 else index
    
    instructions_map = {
        "INC": 1,
        "DEC": -1
    }

    index = 0
    while index < len(instructions):
        current_instruction = instructions[index].split(" ")

        for i, instruction in enumerate(current_instruction[1:], start=1):
            if is_number(instruction):
                current_instruction[i] = int(instruction)
            
            elif instruction not in registers:
                registers[instruction] = 0

        if current_instruction[0] in instructions_map:
            registers[current_instruction[1]] += instructions_map[current_instruction[0]]
        
        elif current_instruction[0] == "MOV":
            move(current_instruction[1], current_instruction[2])
        
        else:
            index = jump(current_instruction[1], current_instruction[2], index)
        
        index += 1
    
    return registers.get("A") # -> Lo mismo que: return registers["A"] if "A" in registers else None


def main():
    instructions = [
        'MOV -1 C', # copia -1 al registro 'C',
        'INC C', # incrementa el valor del registro 'C'
        'JMP C 1', # salta a la instrucción en el índice 1 si 'C' es 0
        'MOV C A', # copia el registro 'C' al registro 'a',
        'INC A' # incrementa el valor del registro 'a'
    ]

    print(test(2, compile(instructions))) # -> 2

    """
    Ejecución paso a paso:
    0: MOV -1 C -> El registro C recibe el valor -1
    1: INC C    -> El registro C pasa a ser 0
    2: JMP C 1  -> C es 0, salta a la instrucción en el índice 1
    1: INC C    -> El registro C pasa a ser 1
    2: JMP C 1  -> C es 1, ignoramos la instrucción
    3: MOV C A  -> Copiamos el registro C en A. Ahora A es 1
    4: INC A    -> El registro A pasa a ser 2
    """

    print(test(1, compile([
        "MOV 0 A",
        "INC A"
    ]))) # -> 1

    print(test(1, compile([
        "INC A",
        "INC A",
        "DEC A",
        "MOV A B",
    ]))) # -> 1

    print(test(5, compile([
        "MOV 5 B",
        "DEC B",
        "MOV B A",
        "INC A"
    ]))) # -> 5

    print(test(None, compile([
        "INC C",
        "DEC B",
        "MOV C Y",
        "INC Y",
    ]))) # -> None

    print(test(-2, compile([
        "MOV 2 X",
        "DEC X",
        "DEC X",
        "JMP X 1",
        "MOV X A"
    ]))) # -2

    print(test(-1, compile([
        "MOV 3 C",
        "DEC C",
        "DEC C",
        "DEC C",
        "JMP C 3",
        "MOV C A"
    ]))) # -1


if __name__ == "__main__":
    main()