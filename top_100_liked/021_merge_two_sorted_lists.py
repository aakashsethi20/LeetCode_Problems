"""
Submission: Accepted!

Runtime: 44 ms, faster than 65.80% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.7 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        dummy_list = ListNode(0)
        new_list = dummy_list
        while new_list is not None:
            if l1 is not None and l2 is not None:
                if l1.val <= l2.val:
                    new_list.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    new_list.next = ListNode(l2.val)
                    l2 = l2.next
            elif l1 is not None:
                new_list.next = ListNode(l1.val)
                l1 = l1.next
            elif l2 is not None:
                new_list.next = ListNode(l2.val)
                l2 = l2.next
                
            new_list = new_list.next

        new_list = dummy_list.next
        return new_list  

def main():
    numbers_1 = [1, 2, 4]
    numbers_2 = [1, 3, 4]
    
    l1_dummy = ListNode(0)
    l2_dummy = ListNode(0)
    l1 = l1_dummy
    l2 = l2_dummy

    for number_1, number_2 in zip(numbers_1, numbers_2):
        l1.next = ListNode(number_1)
        l1 = l1.next

        l2.next = ListNode(number_2)
        l2 = l2.next

    l1 = l1_dummy.next
    l2 = l2_dummy.next

    solution = Solution()

    print(solution.mergeTwoLists(l1, l2).val)

if __name__ == "__main__":
    main()
