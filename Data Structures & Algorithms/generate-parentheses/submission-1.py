class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def backtrack(opened, closed):
            if len(subset) == n * 2:
                res.append("".join(subset.copy()))

            if opened < n:
                subset.append('(')
                backtrack(opened + 1, closed)
                subset.pop()
            if opened > closed and closed < n:
                subset.append(')')
                backtrack(opened, closed + 1)
                subset.pop()

        backtrack(0, 0)
        return res