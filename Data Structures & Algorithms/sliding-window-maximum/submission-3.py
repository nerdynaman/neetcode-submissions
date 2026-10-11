from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        d = deque()
        start, end = 0, 0
        while end < len(nums):
            while end - start <k:
                if d and nums[d[-1]]<nums[end]:
                    d.pop()
                    # end+=1
                    continue
                d.append(end)
                end += 1
            
            
            while d[0] < start:
                d.popleft()
            output.append(nums[d[0]])

            start += 1
        
        return output
