class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calc=[]
        ans=int()
        if len(tokens)==1:
            return int(tokens[0])
        for i in tokens:
            # print(i)
            
            if i.lstrip('-').isdigit():
                    num = int(i)
                    calc.append(num)
                    # print(calc,i,'isdigit')
            else:
                # print(calc)
                a=int(calc.pop())
                b=int(calc.pop())
                if i == '*':
                    # print(calc)
                    ans = a*b
                    calc.append(ans)
                    # print(calc)
                elif i == '+':
                    ans = b+a
                    calc.append(ans)
                elif i == '/':
                    ans = b/a
                    calc.append(ans)
                elif i == '-':
                    ans = b-a
                    calc.append(ans)
            # print("i++")
        
        return int(ans)
        
