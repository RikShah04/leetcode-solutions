"""
Problem: Leetcode 271 Encode and Decode Strings

Intuition: 
    encode: we prepend each string with its length then a '#' symbol so that we know when the length is done,
            then join all the strings together and return it
    decode: we keep a pointer, find the next occurrence of '#', and everything between our pointer and the
            symbol is the length. The string we append starts one past the symbol and spans that length.
            We then jump our pointer to the end of the found string and continue.

Time Complexity: O(n), where n is the total number of characters across all strings.
                 encode touches each character once when joining.
                 decode also touches each character once: find() always searches forward from i,
                 so no character is scanned twice.
Space Complexity: O(n) encode builds a string containing all n characters plus their length prefixes.
                  decode stores the decoded strings, which total n characters.

"""

class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s)) + "#" + s for s in strs )

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find("#", i, len(s))
            length = int(s[i:j])
            res.append(s[j+1 : j+length+1])
            i = j + length + 1
        return res