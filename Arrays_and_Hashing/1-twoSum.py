"""
Problem: Leetcode 1 - Two Sum

Intuition: We can create a dictionary where the the values are the current index, and the keys are what is needed to sum to the target
           this makes it so that when we iterate over the list as soon as the second element forming the pair is found we can return

Time Complexity:
O(n) - The worst case scenario is the very last element being part of the solution, so at worst we look at every element once

Space Complexity:
O(n) - The worst case scenario is the very last element being part of the solution, so at worst we have n-1 elements in the  dict where n is the number of nums in the list

"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pairs = {}

        for i in range(len(nums)):
            val = nums[i]
            needed = target - val
            
            if needed in pairs:
                return [pairs[needed], i]
    
            pairs[val] = i