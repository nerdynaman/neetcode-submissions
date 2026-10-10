class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')
        self.minValArr = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<self.minVal:
            self.minVal = val
        self.minValArr.append(self.minVal)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minValArr.pop()
        self.minVal = self.minValArr[-1] if self.minValArr else float('inf')
        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.minVal