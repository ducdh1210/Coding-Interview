# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_count = {}
        # Count occurrences of each character
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Find the first non-repeating character
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index

        return -1


# Write tests based on the comments above
solution = Solution()

# Test case 1
s1 = "leetcode"
print("Test case 1:")
print("Input: s =", s1)
output = solution.firstUniqChar(s1)
print("Output:", output)
print("Expected: 0")
print()

# Test case 2
s2 = "loveleetcode"
print("Test case 2:")
print("Input: s =", s2)
output = solution.firstUniqChar(s2)
print("Output:", output)
print("Expected: 2")
print()

# Test case 3
s3 = "aabb"
print("Test case 3:")
print("Input: s =", s3)
output = solution.firstUniqChar(s3)
print("Output:", output)
print("Expected: -1")
print()
