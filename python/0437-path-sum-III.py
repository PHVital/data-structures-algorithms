# LeetCode Problem 437: Path Sum III
# Link: https://leetcode.com/problems/path-sum-iii/
# Difficulty: Medium

# ✅ Approach 1: Brute Force with DFS from each node
# 🧠 Idea:
# - Para cada nó, fazemos uma DFS tentando achar todos os caminhos a partir dele que somam targetSum.
# - Fazemos isso recursivamente para cada subárvore.

# 🕒 Time Complexity: O(n^2) no pior caso (em árvores não balanceadas)
# 🧠 Space Complexity: O(h) para profundidade da recursão

class Solution:
    def dfs(self, node, curr_sum, target):
        if not node:
            return 0

        curr_sum += node.val
        count = 1 if curr_sum == target else 0

        count += self.dfs(node.left, curr_sum, target)
        count += self.dfs(node.right, curr_sum, target)

        return count

    def pathSum(self, root, targetSum):
        if not root:
            return 0

        return (self.dfs(root, 0, targetSum)
                + self.pathSum(root.left, targetSum)
                + self.pathSum(root.right, targetSum))


# ✅ Approach 2: Optimized DFS with Prefix Sum (using HashMap)
# 🧠 Idea:
# - Usamos um dicionário para armazenar a soma acumulada até cada ponto do caminho.
# - Se em algum ponto curr_sum - targetSum já foi visto, existe um caminho com soma targetSum.
# - Backtrack é usado para desfazer o estado ao voltar da recursão.

# 🕒 Time Complexity: O(n)
# 🧠 Space Complexity: O(n) com dicionário e stack

class Solution:
    def pathSum(self, root, targetSum):
        def dfs(node, curr_sum, prefix_sums):
            if not node:
                return 0

            curr_sum += node.val
            count = prefix_sums.get(curr_sum - targetSum, 0)

            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1

            count += dfs(node.left, curr_sum, prefix_sums)
            count += dfs(node.right, curr_sum, prefix_sums)

            prefix_sums[curr_sum] -= 1  # backtrack
            return count

        prefix_sums = {0: 1}  # soma nula já "existe"
        return dfs(root, 0, prefix_sums)
