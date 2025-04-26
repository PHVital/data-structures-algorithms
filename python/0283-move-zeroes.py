# Problem: 283. Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/
# Difficulty: Easy
# Tags: Two Pointers, Array
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
