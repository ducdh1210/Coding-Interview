# Queue: First-In-First-Out (FIFO) data structure
class Queue:
    def __init__(self):
        self.items = []  # Initialize an empty queue

    def is_empty(self):
        return len(self.items) == 0  # Check if queue is empty

    def enqueue(self, item):
        self.items.append(item)  # Add item to the end of the queue

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove and return the first item
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]  # Return the first item without removing
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)  # Return the number of items in the queue

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
