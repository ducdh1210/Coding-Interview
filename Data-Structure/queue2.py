from collections import deque


# Imagine a queue as a line of people waiting for a movie ticket
class Queue:
    def __init__(self):
        # We use a deque (double-ended queue) for efficient operations at both ends
        self.items = deque()  # This is our line of people

    def enqueue(self, item):
        # Adding a person to the back of the line
        self.items.append(item)

    def dequeue(self):
        # Serving the person at the front of the line (and they leave)
        if not self.is_empty():
            return (
                self.items.popleft()
            )  # popleft is efficient for removing from the front
        raise IndexError("Queue is empty")  # Can't serve anyone if the line is empty!

    def front(self):
        # Checking who's at the front of the line without serving them
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Queue is empty")  # Can't check the front if no one's in line

    def is_empty(self):
        # Checking if there's anyone in line
        return len(self.items) == 0

    def size(self):
        # Counting how many people are in line
        return len(self.items)

    def display(self):
        # Showing everyone in line (front to back)
        print(list(self.items))


# Test code
if __name__ == "__main__":
    queue = Queue()

    print("People joining the line:")
    for i in range(1, 6):
        queue.enqueue(i)
        print(f"Person {i} joined the line")
    print("Current line:")
    queue.display()

    print("\nServing the first person:")
    dequeued = queue.dequeue()
    print(f"Served and left: Person {dequeued}")
    print("Remaining line:")
    queue.display()

    print("\nWho's next in line?")
    front = queue.front()
    print(f"Next to be served: Person {front}")
    print("Line hasn't changed:")
    queue.display()

    print("\nHow many people are in line?", queue.size())
    print("Is the line empty?", queue.is_empty())

    print("\nServing everyone in line:")
    while not queue.is_empty():
        print(f"Served and left: Person {queue.dequeue()}")

    print("\nIs the line empty now?", queue.is_empty())

    print("\nTrying to serve someone when the line is empty:")
    try:
        queue.dequeue()
    except IndexError as e:
        print("Error:", str(e))
