def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Get user input
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Original list:", numbers)

insertion_sort(numbers)

print("Sorted list:", numbers)
