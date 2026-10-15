
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBound = max(piles)
        minSpeed = sys.maxsize
        left = 1
        right = maxBound

        while left <= right:
            mid = left + (right-left)//2

            timeReq = self.timeRequired(piles, mid)
            if timeReq<=h:
                minSpeed = min(mid, minSpeed)
                right = mid - 1
            else:
                left = mid+1
        
        return int(minSpeed)

    def timeRequired(self, listVal, speed):
        time = 0
        for i in listVal:
            time += math.ceil(i/speed)
        return time