"""
Problem: Leetcode 167 Two Sum II

Intuition: Since the array is sorted, we can create two pointers for the start and end of the list
           if the sum of the values at the two pointers is less than the target, we know the left pointer needs to be incremented
           since every other pair with the current left value would be even smaller
           if the sum is too high, we know the right pointer needs to be decremented since every other pair with the current right value would be even larger
           once the sum == the target we return the 1 indexed pair

Time Complexity: O(n) where n is the length of the list, at worst we look at every value in the list

Space Complexity: O(1) the only values that are stored are the pointers

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total < target:
                l += 1
            else:
                r -= 1