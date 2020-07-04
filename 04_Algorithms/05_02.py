# Better to search in a binary fashion in sorted list.
items = [6, 20, 8, 9, 19, 56, 23, 87, 41, 49, 53]


def binarySearch(item, itemList):
    # Get list size
    listSize = len(itemList)-1
    # start at two ends of the list
    lowerIdx = 0
    upperIdx = listSize

    while lowerIdx <= upperIdx:
        middle = (upperIdx+lowerIdx) // 2
        if itemList[middle] == item:
            return middle

        if item > itemList[middle]:
            lowerIdx = middle+1
        else:
            upperIdx = middle-1

    if lowerIdx > upperIdx:
        return None


items = items.sort()
binarySearch(56, items)
