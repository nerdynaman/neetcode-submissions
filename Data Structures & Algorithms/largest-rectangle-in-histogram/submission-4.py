class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                currValue = heights[stack.pop()]
                currNSE = i
                currPSE = stack[-1] if stack else -1
                maxArea = max(maxArea, currValue * (currNSE - currPSE - 1))
            stack.append(i)
        
        currNSE = len(heights)
        while stack:
            # print(stack, maxArea)
            currVal = stack.pop()
            currPSE = stack[-1] if stack else -1
            maxArea = max(maxArea, heights[currVal] * (currNSE - currPSE - 1))
        return maxArea