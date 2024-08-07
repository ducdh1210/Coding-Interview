# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - k % len(nums)
        print(i)
        if i == 0:
            return nums

        to_move_region = nums[:i]
        # Remove the elements from the beginning, after this, nums --> nums[index_new_first_part:]
        nums[:i] = []
        # Append the stored elements
        nums.extend(to_move_region)
        return nums


# Write tests
# Test cases
solution = Solution()

# Test case 1
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
print("Test case 1:")
print("Input: nums =", nums1, "k =", k1)
output = solution.rotate(nums1, k1)
print("Output:", output)
print("Expected: [5, 6, 7, 1, 2, 3, 4]")
print()

# Test case 2
nums2 = [-1, -100, 3, 99]
k2 = 2
print("Test case 2:")
print("Input: nums =", nums2, "k =", k2)
output = solution.rotate(nums2, k2)
print("Output:", output)
print("Expected: [3, 99, -1, -100]")
print()

# Additional test case
nums3 = [1, 2]
k3 = 3
print("Test case 3:")
print("Input: nums =", nums3, "k =", k3)
output = solution.rotate(nums3, k3)
print("Output:", nums3)
print("Expected: [2, 1]")
