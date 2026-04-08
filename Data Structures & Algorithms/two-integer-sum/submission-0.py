class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsFreq = {}
        result = []
        for i in nums:
            numsFreq[i] = numsFreq.get(i,0) + 1
        for i in range(len(nums)):
            numsFreq[nums[i]] -= 1
            if (target-nums[i]) in numsFreq and numsFreq[target-nums[i]]>0:
                result.append(i)
                numsFreq[nums[i]] += 1
        return result

