# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxValue):
            if not node:
                return 0
            
            if node.val >= maxValue:
                return 1 + dfs(node.left, max(node.val, maxValue)) + dfs(node.right, max(node.val, maxValue))
            else:
                return dfs(node.left, max(node.val, maxValue)) + dfs(node.right, max(node.val, maxValue))
        
        return dfs(root, float('-inf'))
