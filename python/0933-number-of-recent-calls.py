# LeetCode Problem 933: Number of Recent Calls
# Link: https://leetcode.com/problems/number-of-recent-calls/
# Difficulty: Easy

# 🧠 Idea:
# - Usamos uma fila (deque) para armazenar os tempos de chamadas.
# - Quando uma nova chamada `ping(t)` ocorre, adicionamos `t` na fila.
# - Removemos da frente da fila todas as chamadas com tempo < t - 3000 (fora da janela de 3000ms).
# - O número de elementos restantes na fila representa quantas chamadas ocorreram nos últimos 3000ms.

# 🕒 Time Complexity: O(1) amortizado por operação
# 🧠 Space Complexity: O(n), onde n é o número de pings nos últimos 3000ms

from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)
