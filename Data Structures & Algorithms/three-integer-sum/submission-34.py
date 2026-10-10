class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue
            # will use two pointer to find target array in remaining subArr
            left, right = i+1, len(nums)-1
            currTarget = -nums[i]
            
            while left < right:
                # print(left,right)
                localRes = nums[left] + nums[right]
                # print(localRes, currTarget)
                if localRes == currTarget:
                    output.append([nums[i], nums[left] , nums[right]])
                    left+=1
                    right-=1
                    while nums[left-1] == nums[left] and left<right:
                        left+=1
                    while nums[right] == nums[right+1] and left<right:
                        right-=1
                elif localRes < currTarget:
                    left+=1
                else:
                    right -= 1
                # print(left,right)
                # break

        return output