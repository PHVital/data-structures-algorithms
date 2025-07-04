# Problem: 392. Is Subsequence
# Link: https://leetcode.com/problems/is-subsequence/
# Difficulty: Easy
# Tags: Two Pointers, String
# Time Complexity: O(n + m)
# Space Complexity: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
