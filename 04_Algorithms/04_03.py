# Merge Sort: D&C Algo, Breaks data into individual pieces and merges them, uses recursion to operate on datasets. Key is to understand how to merge 2 sorted arrays.

items = [6, 20, 8, 9, 19, 56, 23, 87, 41, 49, 53]


def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # TODO: Recursively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)

        # TODO: Perform merging
        i = 0  # index into the left array
        j = 0  # index into the right array
        k = 0  # index into the merger array

        while i < len(leftarr) and j < len(rightarr):
            if(leftarr[i] <= rightarr[j]):
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1


print(items)
mergesort(items)
print(items)
