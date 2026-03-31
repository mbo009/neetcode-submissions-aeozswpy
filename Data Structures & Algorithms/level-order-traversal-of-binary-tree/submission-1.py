# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []

        def dfs(root, depth):
            if not root:
                return
            if len(self.res) <= depth:
                self.res.append([])
            
            self.res[depth].append(root.val)

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        
        dfs(root, 0)
        return self.res

# 1
# 2
# 3
