# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
    return arr


# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# # Using built-in methods
# # Sorting
# sorted_arr = sorted([3, 1, 4, 1, 5, 9, 2, 6])  # Returns a new sorted list
# arr = [3, 1, 4, 1, 5, 9, 2, 6]
# arr.sort()  # Sorts the list in-place

# # Searching
# arr = [1, 2, 3, 4, 5]
# index = arr.index(3)  # Returns the index of the first occurrence of 3

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original array:", arr)

    print("Bubble sort:", bubble_sort(arr.copy()))
    print("Quick sort:", quick_sort(arr))

    # Built-in methods
    print("Built-in sorted():", sorted(arr))
    arr.sort()
    print("Built-in sort():", arr)
    print("Built-in index():", arr.index(25))
