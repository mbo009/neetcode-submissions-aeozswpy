class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_llist(root):
            prev = None
            curr = root
            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev
        
        r_l1, r_l2 = reverse_llist(l1), reverse_llist(l2)
        
        head = ListNode()
        curr = head
        curr1 = r_l1
        curr2 = r_l2
        acc = 0
        
        while curr1 or curr2 or acc:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            
            curr_sum = val1 + val2 + acc
            
            acc = curr_sum // 10
            curr.next = ListNode(curr_sum % 10)
            curr = curr.next
            
            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next
            
        return reverse_llist(head.next)