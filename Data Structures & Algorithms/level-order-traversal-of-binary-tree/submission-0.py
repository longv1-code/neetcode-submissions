# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []

        q.append(root)
        while q:
            temp = []
            for _ in range(len(q)):
                popped = q.popleft()
                if not popped:
                    continue 
                temp.append(popped.val)
                q.append(popped.left)
                q.append(popped.right)
            if temp:
                res.append(temp)
        
        return res