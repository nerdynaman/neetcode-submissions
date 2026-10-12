class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        freq = {}
        maxLen = 0
        while end < len(s):
            if start == end or k >= (end-start+1) - (max(freq.values()) if freq else 0) or freq.get(s[end],0) == max(freq.values()):
                freq[s[end]] = freq.get(s[end], 0) + 1
                end += 1
            else:
                freq[s[start]] = freq.get(s[start], 1) - 1
                start += 1
            maxLen = max(maxLen, end-start)
        return maxLen

        # XYYX | K=2
        # {}
        # idea is -> in any window we would want to replace minimum frequency variables 
        # start from s[end] 
        # check if k > (end-start+1) - maxFreq -> add new element and update frequency
        # also if start == end 
        # if        k <= || no more replacement can happen -> remove s[start] and update from freq
            # before removing record maxLen
