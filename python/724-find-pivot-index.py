"""
Leetcode 724 - Find Pivot Index
https://leetcode.com/problems/find-pivot-index/

🟢 Easy
Tema: Prefix Sum

🧠 Estratégia:
- A soma total do array é fixa.
- Para cada índice i:
  - left_sum = soma dos elementos à esquerda de i.
  - O que falta à direita = total - left_sum - nums[i]
  - Se left_sum == right_sum, encontramos o índice pivô.

💡 Evitamos calcular a soma à direita diretamente para melhorar a eficiência.
"""

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == total - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1
