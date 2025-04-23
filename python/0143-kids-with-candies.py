# LeetCode Problem 143: Kids With the Greatest Number of Candies
# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Difficulty: Easy

# 🧠 Idea:
# - Encontre a maior quantidade de doces entre as crianças.
# - Para cada criança, verifique se ela pode alcançar ou ultrapassar esse valor ao ganhar os "extraCandies".

# 🕒 Time Complexity: O(n)
# 🧠 Space Complexity: O(n)

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]
