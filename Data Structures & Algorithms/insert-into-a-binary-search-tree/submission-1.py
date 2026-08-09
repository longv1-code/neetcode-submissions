# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def dfs(root, val):
            if not root:
                return False
            
            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                    return True
                else:
                    if dfs(root.left, val):
                        return True
            else:
                if not root.right:
                    root.right = TreeNode(val)
                    return True
                else:
                    if dfs(root.right, val):
                        return True

        dfs(root, val)
        return root