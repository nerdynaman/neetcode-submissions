class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = { ")" : "(", "}" : "{", "]" : "["}
        for i in s:
            if i in mapper and len(stack)>0:
                if stack.pop() == mapper[i]:
                    continue
                else:
                    return False
            else:
                stack.append(i)
        
        return False if (len(stack) > 0) else True
        