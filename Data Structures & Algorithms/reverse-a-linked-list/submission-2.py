# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        #before reversal - prev->curr->curr.next
        #after reversal - curr.next->curr->prev
        while curr: 
            newhead = curr.next
            curr.next=prev
            prev = curr 
            curr = newhead 
        return prev