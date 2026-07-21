"""
Problem: Leetcode 42 Trapping Rain Water

Intuition: We set a left and right pointer, and initialize maxL and maxR to be the heights at those pointers.
           We loop till the pointers meet. Each iteration we check if maxL is bigger than maxR. If it is, we decrement our
           right pointer, and update maxR based on the new pointer's height. Then we compute the amount of water trapped at r
           to be maxR - the height at r. If maxL is not bigger, we do the reverse on the left side. This area computation works because
           we only care about the smaller max since height is the bottleneck for area: whichever side has the smaller max is
           guaranteed to have its water level capped by that max regardless of what lies beyond the other pointer, since the
           other side's max is already known to be at least as large. That lets us finalize the water at that position without
           needing to know the rest of the array. We prevent negative values by updating the max as soon as we shift pointers.
           This way even if the previous max was smaller than the current height, it gets updated to the current height first,
           so the difference is 0.

Time Complexity: O(n) where n is the length of the height array, we iterate over each element in the array once

Space Complexity: O(1), no extra space is used

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]

        while l < r:

            if maxL > maxR:
                r -= 1
                maxR = max(maxR, height[r])
                area += maxR - height[r]
                
            else:
                l += 1
                maxL = max(maxL, height[l])
                area += maxL - height[l]
                
        return area
