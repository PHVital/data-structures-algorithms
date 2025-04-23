# LeetCode Problem 1768: Merge Strings Alternately
# Link: https://leetcode.com/problems/merge-strings-alternately/
# Difficulty: Easy

# 🧠 Idea:
# - Use dois ponteiros para intercalar as letras de word1 e word2.
# - Quando uma das palavras terminar, continue com a outra.

# 🕒 Time Complexity: O(n + m)
# 🧠 Space Complexity: O(n + m)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        result = ''
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result += word1[i]
                i += 1
            if j < len(word2):
                result += word2[j]
                j += 1
        return result
