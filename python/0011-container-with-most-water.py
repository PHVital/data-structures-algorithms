# 11. Container With Most Water
# Problema: Encontrar duas linhas que, juntas com o eixo x, formem um container com a maior quantidade de água possível.
# Abordagem: Two pointers. Começamos com dois ponteiros nas extremidades e movemos o ponteiro menor para dentro.
# Complexidade: Tempo O(n), Espaço O(1).

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        area = 0
        while i < j:
            area = max(area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area
