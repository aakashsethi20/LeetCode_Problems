"""
Submission: Success!

Runtime: 56 ms, faster than 75.00% of Python3 online submissions for Linked List Cycle.
Memory Usage: 16.9 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
"""

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def hasCycle(self, head: ListNode) -> bool:
        if (head is None):
            return False
        if (head.next is None):
            return False
        current = head
        runner = head
        
        while(True):
            if (current.next is not None):
                current = current.next
            else:
                return False
            if (runner.next is not None and runner.next.next is not None):
                runner = runner.next.next
            else:
                return False
                        
            if (current == runner):
                return True
