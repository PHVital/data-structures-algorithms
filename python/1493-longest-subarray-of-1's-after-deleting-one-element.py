"""
LeetCode Problem 1493: Longest Subarray of 1's After Deleting One Element
Difficulty: Medium
Topic: Sliding Window
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i , count_zeros, max_ones = 0, 0, 0
        for j in range(0, len(nums)):
            if nums[j] == 0:
                count_zeros += 1
            while count_zeros > 1:
                if nums[i] == 0:
                    count_zeros -= 1
                i += 1
            max_ones = max(max_ones, j - i)
        return max_ones
