"""
Problem: Leetcode 20 Valid Parentheses

Intuition: We create a dictionary that maps every closing char to the opening char, and initialize an empty stack.
           We iterate over each char in the string, if it's an opening character we add it to the stack. If it's a closing character,
           we check that the stack has something in it, and that the top of the stack opens the current character. If either of those are untrue
           it is not valid. After we iterate over the entire string, we return true as long as the stack is empty. If it was not that would mean
           there was an unclosed parentheses. Note this relies on the input only ever containing the characters "(){}[]", since matching[char]
           assumes char is always a valid key whenever it's not an opening bracket.

Time Complexity: O(n) where n is the length of the string, we iterate over each char at most once

Space Complexity: O(n) where n is the length of the string, worst case we store every character at most once

"""

class Solution:
    def isValid(self, s: str) -> bool:
        matching = {"}": "{", ")": "(", "]": "["}
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if not stack or matching[char] != stack.pop():
                    return False
        return not stack