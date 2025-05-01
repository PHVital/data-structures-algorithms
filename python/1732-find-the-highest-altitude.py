"""
Leetcode 1732 - Find the Highest Altitude
https://leetcode.com/problems/find-the-highest-altitude/

🟢 Easy
Tema: Prefix Sum

🧠 Estratégia:
- Começamos com altitude 0.
- Para cada ganho no percurso, somamos ao valor atual da altitude.
- Mantemos o maior valor de altitude alcançado.
"""

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_altitude = 0
        for g in gain:
            altitude += g
            max_altitude = max(max_altitude, altitude)
        return max_altitude
