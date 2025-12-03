def organizeInventory(inventory: list[dict]) -> dict:
    organized_inventory = {}
    
    for model in inventory:
        name = model['name']
        quantity = model['quantity']
        category = model['category']

        if category not in organized_inventory:
            organized_inventory[category] = {}

        current_quantity = organized_inventory[category].get(name, 0)
        organized_inventory[category][name] = current_quantity + quantity

    return organized_inventory


def main():
    inventory = [
        { "name": 'doll', "quantity": 5, "category": 'toys' },
        { "name": 'car', "quantity": 3, "category": 'toys' },
        { "name": 'ball', "quantity": 2, "category": 'sports' },
        { "name": 'car', "quantity": 2, "category": 'toys' },
        { "name": 'racket', "quantity": 4, "category": 'sports' }
    ]

    print(organizeInventory(inventory))

    # Resultado esperado:
    # {
    #   toys: {
    #     doll: 5,
    #     car: 5
    #   },
    #   sports: {
    #     ball: 2,
    #     racket: 4
    #   }

    inventory2 = [
        { "name": 'book', "quantity": 10, "category": 'education' },
        { "name": 'book', "quantity": 5, "category": 'education' },
        { "name": 'paint', "quantity": 3, "category": 'art' }
    ]

    print(organizeInventory(inventory2))

    # Resultado esperado:
    # {
    #   education: {
    #     book: 15
    #   },
    #   art: {
    #     paint: 3
    #   }
    # }


if __name__ == "__main__":
    main()