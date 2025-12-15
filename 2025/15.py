"""Al Polo Norte ha llegado ChatGPT y el elfo Sam Elfman está trabajando en una aplicación de administración de regalos y niños.

Para mejorar la presentación, quiere crear una función drawTable que reciba un array de objetos y lo convierta en una tabla de texto.

La tabla dibujada debe tener:

Cabecera con letras de columna (A, B, C…).
El contenido de la tabla son los valores de los objetos.
Los valores deben estar alineados a la izquierda.
Los campos dejan siempre un espacio a la izquierda.
Los campos dejan a la derecha el espacio necesario para alinear la caja.
La función recibe un segundo parámetro sortBy que indica el nombre del campo por el que se deben ordenar las filas. El orden será alfabético ascendente si los valores son strings y numérico ascendente si son números.

Mira el ejemplo para ver cómo debes dibujar la tabla:"""


def drawTable(data: list[dict[str, str | int]], sortBy: str) -> str:
    data_map = [tuple(value for value in row.values()) for row in data]
    
    sort_by_index = tuple(data[0].keys()).index(sortBy)
    data_map.sort(key=lambda x: x[sort_by_index])

    column_width = []
    for row in data_map:
        for i, col in enumerate(row):
            if len(column_width) < i + 1: column_width.append(len(str(col)))

            if len(str(col)) > column_width[i]:
                column_width[i] = len(str(col))
    
    column_headers = (chr(i) for i in range(ord("A"), ord("Z") + 1))
    
    table_limit = ["+" + "-" * (width + 2) for width in column_width]
    table_limit.append("+")
    table_limit = "".join(table_limit)

    table = [table_limit]
    header_row = ["|"]

    for i, row in enumerate(data_map):
        table_row = ["|"]
        for j, col in enumerate(row):
            if i == 0:
                header = next(column_headers)
                header_row.append(" " + header + " " * (column_width[j] - len(header)) + " |")
                if j == len(row) - 1:
                    header_row = "".join(header_row)
                    table.append(header_row)
                    table.append(table_limit)

            table_row.append(" " + str(col) + " " * (column_width[j] - len(str(col))) + " |")

            if j == len(row) - 1:
                table_row = "".join(table_row)
                table.append(table_row)

    table.append(table_limit)   

    return "\n".join(table)


def main():
    print(drawTable(
    [
        { "name": 'Charlie', "city": 'New York' },
        { "name": 'Alice', "city": 'London' },
        { "name": 'Bob', "city": 'Paris' }
    ],
    'name'
    ))
    # +---------+----------+
    # | A       | B        |
    # +---------+----------+
    # | Alice   | London   |
    # | Bob     | Paris    |
    # | Charlie | New York |
    # +---------+----------+

    print(drawTable(
    [
        { "gift": 'Book', "quantity": 5 },
        { "gift": 'Music CD', "quantity": 1 },
        { "gift": 'Doll', "quantity": 10 }
    ],
    'quantity'
    ))
    # +----------+----+
    # | A        | B  |
    # +----------+----+
    # | Music CD | 1  |
    # | Book     | 5  |
    # | Doll     | 10 |
    # +----------+----+


if __name__ == "__main__":
    main()