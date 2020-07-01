# Iteration: Repeat the same procedure until it reaches a end point.
# Specify the data to iterate over,what to do to data at every step, and we need to specify when our loop should stop.
# Infinite Loop: Bug that may occur when ending condition speicified incorrectly or not specified.

spices = [
    'salt',
    'pepper',
    'cumin',
    'turmeric'
]

for spice in spices:  # in is a python keyword that indicates that what follows is the set of values that we want to iterate over
    print(spice)

print("No more boring omelettes!")
