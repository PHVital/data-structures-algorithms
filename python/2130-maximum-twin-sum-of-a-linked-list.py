# LeetCode Problem 2130: Maximum Twin Sum of a Linked List
# Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Difficulty: Medium

# 🧠 Idea:
# - O problema pede o maior "twin sum", que é a soma de nós equidistantes dos extremos da lista.
# - Podemos resolver com:
#   1. Dois ponteiros (slow/fast) para encontrar o meio da lista.
#   2. Reverter a segunda metade da lista.
#   3. Percorrer a primeira metade e a reversa da segunda ao mesmo tempo somando os pares.
# - Isso evita o uso de memória adicional, tornando o algoritmo mais eficiente.

# 🕒 Time Complexity: O(n)
# - Cada passo percorre no máximo uma vez a lista.

# 🧠 Space Complexity: O(1)
# - A reversão é feita in-place, sem estruturas auxiliares.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. Encontrar o meio da lista com slow/fast
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverter a segunda metade da lista
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # 3. Calcular o maior twin sum
        max_sum = 0
        first, second = head, prev
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum
