class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, val: int) -> None:
        
        if len(self.min) == 0:
            self.min.append(val)
        
        else:
            currentmin= self.min[-1]
            if currentmin > val:
                self.min.append(val)
            else:
                self.min.append(currentmin)
                
        self.stack.append(val)
        # print(self.stack)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        # print(i, self.stack)

    def top(self) -> int:
        # print(self.stack)
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
