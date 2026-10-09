class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbersSeen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numbersSeen:
                return [numbersSeen[diff], i]
            numbersSeen[nums[i]] = i