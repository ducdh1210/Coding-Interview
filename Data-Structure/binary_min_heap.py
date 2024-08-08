class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent)

    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        if min_index != i:
            self.swap(i, min_index)
            self._heapify_down(min_index)

    def display(self):
        print(self.heap)


# Test code
if __name__ == "__main__":
    min_heap = MinHeap()

    print("Inserting elements into the min-heap:")
    elements = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    for element in elements:
        min_heap.insert(element)
        print(f"Inserted: {element}")
        min_heap.display()

    print("\nExtracting minimum elements:")
    for _ in range(len(elements)):
        min_val = min_heap.extract_min()
        print(f"Extracted min: {min_val}")
        min_heap.display()

    print("\nIs heap empty?", len(min_heap.heap) == 0)

    try:
        min_heap.extract_min()
    except IndexError as e:
        print("\nError:", str(e))
