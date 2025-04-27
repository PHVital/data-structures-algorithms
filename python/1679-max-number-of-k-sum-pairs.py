# 1679. Max Number of K-Sum Pairs
# Problema: Encontrar o número máximo de pares únicos em um array que somam exatamente k.
# Abordagens:
# - (1) Two pointers: ordenar o array e usar dois ponteiros.
# - (2) Hashmap: contar frequências e buscar complementares.
# Complexidade:
# - (1) Tempo O(n log n), Espaço O(1)
# - (2) Tempo O(n), Espaço O(n)

# Implementação 1: Two Pointers
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i, j = 0, len(nums) - 1
        count = 0
        nums.sort()
        while i < j:
            total = nums[i] + nums[j]
            if total == k:
                count += 1
                i += 1
                j -= 1
            elif total < k:
                i += 1
            else:
                j -= 1
        return count

# Implementação 2: Hashmap
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import Counter
        count = Counter(nums)
        operations = 0
        for num in count:
            complement = k - num
            if complement in count:
                if num == complement:
                    operations += count[num] // 2
                else:
                    operations += min(count[num], count[complement])
        return operations // 2
