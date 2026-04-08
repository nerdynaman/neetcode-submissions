class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        for i in s:
            if ord(i)>122 or ord(i)<47 or (ord(i)>56 and ord(i)<97):
                s = s.replace(i,"")
        i ,j = 0, len(s)-1
        while i < len(s):
            if i>=j:
                return True
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
            

        