class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Freq = {}
        for i in s1:
            s1Freq[i] = s1Freq.get(i, 0) + 1
        
        s2Freq = {}
        # init frequency for first n elemets of s2 
        for i in range(len(s1)):
            s2Freq[s2[i]] = s2Freq.get(s2[i],0)+1

        windowEnd = len(s1) - 1
        windowStart = 0
        while windowEnd < len(s2)-1:
            if s2Freq == s1Freq:
                return True
            
            s2Freq[s2[windowStart]] -= 1
            if s2Freq[s2[windowStart]] == 0 :
                del s2Freq[s2[windowStart]]

            windowStart += 1
            windowEnd += 1
            s2Freq[s2[windowEnd]] = s2Freq.get(s2[windowEnd],0)+1

        return s1Freq ==s2Freq
