# LeetCode Problem 151: Reverse Words in a String
# Link: https://leetcode.com/problems/reverse-words-in-a-string/
# Difficulty: Medium

# 🧠 Idea:
# - Use split() para remover espaços extras e separar as palavras.
# - Inverta a lista de palavras com slicing e use join para montar a string final.

# 🕒 Time Complexity: O(n)
# 🧠 Space Complexity: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])
