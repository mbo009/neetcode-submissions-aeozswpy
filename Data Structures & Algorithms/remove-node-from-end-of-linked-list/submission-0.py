# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        node = head
        while node:
            node = node.next
            i += 1
        
        prev = None
        curr = head
        j = 0
        while j < i - n:
            prev = curr
            curr = curr.next
            j += 1
        
        if prev:
            prev.next = curr.next
            return head
        else:
            return head.next
        

# 1 0
# 2 1
# 3 2
# 4 3

# 4 - 2