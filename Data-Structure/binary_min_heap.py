class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class TreeMinHeap:
    def __init__(self):
        self.root = None
        self.last_node = None
        self.size = 0

    def insert(self, value):
        new_node = TreeNode(value)
        self.size += 1

        if not self.root:
            # If the heap is empty, the new node becomes the root
            self.root = new_node
            self.last_node = new_node
        else:
            # Find the position for the new node
            parent = self._find_parent_of_last()
            if not parent.left:
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self.last_node = new_node

        # Restore the min heap property
        self._heapify_up(new_node)

    def _find_parent_of_last(self):
        # Find the parent where the new node should be inserted
        if self.size % 2 == 0:
            return self.last_node.parent
        current = self.last_node
        while current == current.parent.right:
            current = current.parent
        if current.parent.left == current:
            current = current.parent.left
        while current.right:
            current = current.right
        return current

    def _heapify_up(self, node):
        # Move the node up if it's smaller than its parent
        while node.parent and node.value < node.parent.value:
            node.value, node.parent.value = node.parent.value, node.value
            node = node.parent

    def delete_min(self):
        if not self.root:
            return None

        min_value = self.root.value
        if self.size == 1:
            self.root = None
            self.last_node = None
        else:
            # Replace root with last node and remove last node
            self.root.value = self.last_node.value
            parent = self.last_node.parent
            if parent.right == self.last_node:
                parent.right = None
            else:
                parent.left = None
            self.last_node = self._find_new_last()

            # Restore the min heap property
            self._heapify_down(self.root)

        self.size -= 1
        return min_value

    def _find_new_last(self):
        # Find the new last node after deletion
        if self.size % 2 == 1:
            return self.last_node.parent
        current = self.last_node
        while current == current.parent.left:
            current = current.parent
        current = current.parent.left
        while current.right:
            current = current.right
        return current

    def _heapify_down(self, node):
        # Move the node down if it's larger than its children
        while True:
            smallest = node
            if node.left and node.left.value < smallest.value:
                smallest = node.left
            if node.right and node.right.value < smallest.value:
                smallest = node.right
            if smallest == node:
                break
            node.value, smallest.value = smallest.value, node.value
            node = smallest

    def get_min(self):
        # Return the minimum element (root) without removing it
        return self.root.value if self.root else None

    def is_empty(self):
        # Check if the heap is empty
        return self.size == 0


# Example usage
if __name__ == "__main__":
    heap = TreeMinHeap()

    # Insert elements
    for elem in [3, 1, 6, 5, 2, 4]:
        heap.insert(elem)
    print("Heap after insertions. Min value:", heap.get_min())

    # Delete minimum
    print("Deleted minimum:", heap.delete_min())
    print("New min value:", heap.get_min())

    # Insert more elements
    heap.insert(0)
    print("After inserting 0, new min value:", heap.get_min())
