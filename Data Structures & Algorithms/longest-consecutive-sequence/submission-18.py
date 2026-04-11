class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        globalMax = 0
        for i in res:
            currMax = 1
            if i-1 not in res:
               j = i
               while True:
                if j+1 in res:
                    currMax += 1
                    j += 1
                else:
                    break
                
            globalMax = max(globalMax, currMax)
        return globalMax