class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left < right and right < len(nums):
            if nums[left] <= nums[right]:
                return nums[left]
            
            mid = left + (right-left)//2

            if nums[left]<=nums[mid]:
                left = mid + 1
            else:
                right = mid
        print(left, right)
        return nums[left]
