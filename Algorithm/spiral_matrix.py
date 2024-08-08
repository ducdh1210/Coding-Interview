# LEETCODE Q.54) Given an m x n matrix, return all elements of the matrix in spiral order.

# Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

# Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

from typing import Literal


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []  # Initialize an empty list to store the spiral order elements

        rows, cols = len(matrix), len(matrix[0])  # Get the number of rows and columns
        row_idx, col_idx = 0, -1  # Start indices for the current position in the matrix
        direction: Literal[-1, 1] = (
            1  # Direction indicator (1 for right/down, -1 for left/up)
        )

        while (cols > 0) and (
            rows > 0
        ):  # Continue until there are no rows or columns left
            # Traverse the current row from left to right at first, direction controlled by direction variable
            for _ in range(cols):
                col_idx += direction  # Move to the next column
                value = matrix[row_idx][col_idx]  # Get the current value
                print(f"Row Index: {row_idx}, Column Index: {col_idx}, Value: {value}")
                result.append(value)  # Append the value to the result list
            rows -= 1  # Decrease the number of rows left to process

            # Traverse the current column from top to bottom at first, direction controlled by direction variable
            for _ in range(rows):
                row_idx += direction  # Move to the next row
                value = matrix[row_idx][col_idx]  # Get the current value
                print(f"Row Index: {row_idx}, Column Index: {col_idx}, Value: {value}")
                result.append(value)  # Append the value to the result list
            cols -= 1  # Decrease the number of columns left to process

            direction *= -1  # Change direction for the next traversal

        return result  # Return the final spiral order list


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
