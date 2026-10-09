class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNum = set()
        for i in nums:
            if i in uniqueNum:
                print (i, uniqueNum)
                return True
            uniqueNum.add(i)
        return False