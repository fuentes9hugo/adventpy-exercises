"""Santa Claus tiene una agenda mágica 📇 donde guarda las direcciones de los niños para entregar los regalos. El problema: la información de la agenda está mezclada y malformateada. Las líneas contienen un número de teléfono mágico, el nombre de un niño y su dirección, pero todo está rodeado de caracteres extraños.

Santa necesita tu ayuda para encontrar información específica de la agenda. Escribe una función que, dado el contenido de la agenda y un número de teléfono, devuelva el nombre del niño y su dirección.

Ten en cuenta que en la agenda:

Los números de teléfono están formateados como +X-YYY-YYY-YYY (donde X es uno o dos dígitos, e Y es un dígito).
El nombre de cada niño está siempre entre < y >
La idea es que escribas una funcióna que, pasándole el teléfono completo o una parte, devuelva el nombre y dirección del niño. Si no encuentra nada o hay más de un resultado, debes devolver null."""


def findInAgenda(agenda: str, phone: str) -> dict | None:
    agenda = agenda.split("\n")
    matches = 0
    contact = {
        "name": "",
        "address": ""
    }

    for person in agenda:
        if phone in person:
            matches += 1
            if matches > 1:
                break
            start_phone_num = person.find("+")
            person = person.replace(person[start_phone_num:start_phone_num + 15], "")

            start_name = person.find("<")
            end_name = person.find(">")
            contact["name"] = person[start_name + 1:end_name]
            person = person.replace(person[start_name:end_name + 1], "")
            
            contact["address"] = person.strip()
    
    return None if matches == 0 or matches > 1 else contact


def test(expected, received):
    return expected == received


def main():
    agenda = "+34-600-123-456 Calle Gran Via 12 <Juan Perez>\n" \
    "Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654\n" \
    "<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York"

    print(test({ "name": "Juan Perez", "address": "Calle Gran Via 12" }, findInAgenda(agenda, '34-600-123-456')))
    # { name: "Juan Perez", address: "Calle Gran Via 12" }

    print(test({ "name": "Maria Gomez", "address": "Plaza Mayor 45 Madrid 28013" }, findInAgenda(agenda, '600-987')))
    # { name: "Maria Gomez", address: "Plaza Mayor 45 Madrid 28013" }

    print(test(None, findInAgenda(agenda, '111')))
    # null
    # Explicación: No hay resultados

    print(test(None, findInAgenda(agenda, '1')))
    # null
    # Explicación: Demasiados resultados


if __name__ == "__main__":
    main()