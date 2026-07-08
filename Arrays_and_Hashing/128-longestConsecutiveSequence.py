"""
Problem: Leetcode 128 Longest Consecutive Sequence

Intuition: We create a set of every val in the array, then iterate over the array
           for each val we check if val - 1 is in the array (using set for O(1) access time)
           if a number's prev val is not in the array then it is the start of a sequence
           we then keep checking val + 1 to see how long the seq continues, updating the longest length as we go.

Time Complexity: O(n) where n is the length of the array, the outer loop does O(1) work for each element and the inner loop visits at most every element once,
                 since the inner loop only runs at the start of a sequence

Space Complexity: O(n) where n is the length of the array, because we create a set with every value from the original array

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        vals = set(nums)

        for num in nums:
            if num - 1 in vals:
                continue
            
            currLen = 1
            curr = num

            while curr + 1 in vals:
                currLen += 1
                curr += 1
            res = max(currLen, res)
        return res
