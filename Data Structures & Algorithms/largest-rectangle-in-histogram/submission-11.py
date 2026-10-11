class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = float('-inf')
        for bar in enumerate(heights):
            while stack and stack[-1][1]>=bar[1]:
                poppedBar = stack.pop()
                left = stack[-1][0] + 1 if stack else 0
                right = bar[0] - 1
                currentArea = (right -left + 1) * poppedBar[1]
                # print(currentArea)
                maxArea = max(maxArea, currentArea)
            stack.append(bar)
        
        while stack:
            poppedBar = stack.pop()
            left = stack[-1][0] + 1 if stack else 0
            right = len(heights) - 1
            currentArea = (-left+right+1) * poppedBar[1]
            # print(currentArea , poppedBar)
            maxArea = max(maxArea, currentArea)

        return int(maxArea)