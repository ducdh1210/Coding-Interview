# LEETCODE Q.48: Rotate Image
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:
# Input: matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# Output: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

import numpy as np


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        new_matrix, old_matrix = np.matrix(matrix), np.matrix(matrix)
        for row_index in range(len(old_matrix)):
            v = np.array(old_matrix[:, row_index].reshape(-1))
            v = v[0][::-1]
            new_matrix[row_index, :] = v
        return new_matrix

    def rotate_2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # reverse
        l = 0
        r = len(matrix) - 1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        # transpose
        print(matrix)
        print("-----------------")
        for i in range(len(matrix)):
            print("======================>")
            print("i:", i)
            for j in range(i):
                print("*****************")
                print("j:", j)
                print("matrix[i][j]:", matrix[i][j])
                print("matrix[j][i]:", matrix[j][i])
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().rotate_2(matrix))

# matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# print(Solution().rotate_2(matrix))
