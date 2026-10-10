class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in temperatures]
        stack = []
        for idx, temp in enumerate(temperatures):
            if stack and stack[-1][1] < temp:
                while stack and stack[-1][1]<temp:
                    localRes = stack.pop()
                    result[localRes[0]] = idx-localRes[0]
                stack.append((idx,temp))

            else:
                stack.append((idx, temp))
        
        for idx, _ in stack:
            result[idx]=0
        
        return result