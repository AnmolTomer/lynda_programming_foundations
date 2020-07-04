# AKA Dictionaries in Python : Key-Value pair : Associative Array
# Benefits:
# Ability to uniquely map a given key to a specific value.
# Hash tables are typically faster than other kinds of table and lookup structues
# particularly.


# TODO: Create a hashtable all at once

items1 = dict({"key1": 1, "key2": 2, "key3": "three", "key4": 4})
print(items1)

# TODO: Create a hashtableprogressively
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3

print(items2)

# TODO: Try to access a non-existent key
# print(items1["key8"]) # You will get key-error

# TODO: Replace an item
items1["key1"] = 11

print(items1)

# TODO: Iterate over all contents of a hash table

print("Printing key-value format of hash-table keys1:")
for key, value in items1.items():
    print(f"Key: {key}, Value: {value}")
