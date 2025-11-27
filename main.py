def generateGiftSets(gifts: list):
    # Lista donde se almacenarán todas las combinaciones de regalos encontradas.
    setted_gifts = []

    # La función recursiva de backtracking.
    # index: El índice en 'gifts' desde donde debemos empezar a buscar el siguiente juguete.
    # actual_set: La combinación de regalos que estamos construyendo en la rama actual.
    def backtrack(index: int, actual_set: list):
        # Itera sobre los juguetes restantes en 'gifts', empezando desde 'index'.
        # enumerate(..., start=index) asegura que 'i' sea el índice real
        # en la lista original 'gifts', lo cual es crucial.
        for i, gift in enumerate(gifts[index:], start=index):
            
            # --- Paso 1: "ELEGIR" (Explorar con el regalo incluido) ---
            
            # 1.1 Incluir el regalo actual en el conjunto temporal.
            actual_set.append(gift)
            
            # 1.2 Guardar la combinación actual como un resultado válido.
            # Usamos .copy() para guardar una instantánea del set, ya que 'actual_set'
            # se modificará en los pasos siguientes (mutabilidad).
            setted_gifts.append(actual_set.copy())
            
            # 1.3 Llamada recursiva (Backtracking): Avanza a la siguiente posición.
            # Llamamos a backtrack(i + 1) para garantizar que solo seleccionemos
            # juguetes que están DESPUÉS de 'gift' en la lista original. 
            # Esto previene duplicados (ej. evita [doll, car] si ya hicimos [car, doll]).
            backtrack(i + 1, actual_set)
            
            # --- Paso 2: "DESELEGIR" (El paso de Backtracking/Limpieza) ---
            
            # 2.1 Deshacer el cambio: Eliminar el regalo para volver al estado anterior.
            # Esto permite que el bucle 'for' pruebe la siguiente opción (el siguiente 'gift')
            # sin que el 'gift' actual esté presente en el 'actual_set'.
            actual_set.remove(gift)

    # Inicia el proceso de backtracking:
    # Empezamos en el índice 0 con un set de regalo vacío [].
    backtrack(0, [])
    
    # Después de generar todos los sets, la función sort los ordena por tamaño (longitud).
    # Esto cumple con la restricción de que las combinaciones de 1 juguete van primero, luego 2, etc.
    setted_gifts = sorted(setted_gifts, key=len)
    
    return setted_gifts


"""def generateGiftSets(gifts: list):
    setted_gifts = []
    def backtrack(index: int, actual_set: list):
        for i, gift in enumerate(gifts[index:], start=index):
            actual_set.append(gift)
            setted_gifts.append(actual_set.copy())
            backtrack(i + 1, actual_set)
            actual_set.remove(gift)

    backtrack(0, [])
    setted_gifts.sort(key=len)
    return setted_gifts"""


def main():
    print(generateGiftSets(['car', 'doll', 'puzzle']))
    # [
    #   ['car'],
    #   ['doll'],
    #   ['puzzle'],
    #   ['car', 'doll'],
    #   ['car', 'puzzle'],
    #   ['doll', 'puzzle'],
    #   ['car', 'doll', 'puzzle']
    # ]

    print(generateGiftSets(['ball']))
    # [
    #   ['ball']
    # ]

    print(generateGiftSets(['game', 'pc']))
    # [
    #   ['game'],
    #   ['pc'],
    #   ['game', 'pc']
    # ]




if __name__ == "__main__":
    main()