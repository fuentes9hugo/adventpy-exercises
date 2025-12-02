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