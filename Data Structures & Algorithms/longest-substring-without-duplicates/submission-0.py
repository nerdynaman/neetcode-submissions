class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        subSeqStart = 0
        subSeqEnd = 0
        maxSeen = 0
        while True and subSeqEnd<len(s) and subSeqStart<=subSeqEnd:
            if s[subSeqEnd] not in seen:
                seen.add(s[subSeqEnd])
                subSeqEnd += 1
                maxSeen = max(maxSeen, len(seen))
            else:
                seen.remove(s[subSeqStart])
                subSeqStart += 1
            # print(seen, subSeqStart, subSeqEnd )

        return maxSeen