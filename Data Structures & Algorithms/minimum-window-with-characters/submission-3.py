class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if len(t)> len(s):
        #     return ''
        start, end = 0, 0
        freqT = {}
        # we have unique elements A B C in t so we will only have map of these 3 only wrt s also
        freqS = {}
        for i in t:
            freqT[i] = freqT.get(i,0) + 1
            freqS[i] = 0

        need = len(freqT)
        have = 0

        # s -> OUZODYXAZU -> 10
        # t -> XYZ
        output = ''

        while start <= end and end < len(s):

            if s[end] in freqT:
                freqS[s[end]] += 1
                have = have + 1 if freqS[s[end]] == freqT[s[end]] else have
            
            while have == need:
                output = s if output == '' else output
                output = s[start:end+1] if end-start+1 < len(output) else output
                if s[start] in freqS:
                    freqS[s[start]] -= 1
                    if freqS[s[start]] >= freqT[s[start]]:
                        start += 1
                        continue
                    else: 
                        start += 1
                        have -= 1
                        break
                else:
                    start += 1
                # check if start in freqS#if yes then remove start from freqS# check have and need # if now have!=need then break # otherwise continue removing start values# increase start

            end += 1

        return output