#Fantasy Game Inventory

stuff = {'rope':1, 'torch':6,'gold coin':42,'dagger':1,'arrow':12}


#for i in stuff.items():
#    print(i)

def displayInventory(inventory):
    print("Inventory :")
    item_total = 0
    for k,v in inventory.items():
        print(str(v)+' '+  k)
        item_total += v
    print ("Total no of items : "+str(item_total))

displayInventory(stuff)

def addtoInventory(inventory,addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] +=1
    return inventory

    
    
    
inv = {'gold coin':42,'rope':1}
dragonLoot=['gold coin','dagger','gold coin','gold coin','ruby']
inv = addtoInventory(inv,dragonLoot)
displayInventory(inv)