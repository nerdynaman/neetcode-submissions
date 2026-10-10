class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptrA, ptrB = 0, len(s)-1
        while ptrA < ptrB:
            while not s[ptrA].isalnum() and ptrA<ptrB:
                ptrA += 1
            while not s[ptrB].isalnum() and ptrA < ptrB:
                ptrB -= 1
            
            if s[ptrA].lower() != s[ptrB].lower():
                return False
            ptrA += 1
            ptrB -= 1

        return True