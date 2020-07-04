items = [6, 20, 8, 9, 19, 56, 23, 87, 41, 49, 53]


def find_item(item, itemList):
    for obj in range(0, len(itemList)):
        if(item == itemList[obj]):
            return obj

    return None


print(f"Found 87 at index: {find_item(87, items)}")
print(f"Is 99 available? {find_item(99, items)}")
# Average search time incereases by number of items added in an unsorted list.
