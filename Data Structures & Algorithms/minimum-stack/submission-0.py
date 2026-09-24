class MinStack:

    def __init__(self):
        self.stack =[]
        self.minim=[]
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minim:
            self.minim.append(val)
        else:
            current_min = min(val,self.minim[-1])
            self.minim.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minim.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minim[-1]
        
