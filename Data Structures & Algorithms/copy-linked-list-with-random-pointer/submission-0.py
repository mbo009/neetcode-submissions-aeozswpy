"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copy_dict = dict()
        prev = Node(-1)
        curr = head
        new_head = prev

        while curr:
            if curr not in copy_dict:
                copy_dict[curr] = Node(curr.val)
            curr_copy = copy_dict[curr]

            prev.next = curr_copy
            prev = curr_copy

            if curr.random:
                if curr.random not in copy_dict:
                    copy_dict[curr.random] = Node(curr.random.val)
                curr_copy.random = copy_dict[curr.random]
    
            curr = curr.next

        return new_head.next
            