# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        newCurr, othCurr = list1, list2
        newPrev = None
        newHead = None

        while newCurr:
            if newCurr.val > othCurr.val:
                temp = othCurr
                othCurr = newCurr
                newCurr = temp
                if newPrev:
                    newPrev.next = newCurr

            if newCurr.val <= othCurr.val:
                newPrev = newCurr
                newCurr = newCurr.next

            if not newHead:
                newHead = newPrev

        if othCurr:
            if newPrev:
                newPrev.next = othCurr
            else:
                newHead = othCurr

        return newHead
