# LeetCode Problem 206: Reverse Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy

# 🧠 Idea:
# - Usamos dois ponteiros: `prev` e `curr`.
# - A cada passo, salvamos o próximo nó (`next_temp`), apontamos `curr.next` para `prev`, 
#   e avançamos os dois ponteiros.
# - No final, `prev` será o novo head da lista invertida.

# 🕒 Time Complexity: O(n)
# - Precisamos percorrer toda a lista uma vez.

# 🧠 Space Complexity: O(1)
# - A reversão é feita in-place, sem usar memória extra proporcional ao input.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_temp = curr.next  # salvar o próximo nó original
            curr.next = prev       # inverter o ponteiro
            prev = curr            # avançar o ponteiro prev
            curr = next_temp       # avançar o ponteiro curr

        return prev  # novo head da lista
