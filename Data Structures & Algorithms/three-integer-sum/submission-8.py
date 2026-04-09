class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            startPtr, endPtr = i+1, len(nums)-1
            while startPtr < endPtr:
                if (nums[startPtr] + nums[endPtr] == target):
                    if startPtr>0 and nums[startPtr]==nums[startPtr-1] and startPtr-1!=i:
                        startPtr += 1
                        continue
                    result.append([nums[i],nums[startPtr],nums[endPtr]])
                    startPtr += 1
                    endPtr -= 1
                    # break
                elif (nums[startPtr] + nums[endPtr] < target):
                    startPtr += 1
                else:
                    endPtr -= 1
        
        return result