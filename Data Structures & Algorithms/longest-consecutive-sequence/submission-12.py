class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set()
        for i in nums:
            res.add(i)
        globalLargest = float("-inf")
        for i in range(len(nums)):
            localLargest = 1
            localIter = 1
            if nums[i]-1 not in res:
                while nums[i]+localIter < len(nums)+1:
                    if nums[i]+localIter in res:
                        localIter += 1
                        localLargest += 1
                    else:
                        break
                globalLargest = max(localLargest, globalLargest)
        return max(globalLargest,0)