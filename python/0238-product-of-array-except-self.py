# LeetCode Problem 238: Product of Array Except Self
# Link: https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium

# 🧠 Idea:
# - Use prefix and postfix products to avoid division.
# - Do two passes: left-to-right and right-to-left.
# - O(n) time, O(1) extra space (excluding output array).

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        answer = [1] * l
        postfix, prefix = 1, 1

        for x in range(l):
            answer[x] *= prefix
            prefix *= nums[x]

        for x in reversed(range(l)):
            answer[x] *= postfix
            postfix *= nums[x]

        return answer
