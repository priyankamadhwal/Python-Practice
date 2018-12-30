def displayInventory(inventory):
    print('Inventory:')
    totalItems = 0
    for k, v in inventory.items():
        print(v,k)
        totalItems += v
    print('Total number of items:',totalItems)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
