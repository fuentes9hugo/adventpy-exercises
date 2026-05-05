"""Los elfos están preparando la víspera de Navidad y necesitan tu ayuda para calcular si van sobrados o no de tiempo ⏳.

Para ello te pasan un array con la duración de cada entrega. El formato de la duración es HH:mm:ss, las entregas empiezan a las 00:00:00 y el límite de tiempo es 07:00:00.

Tu función debe devolver el tiempo que les faltará o el tiempo que les sobrará para terminar las entregas. El formato de la duración devuelta debe ser HH:mm:ss.

Si terminan antes de las 07:00:00, el tiempo restante hasta las 07:00:00 debe ser mostrado con un signo negativo. Por ejemplo, si sobran 1 hora y 30 minutos, devuelve -01:30:00"""


def calculateTime(deliveries: list[str]) -> str:
    def toSeconds(delivery: str) -> int:
        h, m, s = map(int, delivery.split(":"))

        return h * 3600 + m * 60 + s
    
    def toTimeFormat(seconds):
        negative = "-" if seconds < 0 else ""

        seconds = abs(seconds)

        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        h = abs(h)

        return f"{negative}{h:02d}:{m:02d}:{s:02d}"
    
    limit_time = toSeconds("07:00:00")

    deliveries_time = sum(toSeconds(d) for d in deliveries)

    rest_time = deliveries_time - limit_time

    return toTimeFormat(rest_time)


def test(e, r) -> bool:
    return e == r


def main():
    print(test("-02:20:00", calculateTime(['00:10:00', '01:00:00', '03:30:00'])))
    # '-02:20:00'

    print(test("00:30:00", calculateTime(['02:00:00', '05:00:00', '00:30:00'])))
    # '00:30:00'

    print(test("-05:29:00", calculateTime([
        '00:45:00',
        '00:45:00',
        '00:00:30',
        '00:00:30'
    ]))) # '-05:29:00'


if __name__ == "__main__":
    main()