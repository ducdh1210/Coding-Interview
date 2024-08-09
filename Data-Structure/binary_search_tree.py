class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a new value into the BST."""
        if not self.root:
            # If the tree is empty, create a new root node
            self.root = Node(value)
        else:
            # Otherwise, use recursive helper function to insert the new node
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Recursive helper function for insert."""
        if value < node.value:
            if node.left is None:
                # If there's no left child, insert the new node here
                node.left = Node(value)
            else:
                # Otherwise, recursively insert into the left subtree
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                # If there's no right child, insert the new node here
                node.right = Node(value)
            else:
                # Otherwise, recursively insert into the right subtree
                self._insert_recursive(node.right, value)

    def search(self, value):
        """Search for a value in the BST."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Recursive helper function for search."""
        if node is None or node.value == value:
            # Base case: node is None (value not found) or value is found
            return node
        if value < node.value:
            # If the value is less than the current node's value, search in the left subtree
            return self._search_recursive(node.left, value)
        # If the value is greater than the current node's value, search in the right subtree
        return self._search_recursive(node.right, value)

    def delete(self, value):
        """Delete a value from the BST."""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        """Recursive helper function for delete."""
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node to delete found
            if node.left is None:
                # Case 1 and 2: No child or only right child
                return node.right
            elif node.right is None:
                # Case 2: Only left child
                return node.left

            # Case 3: Two children
            # Find the inorder successor (smallest in the right subtree)
            min_node = self._find_min(node.right)
            node.value = min_node.value
            # Delete the inorder successor
            node.right = self._delete_recursive(node.right, min_node.value)

        return node

    def _find_min(self, node):
        """Find the minimum value node in a subtree."""
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self):
        """Perform an inorder traversal of the BST."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Recursive helper function for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        """Perform a preorder traversal of the BST."""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        """Recursive helper function for preorder traversal."""
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        """Perform a postorder traversal of the BST."""
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        """Recursive helper function for postorder traversal."""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def level_order_traversal(self):
        """Perform a level-order traversal of the BST."""
        if not self.root:
            return []

        result = []
        queue = [self.root]

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

    def height(self):
        """Calculate the height of the BST."""
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        """Recursive helper function to calculate height."""
        if not node:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

    def is_bst(self):
        """Check if the tree is a valid BST."""
        return self._is_bst_recursive(self.root, float("-inf"), float("inf"))

    def _is_bst_recursive(self, node, min_value, max_value):
        """Recursive helper function to check BST property."""
        if not node:
            return True

        if node.value <= min_value or node.value >= max_value:
            return False

        return self._is_bst_recursive(
            node.left, min_value, node.value
        ) and self._is_bst_recursive(node.right, node.value, max_value)

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


# Test the Binary Search Tree implementation
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Test insertion
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        bst.insert(value)

    # Test search
    print("Search for 4:", bst.search(4).value if bst.search(4) else "Not found")
    print("Search for 9:", bst.search(9).value if bst.search(9) else "Not found")

    # Test traversals
    print("Inorder traversal:", bst.inorder_traversal())
    print("Preorder traversal:", bst.preorder_traversal())
    print("Postorder traversal:", bst.postorder_traversal())
    print("Level-order traversal:", bst.level_order_traversal())

    # Test height
    print("Tree height:", bst.height())

    # Test is_bst
    print("Is BST?", bst.is_bst())

    # Test deletion
    bst.delete(3)
    print("Inorder traversal after deleting 3:", bst.inorder_traversal())

    # Test invalid BST
    invalid_bst = BinarySearchTree()
    invalid_bst.root = Node(5)
    invalid_bst.root.left = Node(3)
    invalid_bst.root.right = Node(7)
    invalid_bst.root.left.right = Node(6)  # This makes it an invalid BST
    print("Is invalid BST?", invalid_bst.is_bst())

    # Test find_nearest
    print("Find nearest to 2.5:", bst.find_nearest(2.5))
    print("Find nearest to 7.5:", bst.find_nearest(7.5))
    print("Find nearest to 10:", bst.find_nearest(10))
