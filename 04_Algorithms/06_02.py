# Value count in hash table

items = [
    "apple", "pear", "orange", "banana", "apple",
    "pear", "orange", "banana", "pear", "orange",
    "apple", "kiwi", "pear", "apple", "orange"
]

counter = dict()

for item in items:
    if(item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1


print(counter)