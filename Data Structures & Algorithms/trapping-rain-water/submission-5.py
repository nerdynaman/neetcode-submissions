class Solution:
    def trap(self, height: List[int]) -> int:
        suffixArr = [0 for _ in height]
        maxHeightSeen = -1
        for i in range(len(height)-1,-1,-1):
            suffixArr[i]=maxHeightSeen
            maxHeightSeen = max(maxHeightSeen, height[i])
        
        totalWater = 0
        maxHeightSeen = -1
        for i in range(len(height)):
            totalWater += max(min(maxHeightSeen, suffixArr[i])-height[i],0)
            maxHeightSeen = max(maxHeightSeen, height[i])
        
        return totalWater