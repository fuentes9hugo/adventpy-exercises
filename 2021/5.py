"""Con la emoción, ya estamos empezando a contar los días del calendario hasta el 25 de diciembre 📆.

Para ayudar a esto, vamos a crear una función que pasándole una instancia de datetime nos diga el número de días que faltan.

El resultado tiene que ser un número entero y, como ves, aunque falte un segundo hasta el siguiente día, se entiende que todavía falta un día.

¡Pero ojo! También hay que indicar si la fecha es del mismo día (devolveríamos 0) o si es una fecha futura (devolveríamos el número de días en negativo -).

Por cierto, la fecha de referencia para saber si es 25 de diciembre es Dec 25, 2021."""


from datetime import datetime


def daysToXmas(date: datetime) -> int:
    xmas = datetime(2021, 12, 25)
    remaining_time = xmas - date
    days = remaining_time.days

    return days + 1 if remaining_time.seconds > 0 else days


def test(expected, received):
    return expected == received


def main():
    date1 = datetime(2021, 12, 1)
    print(test(24, daysToXmas(date1))) # 24
    date2 = datetime(2021, 12, 24, 0, 0, 1)
    print(test(1, daysToXmas(date2))) # 1
    date3 = datetime(2021, 12, 24, 23, 59, 59)
    print(test(1, daysToXmas(date3))) # 1
    date4 = datetime(2021, 12, 20, 3, 24)
    print(test(5, daysToXmas(date4))) # 5
    date = datetime(2021, 12, 25)
    print(test(0, daysToXmas(date))) # 0
    date1 = datetime(2021, 12, 26)
    print(test(-1, daysToXmas(date1))) # -1
    date2 = datetime(2021, 12, 31)
    print(test(-6, daysToXmas(date2))) # -6
    date3 = datetime(2022, 1, 1, 0, 0, 1)
    print(test(-7, daysToXmas(date3))) # -7
    date4 = datetime(2022, 1, 1, 23, 59, 59)
    print(test(-7, daysToXmas(date4))) # -7


if __name__ == "__main__":
    main()