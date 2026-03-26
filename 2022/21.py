"""Hay muchas cartas de niños pidiendo regalos y es muy difícil que podamos hacer inventario de todos ellos. Por eso, hemos decidido crear un programa que nos dibuje una tabla con los regalos que nos piden y sus cantidades.

Para ello nos dan un array de objetos con los nombres de los regalos y sus cantidades. Escribe una función que reciba este array y devuelva una cadena con la tabla dibujada.

La tabla siempre usa sólo el espacio justo dependiendo de la longitud de los nombres de los regalos y de las cantidades.

El tamaño de las celdas depende de la longitud de los nombres de los regalos y de las cantidades, aunque como mínimo tendrán que ser del espacio de los títulos Gift y Quantity respectivamente.

La tabla usa los símbolos: + para el borde superior, * para el borde inferior, - para las líneas horizontales y | para las líneas verticales.

Ten en cuenta:
- Usa sólo el espacio que necesitas para dibujar la tabla.
- Adapta la tabla a la longitud de los nombres de los regalos y de las cantidades o los títulos de las columnas.
- No hace falta que ordenes los resultados.
- La tabla no termina con salto de línea."""


def printTable(gifts: list[dict]) -> str:
    cols = [["Gift"] + [gift["name"] for gift in gifts], ["Quantity"] + [str(gift["quantity"]) for gift in gifts]]

    col_1_len = len(max(cols[0], key=len))
    col_2_len = len(max(cols[1], key=len))

    table = ["+" * (7 + col_1_len + col_2_len)]

    for row in range(len(gifts) + 1):
        gift = cols[0][row]
        quantity = cols[1][row]
        
        table.append("| " + gift + " " * (col_1_len - len(gift)) + " | " + quantity + " " * (col_2_len - len(quantity)) + " |")

        if row == 0: table.append("| " + "-" * col_1_len + " | " + "-" * col_2_len + " |")
    
    table.append("+" * (7 + col_1_len + col_2_len))

    return "\n".join(table)


def main():
    print(printTable([
        { "name": 'Game', "quantity": 2 },
        { "name": 'Bike', "quantity": 1 },
        { "name": 'Book', "quantity": 3 }
    ]))
    # +++++++++++++++++++
    # | Gift | Quantity |
    # | ---- | -------- |
    # | Game | 2        |
    # | Bike | 1        |
    # | Book | 3        |
    # *******************

    print(printTable([
        { "name": 'PlayStation 5', "quantity": 9234782374892 },
        { "name": 'Book Learn Web Dev', "quantity": 23531 }
    ]))
    # ++++++++++++++++++++++++++++++++++++++
    # | Gift               | Quantity      |
    # | ------------------ | ------------- |
    # | PlayStation 5      | 9234782374892 |
    # | Book Learn Web Dev | 23531         |
    # **************************************


if __name__ == "__main__":
    main()