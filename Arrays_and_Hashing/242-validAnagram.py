"""
Problem: LeetCode 242 - Valid Anagram

Intuition:
In order to check if one string is an anagram of another, we can just track what letters ( and their occurences), appear in each string, and then check these dicts against one another

Time Complexity:
O(n) - we iterate over every character in each string once

Space Complexity:
O(1) - we store two dictionarys that have at max 26 elements each
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}

        for i in range(len(s)):
            sDict[s[i]] = sDict.get(s[i], 0) + 1
            tDict[t[i]] = tDict.get(t[i], 0) + 1

        return sDict == tDict 