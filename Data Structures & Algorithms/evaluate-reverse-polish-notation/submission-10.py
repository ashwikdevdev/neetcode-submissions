import operator

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        # 1. Map string tokens directly to functional operations O(1) lookup
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda b, a: int(b / a)  # Handles truncation toward zero directly
        }
        
        for token in tokens:
            # 2. Faster than string manipulation: Just try to convert to int
            try:
                stack.append(int(token))
            except ValueError:
                # If it's not an int, it's an operator
                a = stack.pop()
                b = stack.pop()
                stack.append(ops[token](b, a))
                
        return stack[0]
