# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        first = True

        while slow and fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

            # Detection
            if not first and slow == fast:
                return True

            first = False

        return False