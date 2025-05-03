# LeetCode Problem 1207: Unique Number of Occurrences
# Link: https://leetcode.com/problems/unique-number-of-occurrences/
# Difficulty: Easy

# 🧠 Idea:
# - Conte a frequência de cada número usando Counter.
# - Coloque todas as contagens em uma lista.
# - Verifique se todas as contagens são únicas usando um set.

# 🕒 Time Complexity: O(n)
# 🧠 Space Complexity: O(n)

from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        return len(freq.values()) == len(set(freq.values()))
