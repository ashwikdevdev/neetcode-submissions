class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        import operator
        stack = []
        # for t in tokens:
        #     if t in {'+', '-', '*', '/'}:
        #         a = stack.pop()
        #         b = stack.pop()
        #         if t == '+':
        #             stack.append(b + a)
        #         elif t == '-':
        #             stack.append(b - a)
        #         elif t == '*':
        #             stack.append(b * a)
        #         else:
        #             stack.append(int(b / a))
        #     else:
        #         stack.append(int(t))
        b , a = 0,0
        ops = {
            '*': operator.mul,
            '+': operator.add,
            '-': operator.sub,
            '/': lambda b,a : int(b/a)
        }
        for t in tokens:
            if t in {'+', '-', '*', '/'}:
                a = stack.pop()
                b = stack.pop()
                stack.append(ops[t](b,a))
            else:
                stack.append(int(t))

        
                
        return stack[0]

        
