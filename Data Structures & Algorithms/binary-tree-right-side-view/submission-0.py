# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()

        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                popped = q.popleft()
                if popped:
                    level.append(popped.val)
                    q.append(popped.left)
                    q.append(popped.right)
            if level:
                res.append(level[-1])
        
        return res