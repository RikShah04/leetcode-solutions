"""
Problem: Leetcode 125 Valid Palindrome

Intuition: We set two pointers, one from the start and one from the end
           we skip any non-alphanumeric characters by advancing the pointers past them
           we keep comparing the values at those pointers (case-insensitively) and increment/decrement them
           till they meet, if the values ever differ we return false, if the loop terminates
           its a palindrome

Time Complexity: O(n) where n is the length of the string, at worst we iterate over every character once

Space Complexity: O(1), the only thing we store is 2 pointers that get updated
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l<r and not self.isNumLetter(s[l]):
                l += 1
            while l<r and not self.isNumLetter(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    def isNumLetter(self, s: str):
        return (
            (ord('A') <= ord(s) <= ord('Z')) or
            (ord('a') <= ord(s) <= ord('z')) or
            (ord('0') <= ord(s) <= ord('9')) 
        )