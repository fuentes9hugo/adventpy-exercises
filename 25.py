def execute(code: str) -> int:
    code_map = {
        "+": 1,
        "-": -1,
        ">": 0
    }

    value = 0

    return value


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