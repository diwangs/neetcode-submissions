# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = None
        nex = head

        while nex:
            temp = nex.next
            nex.next = cur
            
            cur = nex
            nex = temp

        return cur