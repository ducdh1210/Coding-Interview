class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # DFS Traversals

    def dfs_preorder(self):
        """
        Depth-First Search: Preorder Traversal (Root -> Left -> Right)
        """

        def preorder(node):
            if node:
                print(node.value, end=" ")  # Visit the root
                preorder(node.left)  # Traverse left subtree
                preorder(node.right)  # Traverse right subtree

        preorder(self.root)
        print()  # New line for formatting

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

    def dfs_iterative(self):
        """
        Depth-First Search: Iterative implementation (Preorder traversal)
        """
        if not self.root:
            return

        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.value, end=" ")

            # Push right child first so that left is processed first (LIFO)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        print()  # New line for formatting

    # BFS Traversal
    def bfs(self):
        """
        Breadth-First Search: Level Order Traversal
        """
        if not self.root:
            return

        queue = [self.root]
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                print(node.value, end=" ")

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()  # New line after each level

    def height(self):
        """
        Calculate the height of the binary tree.
        Height is defined as the number of edges in the longest path from the root to a leaf.
        """

        def calculate_height(node):
            if not node:
                return -1  # Return -1 for null nodes (height of empty tree)
            left_height = calculate_height(node.left)  # Height of left subtree
            right_height = calculate_height(node.right)  # Height of right subtree
            return 1 + max(left_height, right_height)  # Return height of the tree

        return calculate_height(self.root)  # Start from the root


# Example usage and testing
if __name__ == "__main__":
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
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    tree.root.right.right = TreeNode(6)
    tree.root.left.right.left = TreeNode(7)

    print("Height of the tree:", tree.height())  # Output the height of the tree

    # print("DFS Preorder Traversal:")
    # tree.dfs_preorder()

    # print("\nDFS Inorder Traversal:")
    # tree.dfs_inorder()

    # print("\nDFS Postorder Traversal:")
    # tree.dfs_postorder()

    # print("\nDFS Iterative Traversal (Preorder):")
    # tree.dfs_iterative()

    # print("\nBFS Level Order Traversal:")
    # tree.bfs()
