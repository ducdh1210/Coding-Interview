class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None  # Left child
        self.right = None  # Right child


class BinarySearchTree:
    def __init__(self):
        self.root = None  # Root node of the BST

    def insert(self, value):
        """Insert a new value into the BST."""
        if not self.root:
            # If the tree is empty, create a new root node
            self.root = TreeNode(value)
        else:
            # Otherwise, use recursive helper function to insert the new node
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Recursive helper function for insert."""
        if value < node.value:
            if node.left is None:
                # If there's no left child, insert the new node here
                node.left = TreeNode(value)
            else:
                # Otherwise, recursively insert into the left subtree
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                # If there's no right child, insert the new node here
                node.right = TreeNode(value)
            else:
                # Otherwise, recursively insert into the right subtree
                self._insert_recursive(node.right, value)

    def find_nearest(self, target):
        """Find the value in the BST nearest to the target."""
        if not self.root:
            return None  # Tree is empty

        nearest = self.root.value  # Start with root as nearest
        current = self.root

        while current:
            # Update nearest if current node is closer to target
            if abs(current.value - target) < abs(nearest - target):
                nearest = current.value

            if target < current.value:
                if not current.left:
                    break  # No more left children, end search
                current = current.left
            elif target > current.value:
                if not current.right:
                    break  # No more right children, end search
                current = current.right
            else:
                return current.value  # Exact match found

        return nearest


# Helper function to build BST from a list
def build_bst_from_list(numbers):
    """Create a BST from a list of numbers."""
    bst = BinarySearchTree()
    for num in numbers:
        bst.insert(num)
    return bst


# Test the implementation
if __name__ == "__main__":
    numbers = [5, 2, 8, 1, 3, 7, 9, 4, 6]
    bst = build_bst_from_list(numbers)

    test_cases = [0, 2.5, 5, 7.5, 10]

    print("Numbers in BST:", numbers)
    for target in test_cases:
        nearest = bst.find_nearest(target)
        print(f"Nearest to {target}: {nearest}")
