class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def backtrack(openBracket, closeBracket):
            if openBracket == closeBracket == n:
                res.append("".join(subset.copy()))
                return
            
            if openBracket < n:
                subset.append("(")
                backtrack(openBracket + 1, closeBracket)
                subset.pop()
            if closeBracket < openBracket:
                subset.append(")")
                backtrack(openBracket, closeBracket + 1)
                subset.pop()

        backtrack(0, 0)
        return res