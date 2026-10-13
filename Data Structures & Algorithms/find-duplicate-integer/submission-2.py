class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while slow < len(nums) and fast < len(nums):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0 
        while True:
            if nums[slow] == nums[fast]:
                return nums[slow]
            
            slow = nums[slow]
            fast = nums[fast]