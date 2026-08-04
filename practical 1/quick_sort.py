def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return left + middle + right

# Get user input
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Original list:", numbers)

sorted_numbers = quick_sort(numbers)

print("Sorted list:", sorted_numbers)
