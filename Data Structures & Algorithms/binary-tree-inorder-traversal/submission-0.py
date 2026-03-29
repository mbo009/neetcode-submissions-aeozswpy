# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root):
            if not root:
                return []
            curr_path = []
            if root.left:
                curr_path += bfs(root.left)
            curr_path += [root.val]
            if root.right:
                curr_path += bfs(root.right)
            return curr_path
    
        return bfs(root)