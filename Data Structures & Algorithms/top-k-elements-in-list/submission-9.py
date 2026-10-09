class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurenceCount = [[] for i in range(len(nums))]
        freqTable = {}
        for i in nums:
            freqTable[i] = freqTable[i]+1 if i in freqTable else 1
        for key in freqTable:
            occurenceCount[freqTable[key]-1].append(key)
        output = []
        for i in range(len(occurenceCount),0,-1):
            if k>0:
                if len(occurenceCount[i-1])>0:
                    k -= len(occurenceCount[i-1])
                    output.extend(occurenceCount[i-1])
            else:
                return output
        return output