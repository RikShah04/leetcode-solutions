"""
Problem: LeetCode 217 - Contains Duplicate

Intuition:
To check if there are any duplicates in the given list, we can use a hash set (set in Python) to store the unique elements as we traverse the list. For each element, we check if it is already present in the set. If it is, then we have found a duplicate, and we return True. If we traverse the entire list without finding any duplicates, we return False.

Time Complexity:
O(n) - we iterate over every element once at worst

Space Complexity:
O(n) - we store every number once at worst 
"""

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        noDupes = set()

        for num in nums:
            if num in noDupes:
                return True
            noDupes.add(num)

        return False