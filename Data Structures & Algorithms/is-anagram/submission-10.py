class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = {}
        tFreq = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in sFreq:
                sFreq[s[i]] = 1
            else:
                sFreq[s[i]] += 1
            
            if t[i] not in tFreq:
                tFreq[t[i]] = 1
            else:
                tFreq[t[i]] += 1

        if sFreq != tFreq : 
            return False

        print(sFreq, tFreq)
        return True