"""
334. Increasing Triplet Subsequence (Medium)

Dado um array de inteiros, retorna True se existir uma subsequência crescente de tamanho 3.
Ou seja, existem índices i < j < k tais que nums[i] < nums[j] < nums[k].

Exemplo:
Input: [1,2,3,4,5]
Output: True

Input: [5,4,3,2,1]
Output: False

Complexidade:
- Tempo: O(n)
- Espaço: O(1)
"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                return True

        return False
