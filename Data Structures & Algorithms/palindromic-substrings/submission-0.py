class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        
        count = 0
        for i in range(n):
            #odd centered palindrome
            L = R = i
            while L >= 0 and R < n and s[L] == s[R]:
                count += 1
                L -= 1
                R += 1
            
            L = i
            R = i + 1
            while L >= 0 and R < n and s[L] == s[R]:
                count += 1
                L -= 1
                R += 1
        
        return count

        