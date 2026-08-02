class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import math
        stk = []
        op = "+-*/"
        for token in tokens:
            if token not in op:
                stk.append(int(token))
            else:
                if token == '+':
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(a + b)
                elif token == '-':
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(b - a)
                elif token == '*':
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(a * b)
                elif token == '/':
                    a = stk.pop()
                    b = stk.pop()
                    if b / a < 0:
                        stk.append(math.ceil(b / a))
                    else:
                        stk.append(math.floor(b / a))
        return stk[0]