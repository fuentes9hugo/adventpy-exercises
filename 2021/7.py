"""Mi amigo Dani está trabajando en una tienda y con la llegada de las navidades tiene el almacén hecho un desastre y no encuentra nada.

Vamos a crear una función contains que recibe dos parámetros: un objeto que define el almacén y el producto que buscamos.

La función debe devolver un booleano que indique si se encuentra el string como valor en algún nivel del objeto.

Ten en cuenta que la tienda es enorme. Tiene diferentes almacenes y, como has visto en los ejemplos, cada uno puede tener diferentes organizaciones.Lo importante es buscar que el producto está en los almacenes."""


def contains(store: dict, product: str) -> bool:
    for value in store.values():
        if isinstance(value, dict):
            if contains(value ,product):
                return True
        
        elif value == product:
            return True

    return False

def test(expected, received):
    return expected == received


def main():
    almacen = {
        'estanteria1': {
            'cajon1': {
                'producto1': 'coca-cola',
                'producto2': 'fanta',
                'producto3': 'sprite'
            }
        },
        'estanteria2': {
            'cajon1': 'vacio',
            'cajon2': {
                'producto1': 'pantalones',
                'producto2': 'camiseta' # <- ¡Está aquí!
            }
        }
    }
                
    print(test(True, contains(almacen, 'camiseta'))) # True

    otroAlmacen = {
        'baul': {
            'fondo': {
                'objeto': 'cd-rom',
                'otro-objeto': 'disquette',
                'otra-cosa': 'mando'
            }
        }
    }
    
    print(test(False, contains(otroAlmacen, 'gameboy'))) # False


if __name__ == "__main__":
    main()