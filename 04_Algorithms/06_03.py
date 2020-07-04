list1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def find_max(items):
    if (len(items) == 1):
        return items[0]

    item1 = items[0]
    print(f"Item1 = {item1}")
    item2 = find_max(items[1:])
    print(f"Item2 = {item2}")

    if item1 > item2:
        return item1
    else:
        return item2


print(find_max(list1))
