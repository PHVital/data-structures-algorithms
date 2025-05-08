# LeetCode Problem 1657: Determine if Two Strings Are Close
# Link: https://leetcode.com/problems/determine-if-two-strings-are-close/
# Difficulty: Medium

# 🧠 Idea:
# - Podemos reordenar livremente as letras, então a ordem não importa.
# - Podemos trocar todas as ocorrências de uma letra A por B (desde que ambas existam).
# - Então, para serem "close":
#   1. Ambas devem conter o MESMO CONJUNTO de letras.
#   2. As FREQUÊNCIAS devem ser permutáveis (mesmos valores, em qualquer ordem).

# 🕒 Time Complexity: O(n)
# 🧠 Space Complexity: O(n) — usamos dicionários para contar as frequências.

from collections import Counter
from typing import List

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        return sorted(freq1.values()) == sorted(freq2.values())
