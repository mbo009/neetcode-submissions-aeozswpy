# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def llist_len(node):
            curr = node
            curr_len = 0
            while curr:
                curr = curr.next
                curr_len += 1
            
            return curr_len
    
        def llist_to_int(node, length):
            acc = 0
            curr = node
            i = 1
            while curr:
                acc += curr.val * 10**(length - i)
                curr = curr.next
                i += 1
            
            return acc
        
        len1, len2 = llist_len(l1), llist_len(l2)
        acc1, acc2 = llist_to_int(l1, len1), llist_to_int(l2, len2)
        new_val = acc1 + acc2 
        digits = [int(digit) for digit in str(new_val)]
        print(acc1, acc2)
        root = ListNode(digits[0])
        curr = root

        for i in range(1, len(digits)):
            curr.next = ListNode(digits[i])
            curr = curr.next
    
        return root
            

        
