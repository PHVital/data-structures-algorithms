# LeetCode Problem 2352: Equal Row and Column Pairs
# Link: https://leetcode.com/problems/equal-row-and-column-pairs/
# Difficulty: Medium

# 🧠 Idea:
# - Use zip(*grid) para obter as colunas como tuplas.
# - Use Counter para contar as linhas e colunas.
# - Para cada linha, verifique quantas vezes ela aparece como coluna.

# 🕒 Time Complexity: O(n^2)
# 🧠 Space Complexity: O(n^2)

from collections import Counter
from typing import List

# Com zip

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = Counter(tuple(row) for row in grid)
        col_counts = Counter(tuple(col) for col in zip(*grid))

        count = 0
        for row in row_counts:
            count += row_counts[row] * col_counts.get(row, 0)
        return count

# Sem zip

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns = []
        rows = []
        count = 0
        i = 0
        while i < len(grid):
            column = [column[i] for column in grid]
            columns.append(column)
            i += 1
        for row in grid:
            rows.append(row)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if columns[i] == rows[j]:
                    count += 1
        return count