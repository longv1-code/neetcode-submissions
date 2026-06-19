# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        Binary Search Tree -> from the current node, 
        all values on the left subtree is smaller and all values on the right subtree is greater

        Pattern: DFS
        Approach:
        1. In-Traversal
        '''
        res = []

        def dfs(node, arr):
            if not node:
                return
            
            dfs(node.left, arr)
            arr.append(node.val)
            dfs(node.right, arr)

        dfs(root, res)
        return res[k - 1]