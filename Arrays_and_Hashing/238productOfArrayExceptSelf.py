"""
Problem: Leetcode 238 Product of Array Except Self

Intuition: we create a prefix array by iterating forward through the list of nums keeping a running product starting at 1, we first append the running product to the prefix array
           then we multiply the running product by the current num, we multiply after appending because we want index i to hold the product of everything before it, excluding nums[i] itself
           we then iterate backwards through the array and do the same, but instead of appending we multiply the corresponding index by the running product before folding nums[i] in, again so nums[i] is excluded from its own result

Time Complexity: O(n) where n is the length of the array, because we just iterate over the array twice

Space Complexity: O(1) extra space excluding the output array, we reuse the output array for the prefix products and only keep a running scalar for the suffix pass, O(n) if the output array counts

"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        rs = 1
        for num in nums:
            prefix.append(rs)
            rs *= num
        
        rs = 1
        for i in range(len(nums)-1, -1 , -1):
            prefix[i] *= rs
            rs *= nums[i]
        return prefix
        
