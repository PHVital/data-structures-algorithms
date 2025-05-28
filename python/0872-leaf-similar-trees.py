# LeetCode Problem 872: Leaf-Similar Trees
# Link: https://leetcode.com/problems/leaf-similar-trees/
# Difficulty: Easy

# 🧠 Idea:
# - Percorremos as duas árvores em DFS para coletar os valores das folhas (nós sem filhos).
# - Comparamos as duas listas resultantes: se forem iguais, as árvores são leaf-similar.

# 🕒 Time Complexity: O(n + m)
# - Onde n e m são os números de nós nas árvores root1 e root2.
# - Visitamos todos os nós uma vez para coletar as folhas.

# 🧠 Space Complexity: O(h1 + h2 + l)
# - h1 e h2 são as alturas das duas árvores (recursão).
# - l é o número total de folhas (armazenadas nas listas).

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, leaves):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
            dfs(node.left, leaves)
            dfs(node.right, leaves)

        leaves1 = []
        leaves2 = []
        dfs(root1, leaves1)
        dfs(root2, leaves2)

        return leaves1 == leaves2
