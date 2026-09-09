class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for t in tokens:
            # 1. Checking if t is an operator using a set is a lightning-fast O(1) operation
            if t in {'+', '-', '*', '/'}:
                # 2. Pop right-hand operand, then left-hand operand
                a = stack.pop()
                b = stack.pop()
                
                # 3. Inline evaluations have ZERO function call overhead
                if t == '+':
                    stack.append(b + a)
                elif t == '-':
                    stack.append(b - a)
                elif t == '*':
                    stack.append(b * a)
                else:
                    # Truncation toward zero handled with int()
                    stack.append(int(b / a))
            else:
                # 4. If it's not an operator, it's definitely a number
                stack.append(int(t))
                
        return stack[0]

        
