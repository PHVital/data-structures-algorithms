"""
LeetCode Problem 1004: Max Consecutive Ones III
Difficulty: Medium
Topic: Sliding Window
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, max_window, count_zeros, count_ones = 0, 0, 0, 0
        for j in range(len(nums)):
            if nums[j] == 0:
                count_zeros += 1
            while count_zeros > k:
                if nums[i] == 0:
                    count_zeros -= 1
                i += 1
            count_ones = max(count_ones, j - i + 1)
        return count_ones
