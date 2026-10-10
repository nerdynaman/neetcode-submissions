class Solution:
    def isValid(self, s: str) -> bool:
        check = {'(':')', '[':']', '{':'}'}
        stack = []
        for i in s:
            if i in check:
                stack.append(i)
            else:
                if len(stack) and check[stack.pop()] == i:
                    continue
                else:
                    return False
        return False if stack else True