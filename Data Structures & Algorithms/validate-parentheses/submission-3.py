class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stk = []

        for c in s:
            if c not in match:
                stk.append(c)
            else:
                if stk and stk[-1] == match[c]:
                    stk.pop()
                else:
                    return False
        
        return True if not stk else False