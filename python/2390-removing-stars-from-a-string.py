'''
LeetCode Problem 2390: Removing Stars From a String

Link: https://leetcode.com/problems/removing-stars-from-a-string/

Approach:
Usamos uma pilha para simular o processo de remoção de caracteres. A cada caractere '*', removemos o último elemento inserido (comportamento de pilha - LIFO). Caso contrário, adicionamos o caractere à pilha. Ao final, juntamos os elementos da pilha para obter a string resultante.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)