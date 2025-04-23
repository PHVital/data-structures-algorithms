# LeetCode Problem 605: Can Place Flowers
# Link: https://leetcode.com/problems/can-place-flowers/
# Difficulty: Easy

# 🧠 Idea:
# - Percorra cada canteiro e verifique se ele está vazio e os dois vizinhos também (ou se é borda).
# - Se sim, plante uma flor e incremente o contador.
# - Retorne True se conseguiu plantar pelo menos n flores.

# 🕒 Time Complexity: O(n)
# 🧠 Space Complexity: O(1)

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1
        return count >= n
