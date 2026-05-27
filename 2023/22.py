"""En la fábrica de juguetes de Santa, los elfos están desarrollando un lenguaje de programación llamado Santa.js 👨‍💻👩‍💻 basado en símbolos para controlar sus máquinas de juguetes 🚂.

Han creado un sistema de instrucciones simple y necesitan tu ayuda para construir un compilador que interprete estos símbolos.

El compilador trabaja con un contador que inicialmente tiene un valor de 0. Las instrucciones modificarán el valor de este contador.

Instrucciones del lenguaje de los elfos en base a símbolos:
- +: Incrementa en 1 el valor del contador.
- *: Multiplica por 2 el valor del contador.
- -: Resta 1 al valor del contador.
- %: Marca un punto de retorno. No modifica el contador.
- <: Vuelve atrás una vez a la última instrucción con el símbolo % que haya visto. Si no hay un % previo, no hace nada.
- ¿: Inicia un bloque condicional que se ejecuta si el contador es mayor a 0.
- ?: Finaliza un bloque condicional.

Crea una función compile que reciba un string con las instrucciones del lenguaje y devuelve el resultado de ejecutarlas."""


def compile(code: str) -> int:
    basic_ops = {
        "+": lambda x: x + 1,
        "-": lambda x: x - 1,
        "*": lambda x: x * 2
    }

    counter = 0

    come_backs = {-1}
    conditionals = set()

    def come_back(pos: int) -> int:
        new_pos = code[:pos].rfind("%")

        if new_pos in come_backs: return pos

        come_backs.add(new_pos)

        return new_pos
    

    def conditional_block(pos: int) -> int:
        if counter > 0:
                    return pos
                
        stack = 0

        for i in range(pos, len(code)):
            if code[i] == "¿":
                stack += 1

            elif code[i] == "?":
                stack -= 1
                if stack == 0: return i

        return len(code)
    

    i = 0

    while i < len(code):
        char = code[i]

        if char in basic_ops: counter = basic_ops[char](counter)

        elif char == "<": i = come_back(i)

        elif char == "¿": i = conditional_block(i)

        i += 1
    
    return counter


def test(e, r) -> bool:
    return e == r


def main():
    print(compile('++*-')) # 3
    print(test(3, compile('++*-'))) # 3
    # (1 + 1) * 2 - 1 = 3

    print(compile('++%++<')) # 6
    print(test(6, compile('++%++<'))) # 6
    # 1 + 1 + 1 + 1 + 1 + 1 = 6

    print(compile('++<--')) # 0
    print(test(0, compile('++<--'))) # 0
    # 1 + 1 - 1 - 1 = 0

    print(compile('++¿+?')) # 3
    print(test(3, compile('++¿+?'))) # 3
    # 1 + 1 + 1 = 3

    print(compile('--¿+++?')) # -2
    print(test(-2, compile('--¿+++?'))) # -2
    # - 1 - 1 = -2

    print(compile('+¿++---¿-?+?')) # 1
    
    print(compile('¿++---¿-?+?++¿++¿++??')) # 6


if __name__ == "__main__":
    main()