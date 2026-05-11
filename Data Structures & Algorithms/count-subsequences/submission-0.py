class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        LEN_S, LEN_T = len(s), len(t)
        if LEN_T > LEN_S:
            return 0
        
        cache = {}
        def dfs(i,j):
            if j == LEN_T:
                return 1
            if i == LEN_S:
                return 0

            if (i,j) in cache:
                return cache[(i,j)]

            cache[(i,j)] = dfs(i + 1, j)

            if s[i] == t[j]:
                cache[(i,j)] += dfs(i+1,j+1)
            return cache[(i,j)]
        
        return dfs(0,0)

