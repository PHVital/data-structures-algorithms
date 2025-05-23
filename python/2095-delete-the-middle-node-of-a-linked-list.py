# LeetCode Problem 2095: Delete the Middle Node of a Linked List
# Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# Difficulty: Medium

# 🧠 Idea:
# - Usamos dois ponteiros: slow (1 passo) e fast (2 passos).
# - Quando o fast chega ao fim, o slow estará no meio da lista.
# - Usamos uma variável prev para guardar o nó anterior ao slow.
# - Para deletar o meio, fazemos prev.next = slow.next.

# 🕒 Time Complexity: O(n), percorremos a lista apenas uma vez.
# 🧠 Space Complexity: O(1), não usamos espaço adicional proporcional à entrada.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Caso especial: lista com 1 nó
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        # Encontrar o nó do meio
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Remover o nó do meio
        prev.next = slow.next

        return head
