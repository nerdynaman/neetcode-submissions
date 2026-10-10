class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([(i.lower() if i.isalnum() else '' ) for i in s ])
        print(s)
        for i in range(len(s)):
            if s[i] != s[len(s)-i-1]:
                return False

        return True