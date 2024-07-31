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
