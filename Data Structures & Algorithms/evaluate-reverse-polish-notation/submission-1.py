class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = "+-*/"
        stk = []
        for c in tokens:
            if c in op:
                b = int(stk.pop())
                a = int(stk.pop())

                if c == "+":
                    stk.append(str(a + b))
                elif c == "-":
                    stk.append(str(a - b))
                elif c == "*":
                    stk.append(str(a * b))
                else:
                    stk.append(str(math.trunc(a / b)))
            else:
                stk.append(c)

        return int(stk[-1])