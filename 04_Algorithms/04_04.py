# Quicksort: D&C Algo, Uses Recursion to sort items, Generally performs better than merge sort O(n logn). Operates in place on data, doesn't needs extra memory.
# Worst case O(n^2) when data is mostly sorted already. But this is rare.
# Pivot point selection:

items = [6, 20, 8, 9, 19, 56, 23, 87, 41, 49, 53]


def quickSort(dataset, first, last):
    if(first < last):
        pivotIdx = partition(dataset, first, last)

        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)


def partition(datavalues, first, last):
    pivotValue = datavalues[first]

    lower = first+1
    upper = last

    done = False
    while not done:
        # TODO: Advance the lower index i.e. incrememnt it till value at index of lower is less than pivot value and lower doesn't cross upper index
        while lower <= upper and datavalues[lower] <= pivotValue:
            lower += 1

# TODO: Advance the upper index, i.e. keep decrementing the upper index if datavalue at upper index is more than pivot value and index upper > index lower
        while datavalues[upper] >= pivotValue and upper >= lower:
            upper -= 1

        # TODO: If the two indexes cross each other, i.e. value of upper which was more in beginning becomes < value of lower we found the split
        if upper < lower:
            done = True  # Found the crossing point
        else:  # if they haven't crossed each other exchange the values
            datavalues[lower], datavalues[upper] = datavalues[upper], datavalues[lower]

    # when split point is found, exchange pivot value
    datavalues[first], datavalues[upper] = datavalues[upper], datavalues[first]

    return upper


print(items)
quickSort(items, 0, len(items))
print(items)
