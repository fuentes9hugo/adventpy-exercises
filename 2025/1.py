"""Santa ha recibido una lista de regalos, pero algunos están defectuosos. Un regalo es defectuoso si su nombre contiene el carácter #.

Ayuda a Santa escribiendo una función que reciba una lista de nombres de regalos y devuelva una nueva lista que solo contenga los regalos sin defectos."""


def filterGifts(gifts):
    return [gift for gift in gifts if "#" not in gift]


def main():
    gifts1 = ['car', 'doll#arm', 'ball', '#train']
    print(filterGifts(gifts1))
    # ['car', 'ball']

    gifts2 = ['#broken', '#rusty']
    print(filterGifts(gifts2))
    # []

    gifts3 = []
    print(filterGifts(gifts3))
    # []

    print(filterGifts(['game', 'poster', 'sticker#bad', 'console']))
    # ["game", "poster", "console"]

    print(filterGifts(['#bad', 'car', '#oops', 'ball']))
    # ["car", "ball"]


if __name__ =="__main__":
    main()