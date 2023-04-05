print('#list')
def appendItem(itemName, itemList=None):
    
    itemList = []
    itemList.append(itemName)
    return itemList
 
 
print(appendItem('notebook'))
print(appendItem('pencil'))
print(appendItem('eraser'))
 
 
# using None as value of default parameter
 
print('\n\n#dictionary')
def addItemToDictionary(itemName, quantity, itemList = None):
    if itemList == None:
        itemList = {}
    itemList[itemName] = quantity
    return itemList
 
 
print(addItemToDictionary('notebook', 4))
print(addItemToDictionary('pencil', 1))
print(addItemToDictionary('eraser', 1))

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 14,514, 1444444, key=mod_5,),
    sep='\n',
)
help(round)