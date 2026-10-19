# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if (head == None):
            return head

        curr = head
        next = head.next
        prev = None
        while (next != None):
            curr.next = prev
            prev = curr
            curr = next
            if (next):
                next = next.next
        curr.next = prev
        return curr