# LEETCODE Q.1) Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum_optimized(self, nums: list[int], target: int) -> list[int]:
        numToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []


solution = Solution()

# Test case 1
nums1 = [2, 7, 11, 15]
target1 = 9
print("Test case 1:")
print("Input: nums =", nums1, "target =", target1)
output = solution.twoSum_optimized(nums1, target1)
print("Output:", output)
print("Expected: [0, 1]")
print()

# Test case 2
nums2 = [3, 2, 4]
target2 = 6
print("Test case 2:")
print("Input: nums =", nums2, "target =", target2)
output = solution.twoSum_optimized(nums2, target2)
print("Output:", output)
print("Expected: [1, 2]")
print()

# Test case 3
nums3 = [3, 3]
target3 = 6
print("Test case 3:")
print("Input: nums =", nums3, "target =", target3)
output = solution.twoSum_optimized(nums3, target3)
print("Output:", output)
print("Expected: [0, 1]")
print()
