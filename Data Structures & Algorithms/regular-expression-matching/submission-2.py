class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        LEN_S, LEN_P = len(s), len(p)
        
        memo = {}
        def dfs(i,j):
            if j == LEN_P:
                return True if i == LEN_S else False

            if i == LEN_S:
                return True if j == LEN_P - 2 and p[j+1] == '*' else False
            
            # n*n*   nnn
            key = (i,j)
            if key in memo:
                return memo[key]

            # three cases
            if j + 1 < LEN_P and p[j+1] == '*':
                if p[j] == '.' or s[i] == p[j]:
                    memo[key] = dfs(i + 1, j + 2) or dfs(i + 1, j) or dfs(i, j + 2)
                else:
                    memo[key] = dfs(i, j + 2)
            elif p[j] == '.':
                memo[key] = dfs(i + 1, j + 1)
            elif s[i] == p[j]:
                    memo[key] = dfs(i + 1, j + 1)
            else:
                memo[key] = False

            return memo[key]
        
        return dfs(0,0)
