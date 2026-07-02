"""
Problem: Leetcode 347 Top K Frequent Elements

Intuition: First we use counter to get the number of occurences for each number,
           then rather then use normal sorting, we create a list of n lists
           where n is the number of elements, we iterate over the counter and 
           place each value in the index that matches the number of time it occurs,
           we then iterate backwords through the buckets and keep appending to the res
           till we have k elements

Time Complexity: O(n) we iterate through the list once to get the counters, then one more time to place each in a bucket, then at most once more while going backwards through buckets

Space Complexity: O(n) we create a counter that has at most n elements, and then we create n buckets in our bucket array

"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for i in range(len(nums))]
        for key in count:
            buckets[count[key] - 1].append(key)
        
        res = []
        for i in range(len(nums)-1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
