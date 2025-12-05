"""Los elfos tienen un timestamp secreto: es la fecha y hora exacta en la que Papá Noel despega con el trineo 🛷 para repartir regalos por el mundo. Pero en el Polo Norte usan un formato rarísimo para guardar la hora: YYYY*MM*DD@HH|mm|ss NP (ejemplo: 2025*12*25@00|00|00 NP).

Tu misión es escribir una función que reciba:

fromTime → fecha de referencia en formato elfo (YYYY*MM*DD@HH|mm|ss NP).
takeOffTime → la misma fecha de despegue, también en formato elfo.
La función debe devolver:

Los segundos completos que faltan para el despegue.
Si ya estamos en el despegue exacto → 0.
Si el despegue ya ocurrió → un número negativo indicando cuántos segundos han pasado desde entonces.
🎯 Reglas
Convierte el formato elfo a un timestamp primero. El sufijo NP indica la hora oficial del Polo Norte (sin husos horarios ni DST), así que puedes tratarlo como si fuera UTC.
Usa diferencias en segundos, no en milisegundos.
Redondea siempre hacia abajo (floor): solo segundos completos."""

from datetime import datetime


def test(expected, received):
    return True if expected == received else False


def timeUntilTakeOff(from_time: str, take_off_time: str) -> int:
    # Definimos el formato "raro" de los elfos para que Python lo entienda
    # %Y = Año, %m = Mes, %d = Día, %H = Hora, %M = Minuto, %S = Segundo
    elf_format = "%Y*%m*%d@%H|%M|%S NP"
    
    # Convertimos las cadenas de texto a objetos de fecha reales
    date_from = datetime.strptime(from_time, elf_format)
    date_takeoff = datetime.strptime(take_off_time, elf_format)
    
    # Calculamos la diferencia
    difference = date_takeoff - date_from
    
    # Devolvemos los segundos totales como entero
    return int(difference.total_seconds())


def main():
    takeoff = '2025*12*25@00|00|00 NP'

    # desde el 24 diciembre 2025, 23:59:30, 30 segundos antes del despegue
    print(test(30, timeUntilTakeOff('2025*12*24@23|59|30 NP', takeoff)))
    # 30

    # justo en el momento exacto
    print(test(0, timeUntilTakeOff('2025*12*25@00|00|00 NP', takeoff)))
    # 0

    # 12 segundos después del despegue
    print(test(-12, timeUntilTakeOff('2025*12*25@00|00|12 NP', takeoff)))
    # -12


if __name__ == "__main__":
    main()