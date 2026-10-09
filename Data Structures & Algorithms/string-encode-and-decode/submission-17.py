class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in strs:
            output += str(len(i)) + "!" + i
            # print(output)
        return output
    def decode(self, s: str) -> List[str]:
        output = []
        while len(s)>0:
            lenNum = 0
            while s[lenNum] != '!':
                lenNum += 1
            stringSize = int(s[:lenNum])
            s = s[lenNum+1:]
            currString = s[:stringSize]
            output.append(currString)
            s = s[stringSize:]
        return output
            
