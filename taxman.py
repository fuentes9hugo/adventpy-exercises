def taxman(envelopes_amount: int) -> list[int]:
    envelopes = {envelope: {j for j in range(1, envelope) if envelope % j == 0}
                 for envelope in range(2, envelopes_amount + 1)}

    def backtracking(result: list[int], forbiddens: set) -> list[int]:
        current_list = result

        for envelope, divisors in envelopes.items():
            if envelope in forbiddens or divisors.issubset(forbiddens): continue

            iterated_result = backtracking(current_list + [envelope], forbiddens | {envelope} | divisors)

            if sum(iterated_result) > sum(result): result = iterated_result
        
        return result


    return backtracking([], set())


def main():
    print(taxman(12))


if __name__ == "__main__":
    main()