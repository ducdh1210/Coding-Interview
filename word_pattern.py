# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()
        mapper = {}
        if len(s) != len(pattern):
            return False
        for s, p in zip(s, pattern):
            if p in mapper:
                if mapper[p] != s:
                    return False
            else:
                mapper[p] = s
        return True

a = Solution()
print(a.wordPattern("abba", "dog cat cat dog"))
print(a.wordPattern("abba", "dog cat cat fish"))
print(a.wordPattern("aaaa", "dog cat cat dog"))
