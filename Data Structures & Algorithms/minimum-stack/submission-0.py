class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = sys.maxsize
        

    def push(self, val: int) -> None:
        if (len(self.stack)==0):
            minVal = val
        self.stack.append(val - self.minVal)
        self.minVal = min(self.minVal, val)
        

    def pop(self) -> None:
        if (self.stack[-1] < 0):
            self.minVal -= self.stack[-1]
        self.stack.pop()

    def top(self) -> int:
        return (self.stack[-1]+self.minVal if self.stack[-1] >= 0 else self.minVal)
        

    def getMin(self) -> int:
        return self.minVal