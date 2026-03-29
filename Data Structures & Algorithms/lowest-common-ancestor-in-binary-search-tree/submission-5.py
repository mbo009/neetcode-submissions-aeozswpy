# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        if p.val > q.val:
            lower = q
            higher = p
        else:
            lower = p
            higher = q
        
        while curr.left or curr.right:
            if lower.val <= curr.val and higher.val >= curr.val:
                return curr
            elif lower.val <= curr.val and higher.val <= curr.val:
                curr = curr.left
            elif lower.val >= curr.val and higher.val >= curr.val:
                curr = curr.right
        
        return curr
