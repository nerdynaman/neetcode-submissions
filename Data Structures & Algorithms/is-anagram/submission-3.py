class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqTableS = {}
        freqTableT = {}
        for i in s:
            freqTableS[i] = freqTableS.get(i,0) + 1 
        for j in t:
            freqTableT[j] = freqTableT.get(j,0) + 1
        
        if freqTableS.items() == freqTableT.items():
            return True
        return False
        