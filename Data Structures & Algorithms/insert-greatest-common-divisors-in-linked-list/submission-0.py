from math import gcd
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:        
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head

        prev = head
        curr = head.next

        while curr:
            prev.next = ListNode(gcd(prev.val, curr.val), prev.next)
            prev = curr
            curr = curr.next

        return head
