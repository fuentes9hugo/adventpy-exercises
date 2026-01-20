from models import Board, O, I, T, S, Z, L, J


def main():
    o, i, t, s, z, l, j = O(), I(), T(), S(), Z(), L(), J()
    print(l)
    l.rotate("right")
    print()
    print(l)
    print()
    l.rotate("right")
    print(l)
    print()
    l.rotate("right")
    print(l)
    l.rotate("right")
    print()
    print(l)
    print()
    l.rotate("left")
    print(l)
    print()
    l.rotate("left")
    print(l)
    l.rotate("left")
    print()
    print(l)

if __name__ == "__main__":
    main()