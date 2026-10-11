class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        deque = []
        start, end = 0, 0
        while end < len(nums):
            while end - start <k:
                if deque and nums[deque[-1]]<nums[end]:
                    deque.pop()
                    # end+=1
                    continue
                deque.append(end)
                end += 1
            
            
            while deque[0] < start:
                deque.pop(0)
            output.append(nums[deque[0]])

            start += 1
        
        return output
