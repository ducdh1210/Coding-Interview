# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Input: root = [1, null, 2, 3]
# Output: [1, 2, 3]

# Input: root = []
# Output: []

# Input: root = [1]
# Output: [1]
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self._preorder_helper(root, result)
        return result

    def _preorder_helper(self, node, result):
        if node:
            result.append(node.val)  # Visit the root
            self._preorder_helper(node.left, result)  # Traverse left
            self._preorder_helper(node.right, result)  # Traverse right


# Test cases
def test_preorder_traversal():
    # Create binary tree:
    #     1
    #      \
    #       2
    #      /
    #     3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solution = Solution()
    print(solution.preorderTraversal(root))  # Output: [1, 2, 3]

    # Create another binary tree:
    #     1
    #    / \
    #   2   3
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)

    print(solution.preorderTraversal(root2))  # Output: [1, 2, 3]

    # Create empty tree
    root3 = None
    print(solution.preorderTraversal(root3))  # Output: []


test_preorder_traversal()
