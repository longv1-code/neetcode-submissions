# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(n1, n2):
            if not n1 and not n2:
                return None
            
            if n1 and n2:
                root = TreeNode(n1.val + n2.val)
                root.left = dfs(n1.left, n2.left)
                root.right = dfs(n1.right, n2.right)
            else:
                root = TreeNode(n1.val if n1 else n2.val)
                root.left = n1.left if n1 else n2.left
                root.right = n1.right if n1 else n2.right

            return root

        return dfs(root1, root2)