"""¡Ya hemos repartido todos los regalos! De vuelta al taller, ya comienzan los preparativos para el año que viene.

Un elfo genio está creando un lenguaje de programación mágico 🪄, que ayudará a simplificar la entrega de regalos a los niños en 2025.

Los programas siempre empiezan con el valor 0 y el lenguaje es una cadena de texto donde cada caracter representa una instrucción:

> Se mueve a la siguiente instrucción
+ Incrementa en 1 el valor actual
- Decrementa en 1 el valor actual
[ y ]: Bucle. Si el valor actual es 0, salta a la instrucción después de ]. Si no es 0, vuelve a la instrucción después de [
{y }: Condicional. Si el valor actual es 0, salta a la instrucción después de }. Si no es 0, sigue a la instrucción después de {
Tienes que devolver el valor del programa tras ejecutar todas las instrucciones.

Nota: Un condicional puede tener un bucle dentro y también un bucle puede tener un condicional. Pero nunca se anidan dos bucles o dos condicionales."""


def execute(code: str) -> int:
    def code_loop(chain, current_value):
        value = 0
        value_aux = 0
        while current_value != 0:
            value_aux += update_value(chain)
            value += value_aux
            current_value += value_aux
            value_aux = 0

        return value


    def code_conditional(chain, current_value):
        value = 0
        if current_value != 0:
            value += update_value(chain)

        return value


    def update_value(chain):
        current_value = 0
        skip_until = ""
        for i, char in enumerate(chain):
            if char == skip_until:
                skip_until = ""

            if char in code_map and not skip_until:
                current_value += code_map[char]
            
            elif char in key_chars:
                current_value += key_chars[char][1](chain[i + 1:chain.find(key_chars[char][0], i + 1)], current_value)
                skip_until = key_chars[char][0]
        
        return current_value

    code_map = {
        "+": 1,
        "-": -1,
        ">": 0
    }

    key_chars = {
        "[": ("]", code_loop),
        "{": ("}", code_conditional)
    }

    return update_value(code)


def main():
    print(execute('+++')) # 3
    print(execute('+--')) # -1
    print(execute('>+++[-]')) # 0
    print(execute('>>>+{++}')) # 3
    print(execute('+{[-]+}+')) # 2
    print(execute('{+}{+}{+}')) # 0
    print(execute('------[+]++')) # 2
    print(execute('-[++{-}]+{++++}')) # 5


if __name__ == "__main__":
    main()