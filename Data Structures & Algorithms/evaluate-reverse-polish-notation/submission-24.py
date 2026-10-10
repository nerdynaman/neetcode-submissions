class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        math = ('+','-','*','/')
        stack = []
        for i in tokens:
            if i not in math:
                stack.append(int(i))
            else:
                numA = stack.pop()
                numB = stack.pop()
                res = self.getRes(numB, numA,i)
                stack.append(res)
            # print(stack)
        return stack.pop()

    def getRes(self, left, right, operation):
        if operation == '+':
            return left + right
        elif operation == '-':
            return left - right
        elif operation == '*':
            return left*right
        elif operation == '/':
            return int(left/right)