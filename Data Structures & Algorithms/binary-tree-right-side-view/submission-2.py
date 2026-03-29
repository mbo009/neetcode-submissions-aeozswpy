# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, depth, res):
        if not root:
            return
        if len(res) == depth:
            res.append(root.val)
        
        self.dfs(root.right, depth + 1, res)
        self.dfs(root.left, depth + 1, res)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        depth = 0
        self.dfs(root, depth, res)
        return res