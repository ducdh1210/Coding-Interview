class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.items = []

    def is_empty(self):
        # Check if the stack is empty by seeing if the list has no items
        return len(self.items) == 0

    def push(self, item):
        # Add an item to the top of the stack (end of the list)
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            # Remove and return the top item from the stack (last item in the list)
            return self.items.pop()
        else:
            # If the stack is empty, raise an error
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            # Return the top item without removing it (last item in the list)
            return self.items[-1]
        else:
            # If the stack is empty, raise an error
            raise IndexError("Stack is empty")

    def size(self):
        # Return the number of items in the stack
        return len(self.items)

    def display(self):
        # Print the stack items from top to bottom
        print("Stack:", self.items)


if __name__ == "__main__":
    # Create a new stack
    stack = Stack()

    # Add items to the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Display the stack
    stack.display()

    # Print the current size of the stack
    print("Stack size:", stack.size())

    # Look at the top item without removing it
    print("Top item:", stack.peek())

    # Remove and print the top item
    print("Popped item:", stack.pop())

    # Print the new size after removing an item
    print("Stack size after pop:", stack.size())
