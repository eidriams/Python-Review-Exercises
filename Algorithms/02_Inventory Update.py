"""Inventory Update
Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery. 
Update the current existing inventory item quantities (in arr1). If an item cannot be found, 
add the new item and quantity into the inventory array. The returned inventory array should be in 
alphabetical order by item."""

# Current Inventory

curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"],
    [21, "Half-Eaten Apple"]
]

# Update with

newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"],
    [5, "Ashurras"]
]

def updinv(lista1,lista2):

    # Creamos un dict en el que las claves seran los productos y los valores, la cantidad de cada uno
    full_inventory = {}
    for item in lista1:
        # La clave sera el elemento 1 de la lista
        key = item[1]
        # El valor sera el elemnto 0 de la lista
        full_inventory[key] = item[0]
    for sitem in lista2:
        skey = sitem[1]
        # Se hace lo mismo con la segunda lista y se añaden los elementos si las claves ya existen
        if skey in full_inventory:
            full_inventory[skey] += sitem[0]
        else:
            full_inventory[skey] = sitem[0]

    order = dict(sorted(full_inventory.items()))

    # Lo volvemos a convertir en lista
    lista_inv = []
    for key,value in order.items():
        mini = [value,key]
        lista_inv.append(mini)

    return f"Iventario actualizado \n{full_inventory}\n\nInventario ordenado\n{order}\n\nFormato Lista:\n{lista_inv}"

print(updinv(curInv,newInv))


