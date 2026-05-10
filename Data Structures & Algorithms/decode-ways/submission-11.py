class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        if n == 1:
            return 1
        
        dp = [0] * n
        dp[0] = 1
        
        # Initialize dp[1]
        if s[1] != '0':
            dp[1] += dp[0]
        if 10 <= int(s[0:2]) <= 26:
            dp[1] += 1
        
        i = 2
        while i < n:
            # Single digit decoding
            if s[i] != '0':
                dp[i] += dp[i-1]
            # Two digit decoding
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2]
            i += 1
        
        return dp[-1]