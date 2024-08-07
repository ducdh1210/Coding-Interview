# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]


# Input: head = [1, 2]
# Output: [2, 1]

# Input: head = []
# Output: []

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        while current:
            next_node = current.next  # Store next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev to current
            current = next_node  # Move to next node
        return prev  # New head of the reversed list


# Test cases
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
reversed_head = solution.reverseList(head)
print_list(reversed_head)  # Output: 5 -> 4 -> 3 -> 2 -> 1 -> None

# Create linked list: 1 -> 2
head2 = ListNode(1, ListNode(2))
reversed_head2 = solution.reverseList(head2)
print_list(reversed_head2)  # Output: 2 -> 1 -> None

# Create empty linked list
head3 = None
reversed_head3 = solution.reverseList(head3)
print_list(reversed_head3)  # Output: None
