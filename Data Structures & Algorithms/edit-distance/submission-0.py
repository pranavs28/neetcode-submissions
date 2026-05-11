class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        LEN_1, LEN_2 = len(word1), len(word2)

        memo = {}
        def dfs(i,j):
            if j == LEN_2:
                return LEN_1 - i
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            memo[(i,j)] = 0
            
            if i == LEN_1:
                memo[(i,j)] = 1 + dfs(i, j+1)
            elif word1[i] == word2[j]:
                memo[(i,j)] = dfs(i+1,j+1)
            else:
                memo[(i,j)] = 1 + min(dfs(i, j+1), dfs(i+1, j), dfs(i+1,j+1))
            return memo[(i,j)]
        
        return dfs(0,0)

            
        