# Node class represents each element in the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.prev = None  # Link to the previous node (like holding hands with the person in front)
        self.next = (
            None  # Link to the next node (like holding hands with the person behind)
        )


# DoublyLinkedList class represents the entire list
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # The first person in the line
        self.tail = None  # The last person in the line

    # Adding a new person to the front of the line
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:  # If the line is empty
            self.head = self.tail = new_node  # The new person is both first and last
        else:
            new_node.next = (
                self.head
            )  # New person holds hands with the current first person
            self.head.prev = (
                new_node  # Current first person holds hands with the new person
            )
            self.head = new_node  # New person becomes the first in line

    # Adding a new person to the end of the line
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If the line is empty
            self.head = self.tail = new_node  # The new person is both first and last
        else:
            self.tail.next = new_node  # Last person holds hands with the new person
            new_node.prev = self.tail  # New person holds hands with the last person
            self.tail = new_node  # New person becomes the last in line

    # Removing a person from the line
    def delete_node(self, key):
        current = self.head
        while current:
            if current.data == key:  # Found the person to remove
                if current.prev:  # If there's someone in front
                    current.prev.next = (
                        current.next
                    )  # Person in front holds hands with person behind
                else:
                    self.head = (
                        current.next
                    )  # If removing the first person, second becomes first
                if current.next:  # If there's someone behind
                    current.next.prev = (
                        current.prev
                    )  # Person behind holds hands with person in front
                else:
                    self.tail = (
                        current.prev
                    )  # If removing the last person, second-to-last becomes last
                return
            current = current.next  # Move to the next person in line

    # Looking for a specific person in the line
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:  # Found the person
                return True
            current = current.next  # Move to the next person
        return False  # Person not in the line

    # Displaying the line from front to back
    def display_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)  # Collect each person's number
            current = current.next
        print(
            " <-> ".join(map(str, elements))
        )  # Show the line with people holding hands

    # Displaying the line from back to front
    def display_backward(self):
        elements = []
        current = self.tail
        while current:
            elements.append(
                current.data
            )  # Collect each person's number, starting from the back
            current = current.prev
        print(
            " <-> ".join(map(str, elements))
        )  # Show the line with people holding hands


# Test code
if __name__ == "__main__":
    dll = DoublyLinkedList()
    # Adding people to the line
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_end(4)
    print("Initial Doubly Linked List (forward):")
    dll.display_forward()

    # Adding a new person to the front
    dll.insert_at_beginning(0)
    print("After inserting 0 at the beginning (forward):")
    dll.display_forward()

    # Removing a person from the middle
    dll.delete_node(3)
    print("After deleting 3 (forward):")
    dll.display_forward()

    # Showing the line from back to front
    print("Doubly Linked List (backward):")
    dll.display_backward()

    # Looking for specific people
    print("Searching for 2:", dll.search(2))
    print("Searching for 5:", dll.search(5))
