class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.items = []

    def push(self, item):
        # Add an item to the top of the stack (end of the list)
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            # Remove and return the top item from the stack (last item in the list)
            return self.items.pop()
        # If the stack is empty, raise an error
        raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            # Return the top item without removing it (last item in the list)
            return self.items[-1]
        # If the stack is empty, raise an error
        raise IndexError("Stack is empty")

    def is_empty(self):
        # Check if the stack is empty by seeing if the list has no items
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the stack
        return len(self.items)

    def display(self):
        # Print the entire stack (useful for debugging)
        print(self.items)


# Test code
if __name__ == "__main__":
    # Create a new stack
    stack = Stack()

    print("Pushing elements onto the stack:")
    # Add numbers 1 to 5 to the stack
    for i in range(1, 6):
        stack.push(i)
        print(f"Pushed {i}")
    stack.display()

    print("\nPop an element:")
    # Remove and print the top element
    popped = stack.pop()
    print(f"Popped: {popped}")
    stack.display()

    print("\nPeek at the top element:")
    # Look at the top element without removing it
    top = stack.peek()
    print(f"Top element: {top}")
    stack.display()

    # Print the current size of the stack
    print("\nStack size:", stack.size())
    # Check if the stack is empty
    print("Is stack empty?", stack.is_empty())

    print("\nPop all elements:")
    # Remove and print all remaining elements
    while not stack.is_empty():
        print(f"Popped: {stack.pop()}")

    # Check if the stack is empty after popping all elements
    print("\nIs stack empty now?", stack.is_empty())

    # Try to pop from an empty stack to demonstrate error handling
    try:
        stack.pop()
    except IndexError as e:
        print("\nError:", str(e))
