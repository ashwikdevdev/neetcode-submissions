class Solution:
    def isValid(self, s: str) -> bool:
        # trace={'(':0,')':0,'[':0,']':0,'{':0,'}':0,}
        # for i in s:
        #     if i == '(' or '{' or '[':
        #         trace[i] += 1
        #     if i == ')':
        #         if trace['(']<= 0:
        #             return False
        #         else:
        #             trace['('] -= 1
        #     if i == '}':
        #         if trace['{']<= 0:
        #             return False
        #         else:
        #             trace['{'] -= 1
        #     if i == ']':
        #         if trace['[']<= 0:
        #             return False
        #         else:
        #             trace['['] -= 1    

        # return True

        stack =[]
        open = {'(','{','['}
        close = {')','}',']'}
        for i in s:
            if i in open:
                stack.append(i)
            if i in close:
                if len(stack) == 0:
                    return False
                pop = stack.pop()
                if i == ')':
                    if pop != '(':
                        return False
                if i == '}':
                    if pop != '{':
                        return False
                if i == ']':
                    if pop != '[':
                        return False  
        if len(stack) == 0:               
            return True 
        return False

