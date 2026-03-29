# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _reverse(self, start, cut):
        prev = None
        curr = start
        i = 0
        while i < cut and curr :
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
            i += 1
        
        return prev, curr
        

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        n = 0
        while curr:
            curr = curr.next
            n += 1
    
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        curr = head
    
        while n >= k:
            new_head, next_part = self._reverse(curr, k)
            
            group_prev.next = new_head
            curr.next = next_part
            
            group_prev = curr
            curr = next_part
            n -= k 
            
        return dummy.next
# 9
# 2
# 5
# 8