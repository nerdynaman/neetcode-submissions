class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        prefixArr = [i for i in range(len(heights))]
        suffixArr = [len(heights)-1 for i in range(len(heights))]
        for idx, barHeight in enumerate(heights):
            while stack and stack[-1][1] >= barHeight:
                localIdx, localBarHeight = stack.pop()
                suffixArr[localIdx] = idx-1
            prefixArr[idx] = stack[-1][0]+1 if stack else 0
            stack.append((idx, barHeight))

        maxArea = float('-inf')
        for i in range(len(heights)):
            area = (suffixArr[i] - prefixArr[i] + 1)*heights[i]
            maxArea = max(maxArea, area)
        return maxArea