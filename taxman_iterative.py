def taxman(envelopes_amount: int) -> list[int]:
    envelopes = {envelope: {j for j in range(1, envelope) if envelope % j == 0}
                 for envelope in range(2, envelopes_amount + 1)}
    
    stack = [([], set())]

    solution = []

    while stack:
        current_list, forbiddens = stack.pop()

        for envelope, dividers in envelopes.items():
            if envelope in forbiddens or dividers.issubset(forbiddens): continue

            

    return solution


def main():
    print(taxman(12))


if __name__ == "__main__":
    main()