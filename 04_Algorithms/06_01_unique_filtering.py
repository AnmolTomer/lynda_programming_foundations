# use hashtable to filter out duplicate items

# define a set of items that we want to reduce duplicates

items = [
    "apple", "pear", "orange", "banana", "apple",
    "pear", "orange", "banana", "pear", "orange",
    "apple", "kiwi", "pear", "apple", "orange"
]

# TODO: create a hashtable to perform a filter

filter = dict()

# TODO: Loop over each item and add to the hash table

for key in items:
    filter[key] = 0

# TODO: create a set from the resulting keys in hashtable

result = set(filter.keys())
print(result)
