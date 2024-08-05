class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)
        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self._search_recursive(root.right, key)
        return self._search_recursive(root.left, key)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, root):
        if root:
            self._inorder_recursive(root.left)
            print(root.val, end=" ")
            self._inorder_recursive(root.right)


# Usage example
if __name__ == "__main__":
    bst = BinarySearchTree()
    keys = [50, 30, 20, 40, 70, 60, 80]

    for key in keys:
        bst.insert(key)

    print("Inorder traversal of the BST:")
    bst.inorder_traversal()
    print("\n")

    search_key = 60
    if bst.search(search_key):
        print(f"{search_key} is found in the BST")
    else:
        print(f"{search_key} is not found in the BST")
