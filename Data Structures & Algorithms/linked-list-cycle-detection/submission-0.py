# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hasSeen = []
        while head:
            if head in hasSeen:
                return True
            hasSeen.append(head)
            head = head.next
        return False