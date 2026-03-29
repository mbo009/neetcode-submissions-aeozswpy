# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        acc_sum = 0
        i = 1
        node1 = l1
        node2 = l2

        while node1 or node2:
            if node1:
                acc_sum += i * node1.val
                node1 = node1.next
            if node2:
                acc_sum += i * node2.val
                node2 = node2.next
            i *= 10
        
        acc_str = str(acc_sum)[::-1]
        if len(acc_str) < 2:
            return ListNode(acc_sum)
        
        prev = ListNode(int(acc_str[0]))
        head = prev
        for num in acc_str[1::]:
            temp_node = ListNode(int(num))
            prev.next = temp_node
            prev = temp_node
        
        return head