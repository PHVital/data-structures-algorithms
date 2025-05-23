# LeetCode Problem 649: Dota2 Senate
# Link: https://leetcode.com/problems/dota2-senate/
# Difficulty: Medium

# 🧠 Idea:
# - Usamos duas filas para armazenar os índices dos senadores de cada partido.
# - Em cada rodada, comparamos os primeiros senadores de cada fila.
#   Quem estiver mais à frente age primeiro e bane o outro.
# - O vencedor volta ao final da fila com índice aumentado de +n (simulando fila circular).
# - O processo continua até que uma das filas fique vazia.

# 🕒 Time Complexity: O(n²) no pior caso (muitas interações entre partidos).
# 🧠 Space Complexity: O(n), para armazenar os índices dos senadores.

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        # Separar os índices dos senadores por partido
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # Simular a votação em rodadas
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()

            # Quem tiver o índice menor age primeiro
            if r_idx < d_idx:
                radiant.append(r_idx + n)
            else:
                dire.append(d_idx + n)

        return "Radiant" if radiant else "Dire"
