from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root):
            if not root:
                return []
            return [root.val] + bfs(root.left) + bfs(root.right)    
        return bfs(root)