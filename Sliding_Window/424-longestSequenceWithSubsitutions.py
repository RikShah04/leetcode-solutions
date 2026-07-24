"""
Problem: Leetcode 424 Longest Repeating Character Replacement

Intuition: We iterate over the list of characters in the string, while also keeping a left pointer which represents the start of 
           the current sequence. We also keep track of the counts of the characters in the current sequence.
           for each character we first update its count in the current window, and if its count is larger than the max count of any char
           we have seen in a window we update that variable. Note that maxCount represents the max frequency of any character seen in any 
           window so far, not necessarily the current window, it is a running upper bound rather than a live recalculation. Then if adding 
           the character to the window made the window invalid then we shift the left pointer. We check if a window is invalid by computing 
           if the window size (r - l + 1) - the max count of a char seen is greater than the allowed number of substitutions. This works 
           because if the window length - the max char count is bigger than k then even with k substitutions we would still have a character 
           that would not match. We also can use the max count of a char seen because even if it allows a window to get bigger than it may 
           actually be allowed to, it will never surpass the true actual largest window.

Time Complexity: O(n) where n is the length of the array, we iterate over every character once

Space Complexity: O(m) where m is the number of unique characters in the array

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        count = {}
        l = 0
        maxCount = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxCount = max(maxCount, count[s[r]])
            
            while (r - l + 1) - maxCount > k:
                count[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)

        return maxLen