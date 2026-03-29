# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def delete_node(root, prev, is_left=True):
            if not root.left and not root.right and root.val == target:
                if is_left:
                    prev.left = None
                else:
                    prev.right = None

        def dfs(root, prev, is_left=True):
            if not root:
                return
            delete_node(root, prev, is_left)
            dfs(root.left, root)
            dfs(root.right, root, False)
            delete_node(root, prev, is_left)

        prev = TreeNode(-1, root)
        dfs(root, prev)
        return prev.left
            