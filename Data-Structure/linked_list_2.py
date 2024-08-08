# Node class represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # The data stored in the node
        self.next = None  # Reference to the next node, initially None


# SinglyLinkedList class represents the entire linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # The head of the list, initially None (empty list)

    # Method to insert a new node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # New node points to the current head
        self.head = new_node  # New node becomes the new head

    # Method to insert a new node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node  # New node becomes the head
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Last node now points to the new node

    # Method to delete a node with a specific value
    def delete_node(self, key):
        if self.head and self.head.data == key:  # If the head node is to be deleted
            self.head = self.head.next  # The second node becomes the new head
            return
        current = self.head
        while current.next:
            if current.next.data == key:  # If the next node is to be deleted
                current.next = current.next.next  # Skip the next node
                return
            current = current.next

    # Method to search for a specific value in the list
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:  # If the key is found
                return True
            current = current.next
        return False  # Key not found in the list

    # Method to display the entire linked list
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)  # Collect all elements
            current = current.next
        print(" -> ".join(map(str, elements)))  # Print elements joined by arrows


# Test code
if __name__ == "__main__":
    # Create a new linked list
    linked_list = SinglyLinkedList()

    # Insert elements at the end
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(4)
    print("Initial Linked List:")
    linked_list.display()

    # Insert element at the beginning
    linked_list.insert_at_beginning(0)
    print("After inserting 0 at the beginning:")
    linked_list.display()

    # Delete an element
    linked_list.delete_node(3)
    print("After deleting 3:")
    linked_list.display()

    # Search for elements
    print("Searching for 2:", linked_list.search(2))
    print("Searching for 5:", linked_list.search(5))
