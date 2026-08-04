def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume the current index has the minimum element
        min_index = i

        # Find the index of the minimum element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Get user input
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Original list:", numbers)

selection_sort(numbers)

print("Sorted list:", numbers)
