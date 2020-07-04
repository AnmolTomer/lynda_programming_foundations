def bubbleSort(dataset):
    for i in range(len(dataset)-1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                dataset[j], dataset[j+1] = dataset[j+1], dataset[j]
        print(f"Current state: {dataset}")


def main():
    list1 = [6, 20, 8, 9, 19, 56, 23, 87, 41, 49, 53]
    bubbleSort(list1)
    print(f"Result: {list1}")


if __name__ == "__main__":
    main()
