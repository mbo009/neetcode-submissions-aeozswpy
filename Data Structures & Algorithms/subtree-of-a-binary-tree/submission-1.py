# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root: Optional[TreeNode], subRoot) -> bool:
            if root is None and subRoot is None:
                return True

            if root is None or subRoot is None or root.val != subRoot.val:
                return False
            
            return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
    
        def find_start(root):
            if root is None:
                return False
            
            if isSameTree(root, subRoot):
                return True
            
            return find_start(root.left) or find_start(root.right)

        return find_start(root) 
            

            

            


