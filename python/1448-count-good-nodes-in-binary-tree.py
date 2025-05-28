# LeetCode Problem 1448: Count Good Nodes in Binary Tree
# Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Difficulty: Medium

# 🧠 Idea:
# - Um nó é considerado "bom" se não houver nenhum valor maior no caminho da raiz até ele.
# - Durante a DFS, passamos o maior valor encontrado até o nó atual.
# - Se o valor do nó atual for maior ou igual a esse maior valor, ele é "bom".
# - Atualizamos o maior valor ao seguir recursivamente para os filhos.

# 🕒 Time Complexity: O(n)
# - Visitamos todos os n nós da árvore exatamente uma vez.

# 🧠 Space Complexity: O(h)
# - h é a altura da árvore, usada pela pilha de chamadas recursivas.
# - No pior caso (árvore degenerada), h = n; no melhor (árvore balanceada), h = log(n).

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node: Optional[TreeNode], max_val: int) -> int:
        if not node:
            return 0
        total_good = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)
        left_good = self.dfs(node.left, max_val)
        right_good = self.dfs(node.right, max_val)
        return total_good + left_good + right_good

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root, root.val)
