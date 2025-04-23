# LeetCode Problem 1071: Greatest Common Divisor of Strings
# Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Difficulty: Easy

# 🧠 Idea:
# - Um divisor comum de strings precisa se repetir para formar ambas as strings.
# - Verifique, do maior possível até o menor, se há uma substring que pode gerar ambas.
# - Versão alternativa: usar gcd matemático dos tamanhos.

# 🕒 Time Complexity: O(n * k), onde n é o comprimento da menor string e k é o custo de validação.
# 🧠 Space Complexity: O(1)

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def valid(k):
            if len(str1) % k != 0 or len(str2) % k != 0:
                return False
            base = str1[:k]
            return str1 == base * (len(str1) // k) and str2 == base * (len(str2) // k)

        for i in range(min(len(str1), len(str2)), 0, -1):
            if valid(i):
                return str1[:i]
        return ""
