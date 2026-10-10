class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxObservedArea = 0
        left, right = 0, len(heights)-1
        while left < right :
            currArea = min(heights[left],heights[right])*(-left+right)
            maxObservedArea = max(maxObservedArea, currArea)
            if heights[left]>heights[right]:
                right -= 1
            else:
                left += 1

        return maxObservedArea