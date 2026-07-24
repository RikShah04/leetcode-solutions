"""
Problem: Leetcode 3 Longest Substring Without Repeating Characters.

Intuition: We iterate over the characters in the string, keeping a set of all characters in our current window
           so we can check membership in O(1). We also keep a pointer l representing the start of the window.
           If the current character is already in the window, we keep removing characters from the start,
           updating the set and l, until it is no longer a duplicate. We then add it and check if the current
           window length (r - l + 1) is longer than the max seen so far.

Time Complexity: O(n) where n is the length of the string, each character is visited at most twice: once when
                 added by r, once when removed by l.

Space Complexity: O(m) where m is the number of unique characters in the string
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        substring = set()
        l = 0

        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[r])

            maxLength = max(maxLength, r - l + 1)

        return maxLength 
