class ArrayMinHeap:
    def __init__(self):
        # Initialize an empty list to store the heap elements
        self.heap = []

    def parent(self, i):
        # Return the index of the parent node
        return (i - 1) // 2

    def left_child(self, i):
        # Return the index of the left child
        return 2 * i + 1

    def right_child(self, i):
        # Return the index of the right child
        return 2 * i + 2

    def swap(self, i, j):
        # Swap elements at indices i and j
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        # Add the new key to the end of the array
        self.heap.append(key)
        # Restore the min heap property by moving the new key up if necessary
        self._heapify_up(len(self.heap) - 1)

    def delete_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Save the minimum value to return later
        min_val = self.heap[0]
        # Move the last element to the root
        self.heap[0] = self.heap.pop()
        # Restore the min heap property by moving the new root down if necessary
        self._heapify_down(0)
        return min_val

    def _heapify_up(self, i):
        # Move the element at index i up to its correct position
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent)

    def _heapify_down(self, i):
        # Move the element at index i down to its correct position
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        # Find the smallest among the node and its children
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        # If the smallest is not the current node, swap and continue heapifying down
        if min_index != i:
            self.swap(i, min_index)
            self._heapify_down(min_index)

    def get_min(self):
        # Return the minimum element (root) without removing it
        return self.heap[0] if self.heap else None

    def size(self):
        # Return the number of elements in the heap
        return len(self.heap)

    def is_empty(self):
        # Check if the heap is empty
        return len(self.heap) == 0

    def build_heap(self, arr):
        # Build a heap from an array
        self.heap = arr.copy()
        # Start from the last non-leaf node and heapify down
        for i in range(len(arr) // 2, -1, -1):
            self._heapify_down(i)


# Example usage
if __name__ == "__main__":
    heap = ArrayMinHeap()

    # Insert elements
    for elem in [3, 1, 6, 5, 2, 4]:
        heap.insert(elem)
    print("Heap after insertions:", heap.heap)

    # Get and delete minimum
    print("Minimum element:", heap.get_min())
    print("Deleted minimum:", heap.delete_min())
    print("Heap after deleting minimum:", heap.heap)

    # Build heap from array
    heap.build_heap([7, 8, 9, 1, 2, 3])
    print("Heap after building from array:", heap.heap)
