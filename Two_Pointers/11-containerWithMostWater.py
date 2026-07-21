"""
Problem: Leetcode 11 Container with Most Water

Intuition: First we set our left and right pointers. Then we loop until the pointers meet.
           To compute the current area we take the minimum of the heights at l and r, and multiply it by the distance between the pointers (r - l).
           We update res to be the max of itself and curr. Then we shift the pointer at the shorter side, since the shorter side limits the area,
           any other container using it would be narrower and no taller, so nothing better is lost by discarding it.
Time Complexity: O(n) where n is the length of the array. We iterate over every value once.

Space Complexity: O(1) there is no extra space used 

"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            res = max(res, curr)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res