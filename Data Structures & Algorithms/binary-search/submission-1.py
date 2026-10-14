class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        size = len(nums)
        if target >= nums[size//2]:
            res = self.search(nums[size//2:], target)
            if res >= 0:
                return (size//2) + res
            else:
                return -1
                
        else:
            return self.search(nums[:size//2],target)