# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNode(self, root, key):
        last = None
        curr = root
        while curr:
            if key == curr.val:
                return last, curr

            last = curr
            if key > curr.val:
                curr = curr.right
            else:
                curr = curr.left

        return None, None

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        last, curr = self.findNode(root, key)
        if not curr:
            return root
        
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right
            
            if not last:
                return child 
            
            if last.left == curr:
                last.left = child
            else:
                last.right = child
        
        else:
            new_last = curr
            new_curr = curr.right
            while new_curr.left:
                new_last = new_curr
                new_curr = new_curr.left

            curr.val = new_curr.val
            if new_last != curr:
                new_last.left = new_curr.right
            else:
                new_last.right = new_curr.right
    
        return root
            

