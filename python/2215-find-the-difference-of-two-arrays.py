# LeetCode Problem 2215: Find the Difference of Two Arrays
# Link: https://leetcode.com/problems/find-the-difference-of-two-arrays/
# Difficulty: Easy

# 🧠 Idea:
# - Use conjuntos (set) para remover duplicatas e permitir operações de diferença.
# - Faça a diferença de nums1 - nums2 e vice-versa.
# - Retorne o resultado como uma lista de listas.

# 🕒 Time Complexity: O(n + m), onde n = len(nums1), m = len(nums2)
# 🧠 Space Complexity: O(n + m)

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
