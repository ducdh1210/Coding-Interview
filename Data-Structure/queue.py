# Imagine a queue as a line of people waiting for a rollercoaster ride
class Queue:
    def __init__(self):
        # Our queue is like an empty line at the start of the day
        self.items = []  # This list represents the line of people

    def is_empty(self):
        # Checking if there's anyone in line
        return len(self.items) == 0  # If the length is 0, the line is empty

    def enqueue(self, item):
        # A new person joins the back of the line
        self.items.append(item)  # Adding to the end of the list

    def dequeue(self):
        # The person at the front gets on the ride and leaves the line
        if not self.is_empty():
            return self.items.pop(0)  # Remove and return the first person in line
        else:
            # If we try to dequeue from an empty line, we raise an error
            raise IndexError(
                "Queue is empty"
            )  # Can't remove someone from an empty line!

    def front(self):
        # Checking who's at the front of the line without letting them on the ride
        if not self.is_empty():
            return self.items[0]  # Return the first person without removing them
        else:
            # If the line is empty, we can't check who's first
            raise IndexError(
                "Queue is empty"
            )  # Can't check the front of an empty line!

    def size(self):
        # Counting how many people are in line
        return len(self.items)  # The length of our list is the number of people in line

    def display(self):
        # Displaying the entire queue (front to back)
        print("Queue:", self.items)


# Usage example
if __name__ == "__main__":
    # Let's simulate a day at the rollercoaster
    queue = Queue()  # Create a new line for the rollercoaster

    # People start joining the line
    queue.enqueue(1)  # Person 1 joins the line
    queue.enqueue(2)  # Person 2 joins the line
    queue.enqueue(3)  # Person 3 joins the line

    print("Initial Queue:")
    queue.display()

    print("Queue size:", queue.size())  # How many people are in line now?
    print("Front item:", queue.front())  # Who's first in line?

    # The ride starts, and the first person gets on
    print(
        "Dequeued item:", queue.dequeue()
    )  # The first person leaves the line to get on the ride

    print("Queue after dequeue:")
    queue.display()

    print(
        "Queue size after dequeue:", queue.size()
    )  # How many people are left in line?
