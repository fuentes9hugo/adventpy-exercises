def taxman(envelopes_amount: int) -> list[int]:
    envelopes = {envelope: {j for j in range(1, envelope) if envelope % j == 0}
                 for envelope in range(2, envelopes_amount + 1)}
    
    stack = [([], set(), 2)]

    solution = []

    while stack:
        current_list, forbiddens, envelope = stack.pop()

        if envelope not in envelopes: continue

        divisors = envelopes[envelope]

        stack.append((current_list, forbiddens, envelope + 1))

        if envelope in forbiddens or divisors.issubset(forbiddens): continue

        new_list = current_list + [envelope]

        stack.append((new_list, forbiddens | {envelope} | divisors, 2))

        if sum(new_list) > sum(solution): solution = new_list

    return solution


def main():
    print(taxman(12))


if __name__ == "__main__":
    main()