class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # DFS search
    def dfs_preorder(self):
        """
        Depth-First Search: Preorder Traversal (Root -> Left -> Right)
        """

        def preorder(node):
            if node:
                print(node.value, end=" ")
                preorder(node.right)
                preorder(node.left)

        preorder(self.root)

    def dfs_inorder(self):
        """
        Depth-First Search: Inorder Traversal (Left -> Root -> Right)
        """

        def inorder(node):
            if node:
                inorder(node.left)  # Traverse left subtree
                print(node.value, end=" ")  # Visit the root
                inorder(node.right)  # Traverse right subtree

        inorder(self.root)
        print()  # New line for formatting

    def dfs_postorder(self):
        """
        Depth-First Search: Postorder Traversal (Left -> Right -> Root)
        """

        def postorder(node):
            if node:
                postorder(node.left)  # Traverse left subtree
                postorder(node.right)  # Traverse right subtree
                print(node.value, end=" ")  # Visit the root

        postorder(self.root)
        print()  # New line for formatting


# Create a sample binary tree
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
#      /
#     7
tree = BinaryTree()
tree.root = TreeNode(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
# tree.root.left.left = TreeNode(4)
# tree.root.left.right = TreeNode(5)
# tree.root.right.right = TreeNode(6)
# tree.root.left.right.left = TreeNode(7)

tree.dfs_preorder()
