# LEETCODE Q.54) Given an m x n matrix, return all elements of the matrix in spiral order.

# Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

# Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # Calculate the total number of rows and columns
        rows, cols = len(matrix), len(matrix[0])

        # Set up pointers to traverse the matrix
        row, col = 0, -1

        # Set the initial direction to 1 for moving left to right
        direction = 1

        # Create an array to store the elements in spiral order
        result = []

        # Traverse the matrix in a spiral order
        while rows > 0 and cols > 0:
            # Move horizontally in one of two directions:
            #   1. Left to right (if direction == 1)
            #   2. Right to left (if direction == -1)
            # Increment the col pointer to move horizontally
            for _ in range(cols):
                col += direction
                result.append(matrix[row][col])
            rows -= 1

            # Move vertically in one of two directions:
            #   1. Top to bottom (if direction == 1)
            #   2. Bottom to top (if direction == -1)
            # Increment the row pointer to move vertically
            for _ in range(rows):
                row += direction
                result.append(matrix[row][col])
            cols -= 1

            # Flip the direction for the next traversal
            direction *= -1

        return result


# Test cases
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print("Test case 1:")
print("Input: matrix =", matrix1)
output1 = Solution().spiralOrder(matrix1)
print("Output:", output1)
print("Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]")
print()

print("Test case 2:")
print("Input: matrix =", matrix2)
output2 = Solution().spiralOrder(matrix2)
print("Output:", output2)
print("Expected: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]")
print()
