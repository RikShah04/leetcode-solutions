"""
Problem: Leetcode 15 3Sum

Intuition: First we sort the list of numbers, then we iterate over the list.
           As soon as we find a value greater than 0 we exit the loop, since no new solutions can be made with a >0 value as the lowest.
           If the current value is the same as the one before it, we skip to the next to avoid duplicates.
           For each value, we then treat it like the sorted 2 sum problem, where we set left and right pointers,
           where left is the current + 1. We compute the sum as the values at left and right plus the anchor value and based on if it is less or greater than 0 we adjust l and r.
           If the sum equals 0 then we add it to the result list, and then we increment l past any duplicates of the value we just used.
           Skipping duplicate anchors and duplicate l values guarantees each triplet is only found once.


Time Complexity: O(n^2) where n is the length of the array, the outer loop runs n times and for each anchor the two pointer scan is O(n),
                 the O(n log n) sort is dominated.

Space Complexity: O(1) extra space ignoring the sort and the output, O(n) where n is the length of the array if the sort's internal space counts.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                curr = nums[i] + nums[l] + nums[r]

                if curr == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l, r = l+1, r-1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1

                elif curr < 0:
                    l += 1
                else:
                    r -= 1
        return res