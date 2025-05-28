# LeetCode Problem 104: Maximum Depth of Binary Tree
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy

# 🧠 Idea:
# - A profundidade máxima de uma árvore binária é igual a:
#   1 + o máximo entre a profundidade da subárvore esquerda e da direita.
# - Se o nó for None (árvore vazia), retorna 0.

# 🕒 Time Complexity: O(n)
# - Visitamos cada nó exatamente uma vez.

# 🧠 Space Complexity: O(h)
# - Onde h é a altura da árvore (pior caso: árvore degenerada -> O(n), melhor caso: árvore balanceada -> O(log n)).

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)
