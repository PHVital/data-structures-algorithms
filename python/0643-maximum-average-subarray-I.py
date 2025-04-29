"""
LeetCode Problem 643 - Maximum Average Subarray I (Easy)

Given an integer array nums of length n and an integer k, return the maximum average 
of any subarray of length k.

Approach: Sliding Window
We first calculate the sum of the first k elements, then move the window one element at a time, 
subtracting the element that is leaving the window and adding the element that is entering.
We track the maximum sum and calculate the average as we go.
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_avarage = sum(nums[:k])
        max_avarage = window_avarage / k
        for i in range(k, len(nums)):
            window_avarage += nums[i] - nums[i - k]
            max_avarage = max(max_avarage, window_avarage / k)
        return max_avarage
