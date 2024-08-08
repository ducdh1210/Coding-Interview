# iterator_vs_generator.py

# SquareIterator: This is a class-based iterator that generates squares of numbers up to a specified max_value.
# The iterator must implement the __iter__() and __next__() methods.
class SquareIterator:
    def __init__(self, max_value):
        self.max_value = max_value  # Initialize the maximum value
        self.current = 1  # Start from 1

    def __iter__(self):
        # __iter__() returns the iterator object itself. This is required to make the object iterable.
        return self

    def __next__(self):
        # __next__() returns the next value in the iteration. It must raise a StopIteration exception
        # when the iteration is complete.
        if self.current <= self.max_value:
            result = self.current * self.current  # Calculate the square
            self.current += 1  # Move to the next number
            return result
        else:
            raise StopIteration  # Signal that the iteration is complete


# square_generator: This is a function-based generator that also generates squares of numbers up to a specified max_value.
# The generator uses the yield statement to return values one by one, pausing and resuming automatically.
def square_generator(max_value):
    current = 1  # Start from 1
    while current <= max_value:
        # yield is a keyword that turns this function into a generator. It allows the function to return
        # a value and pause its execution, resuming from where it left off the next time it's called.
        yield current * current
        current += 1  # Move to the next number


if __name__ == "__main__":
    # Test the SquareIterator
    print("SquareIterator results:")
    squares_iter = SquareIterator(5)
    # The for loop automatically calls __iter__() to get the iterator object and then __next__() to get each value.
    for square in squares_iter:
        print(square)

    print("\nSquareGenerator results:")
    # Test the square_generator
    # The for loop automatically calls the generator function and iterates over the yielded values.
    for square in square_generator(5):
        print(square)

# Explanation:
# - Iterator: An object that implements the __iter__() and __next__() methods. It maintains its own state and
#   produces the next value each time __next__() is called. The iteration stops when StopIteration is raised.
# - Generator: A simpler way to create iterators. A generator function uses the yield keyword to produce values
#   one by one, maintaining state automatically and pausing execution between each value.
# - yield: A keyword used in generator functions to return a value and pause the function's execution. The function
#   can be resumed later to continue generating values.
