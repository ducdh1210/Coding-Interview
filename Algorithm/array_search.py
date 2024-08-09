# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not in the array


# Binary Search (for sorted arrays)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Return -1 if the target is not in the array


# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original array:", arr)

    # Searching
    print("Linear search for 25:", linear_search(arr, 25))
    print("Binary search for 25 (on sorted array):", binary_search(sorted(arr), 25))

    print("Built-in sorted():", sorted(arr))
    arr.sort()
    print("Built-in sort():", arr)
    print("Built-in index():", arr.index(25))
