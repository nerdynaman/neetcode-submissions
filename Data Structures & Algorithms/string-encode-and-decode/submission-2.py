class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i))
            res += '-'
            res += i
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        currPtr = 0
        while currPtr < len(s):
            upcomingStringSize = ''
            while s[currPtr] != '-':
                upcomingStringSize += s[currPtr]
                currPtr += 1
            upcomingStringSize = int(upcomingStringSize)
            res.append(s[currPtr+1:upcomingStringSize+currPtr+1])
            currPtr += upcomingStringSize+1
        return res