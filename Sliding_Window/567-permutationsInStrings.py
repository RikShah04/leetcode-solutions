"""
Problem: Leetcode 567 Permutation in String

Intuition: We create two arrays the size of the alphabet, and for every char in s1, and in the starting window of s2
(which will be the same size as s1), we increment the char's corresponding index in its array. Then we iterate over the character arrays
and anytime both arrays have a matching value for a letter we increment a variable called matches. Then we start a loop with r set at the end of our window
and l set at the start. If matches ever equals 26 we return true because then for every letter the arrays perfectly match.
Otherwise we first increment the letter r corresponds to now. If now the count of the letter r corresponds to matches what its count is in s1's array, then we increment matches,
however if it previously matched and adding r to the window made it no longer match we decrement matches. We then remove the current l from the window, and see if that increased or decreased matches.
If the loop terminates and matches == 26 we return true otherwise false

Time Complexity: O(n) we iterate over each char in each string

Space Complexity: O(1) since the arrays are always size 26 (fixed alphabet size, not a variable input)

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0

        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            r_index = ord(s2[r]) - ord('a')
            s2Count[r_index] += 1

            if s2Count[r_index] == s1Count[r_index]:
                matches += 1
            elif  s2Count[r_index] - 1 == s1Count[r_index]:
                matches -= 1
            
            l_index = ord(s2[l]) - ord('a')
            s2Count[l_index] -= 1

            if s2Count[l_index] == s1Count[l_index]:
                matches += 1
            elif s2Count[l_index] + 1 == s1Count[l_index]:
                matches -= 1

            l += 1
            
        return matches == 26
