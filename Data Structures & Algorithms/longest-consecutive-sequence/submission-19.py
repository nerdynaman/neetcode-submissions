class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        longestSeq = 1 if len(res)>0 else 0
        for i in res:
            if i-1 not in res and i+1 in res:
                currSeqStart = i
                currSeqLen = 0
                while currSeqStart in res:
                    currSeqLen += 1
                    currSeqStart += 1
                longestSeq = max(longestSeq, currSeqLen)
            else:
                continue
        
        return longestSeq