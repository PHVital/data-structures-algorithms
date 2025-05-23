# LeetCode Problem 328: Odd Even Linked List
# Link: https://leetcode.com/problems/odd-even-linked-list/
# Difficulty: Medium

# 🧠 Idea:
# - Reorganizar os nós da lista para que todos os nós em posições ímpares (1º, 3º, 5º...) venham antes dos pares (2º, 4º, 6º...).
# - Utilizamos dois ponteiros:
#     - odd: aponta para o último nó ímpar
#     - even: aponta para o último nó par
#     - even_head: armazena o início da sublista par (para conectar no final)
# - Avançamos alternadamente os ponteiros odd e even até o final da lista.
# - No fim, conectamos o último nó ímpar com o início da sublista par.

# 🕒 Time Complexity: O(n)
# - Percorremos a lista uma única vez.

# 🧠 Space Complexity: O(1)
# - Usamos apenas ponteiros auxiliares.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # Lista com 0 ou 1 elemento já está ordenada

        odd = head
        even = head.next
        even_head = even  # Guardar o início da lista de pares

        while even and even.next:
            odd.next = even.next  # Próximo ímpar
            odd = odd.next
            even.next = odd.next  # Próximo par
            even = even.next

        # Conectar o fim da lista ímpar com o início da par
        odd.next = even_head

        return head
