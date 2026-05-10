class Solution:
    def isPalindrome(self, s: str) -> bool:
        palstr = ""
        for c in s:
            if c.isalnum():
                palstr += c.lower()
        
        n = len(palstr)
        half = n // 2
        s_1 = palstr[:half + (n%2)]
        s_2 = palstr[half:][::-1]
        print(s_1, s_2)
        if s_1 == s_2:
            return True
        return False


        