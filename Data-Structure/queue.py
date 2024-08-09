# Queue: First-In-First-Out (FIFO) data structure
class Queue:
    # Initialize an empty queue
    def __init__(self):
        self.items = []

    # Check if queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # Add item to the end of the queue
    def enqueue(self, item):
        self.items.append(item)

    # Remove and return the first item
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    # Return the first item without removing
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    # Return the number of items in the queue
    def size(self):
        return len(self.items)

    # Display the queue
    def display(self):
        print("Queue:", self.items)


# Usage example
if __name__ == "__main__":
    queue = Queue()

    # Add items to the queue
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Initial Queue:")
    queue.display()

    print("Queue size:", queue.size())
    print("Front item:", queue.front())

    print("Dequeued item:", queue.dequeue())

    print("Queue after dequeue:")
    queue.display()

    print("Queue size after dequeue:", queue.size())
