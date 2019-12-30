# inventory.py
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += inventory.get(k, 0)
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    # your code goes here
    for k in addedItems:
        if k not in inventory:
            inventory[k] = 1
        elif k in inventory:
            inventory[k] += 1
    return inventory

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)