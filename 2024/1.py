def prepareGifts(gifts: list) -> list:
    gifts = sorted(set(gifts))

    return gifts

def main():
    gifts1 = [3, 1, 2, 3, 4, 2, 5]
    preparedGifts1 = prepareGifts(gifts1)
    print(preparedGifts1) # [1, 2, 3, 4, 5]

    gifts2 = [6, 5, 5, 5, 5]
    preparedGifts2 = prepareGifts(gifts2)
    print(preparedGifts2) # [5, 6]

    gifts3 = []
    preparedGifts3 = prepareGifts(gifts3)
    print(preparedGifts3) # []
    # No hay regalos, la lista queda vacía


if __name__ == "__main__":
    main()