"""
LeetCode Problem 1456 - Maximum Number of Vowels in a Substring of Given Length (Easy)

Given a string s and an integer k, return the maximum number of vowel letters 
in any substring of s with length k.

Approach: Sliding Window
We initialize the count of vowels in the first window of size k, 
and as we move the window, we update the count by subtracting the character 
going out and adding the character coming in, if they are vowels.
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_vowels = count
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            max_vowels = max(max_vowels, count)
        return max_vowels
