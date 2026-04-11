class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0 for i in height]
        suffix = [0 for i in height]
        currPrMax = 0
        currSuMax = 0
        for i in range(len(height)):
            prefix[i] = currPrMax
            suffix[len(height)-i-1] = currSuMax
            currPrMax = max(currPrMax, height[i])
            currSuMax = max(currSuMax, height[len(height)-i-1])

        totalWater = 0
        for i in range(len(height)):
            currWaterLevel = min(prefix[i], suffix[i]) - height[i]
            if currWaterLevel>0:
                totalWater += currWaterLevel

        return totalWater