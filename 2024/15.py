"""Al Polo Norte ha llegado ChatGPT y el elfo Sam Elfman está trabajando en una aplicación de administración de regalos y niños.

Para mejorar la presentación, quiere crear una función drawTable que reciba un array de objetos y lo convierta en una tabla de texto.

La tabla dibujada debe representar los datos del objeto de la siguiente manera:

- Tiene una cabecera con el nombre de la columna.
- El nombre de la columna pone la primera letra en mayúscula.
- Cada fila debe contener los valores de los objetos en el orden correspondiente.
- Cada valor debe estar alineado a la izquierda.
- Los campos dejan siempre un espacio a la izquierda.
- Los campos dejan a la derecha el espacio necesario para alinear la caja.

Mira el ejemplo para ver cómo debes dibujar la tabla:"""


def drawTable(data: list[dict[str, str | int]]) -> str:
    cols_names = tuple(data[0].keys())
    rows_num = len(data) + 1
    table_data = {}

    for i, row in enumerate(data, start=1):
        for j, col in enumerate(cols_names, start=1):
            if i == 1:
                table_data[j] = {"values": [col.capitalize()]}
            table_data[j]["values"].append(f"{row[col]}")

            if i == len(data):
                table_data[j]["width"] = len(max(table_data[j]["values"], key=len))

    table_limit = ["+"]
    for data_col in table_data.values():
        table_limit.append("-" * data_col["width"] + "-" * 2 + "+")
    table_limit = "".join(table_limit)

    table = [table_limit]

    for row in range(rows_num):
        table_row = ["|"]
        for table_col in table_data.values():
            table_row.append(" " + table_col["values"][row] + " " * (table_col["width"] - len(table_col["values"][row])) + " |")

        table_row = "".join(table_row)
        table.append(table_row)

        if row == 0: table.append(table_limit)
    
    table.append(table_limit)

    table = "\n".join(table).strip()

    return table


def main():
    print(drawTable([
        { "name": 'Alice', "city": 'London' },
        { "name": 'Bob', "city": 'Paris' },
        { "name": 'Charlie', "city": 'New York' }
    ]))
    # +---------+-----------+
    # | Name    | City      |
    # +---------+-----------+
    # | Alice   | London    |
    # | Bob     | Paris     |
    # | Charlie | New York  |
    # +---------+-----------+

    print(drawTable([
        { "gift": 'Doll', "quantity": 10 },
        { "gift": 'Book', "quantity": 5 },
        { "gift": 'Music CD', "quantity": 1 }
    ]))
    # +----------+----------+
    # | Gift     | Quantity |
    # +----------+----------+
    # | Doll     | 10       |
    # | Book     | 5        |
    # | Music CD | 1        |
    # +----------+----------+

    print(drawTable([
        { "gift": 'Doll', "quantity": 10, "status": True },
        { "gift": 'Book', "quantity": 5, "status": False },
        { "gift": 'Music CD', "quantity": 1, "status": None }
    ]))


if __name__ == "__main__":
    main()