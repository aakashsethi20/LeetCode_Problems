"""
Submission: Accepted!

Runtime: 28 ms, faster than 99.01% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.9 MB, less than 5.28% of Python3 online submissions for Valid Parentheses.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if s is None:
            return False
        length_of_input = len(s)
        if length_of_input == 0:
            return True
        if length_of_input % 2 == 1:
            return False

        open_set = {'(', '[', '{'}
        close_set = {')', ']', '}'}
        
        if s[0] not in open_set or s[-1] not in close_set:
            return False
        
        close_to_open_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for bracket in s:
            if bracket in open_set:
                stack.append(bracket)
            else:
                if stack.pop() != close_to_open_dict[bracket]:
                    return False
        
        return not stack
