"""
Problem: Leetcode 49 Group Anagrams

Intuition: We can create a dictionary, mapping counters for strings to a list of strings, this way all the strings that are made of the same characters are grouped. We can then return just the values of the dictionary

Time Complexity: O(m * n) where m is the number of strings and n is the length of the longest string

Space Complexity: O(m) we only store each string once, and at worst we store the character count of each string once

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            mapping[tuple(count)].append(s)
        
        return list(mapping.values())