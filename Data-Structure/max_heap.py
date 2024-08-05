class MaxHeap:
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
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return max_val

    def _heapify_down(self, i):
        max_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left

        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right

        if i != max_index:
            self.swap(i, max_index)
            self._heapify_down(max_index)

    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(arr) // 2 - 1, -1, -1):
            self._heapify_down(i)


# Usage example
if __name__ == "__main__":
    heap = MaxHeap()
    arr = [3, 10, 5, 22, 4, 15]
    heap.build_heap(arr)
    print("Max Heap:", heap.heap)
    print("Extract max:", heap.extract_max())
    print("Heap after extract:", heap.heap)
    heap.insert(30)
    print("Heap after inserting 30:", heap.heap)
