# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists
        
        l1 = lists[0]
        processed = 1
        while processed < len(lists):
            l2 = lists[processed]
            head = ListNode()
            curr = head

            while l1 and l2:
                if l1.val < l2.val:                    
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            
            if l1:
                curr.next = l1
            else:
                curr.next = l2

            l1 = head.next
            processed += 1
    
        return head.next
            

