class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        R = 0
        n = len(s)
        max_substring = 0
        chars = {}

        while R < n:
            if s[R] in chars:
                chars[s[R]] += 1
            else:
                chars[s[R]] = 1

            while not self.isValid(chars, k):
                if chars[s[L]] > 1:
                    chars[s[L]] -= 1
                else:
                    chars.pop(s[L])
                L += 1
            
            max_substring = max(max_substring, R - L + 1)
            R += 1
        return max_substring
    
    def isValid(self, chars, k):
        #sum of non-max must be less than k
        max_v = 0
        v_sum = 0
        for v in chars.values():
            max_v = max(max_v, v)
            v_sum += v
        if v_sum - max_v <= k:
            return True
        return False


        