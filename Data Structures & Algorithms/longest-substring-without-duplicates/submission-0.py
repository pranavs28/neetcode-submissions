class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        len_s = len(s)
        ans = 0
        chars = {}

        while r < len_s:
            while s[r] in chars:
                chars.pop(s[l])
                l += 1
            
            chars[s[r]] = 1
            ans = max(ans, r - l + 1)
            r += 1
        
        return ans


        
        