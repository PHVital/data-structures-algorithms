from typing import List

# 735. Asteroid Collision
# ------------------------
# Problem:
# Given a list of integers representing asteroids in a row, for each asteroid,
# the absolute value represents its size, and the sign represents its direction
# (positive = right, negative = left). Colliding asteroids will follow these rules:
# - Two asteroids moving in the same direction will never meet.
# - Two asteroids moving toward each other will collide, and the smaller one explodes.
# - If they are the same size, both explode.
# Return the state of the asteroids after all collisions.

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                # Collision occurs
                if stack[-1] < -asteroid:
                    stack.pop()  # Top of the stack explodes
                    continue     # Check again with the new top
                elif stack[-1] == -asteroid:
                    stack.pop()  # Both explode
                break            # Current asteroid explodes or both did
            else:
                # No collision or current asteroid survived
                stack.append(asteroid)
        return stack
