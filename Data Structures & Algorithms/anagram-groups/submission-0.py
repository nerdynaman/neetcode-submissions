class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqTableDict = {}
        for eachString in strs:
            freqTable = [0 for i in range(27)]
            for j in eachString:
                freqTable[ord(j)-97] += 1
            
            if tuple(freqTable) in freqTableDict:
                freqTableDict[tuple(freqTable)].append(eachString)
            else:
                freqTableDict[tuple(freqTable)] = [eachString]
        
        result = []
        for key, value in freqTableDict.items():
            result.append(value)
        return result

        