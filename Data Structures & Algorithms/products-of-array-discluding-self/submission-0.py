class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArr = []

        totalProduct = 1
        for i in range(len(nums)):
            prefixArr.append(totalProduct)
            totalProduct *= nums[i]
        
        suffixArr = [0 for i in nums]
        totalProduct = 1
        for j in range(len(nums)-1,-1,-1):
            suffixArr[j] = totalProduct
            totalProduct *= nums[j]
        
        res = []
        for i in range(len(nums)):
            res.append(prefixArr[i]*suffixArr[i])

        return res
