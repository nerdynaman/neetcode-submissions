class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkDup = set()
        for i in nums:
            if i in checkDup:
                return True
            else:
                checkDup.add(i)
        return False