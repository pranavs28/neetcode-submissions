class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # for each start point, do dfs
        # cache longest path when we can
        # longest path of current node is equal it 1 + longest path of each possible edge

        rows = len(matrix)
        cols = len(matrix[0])   
        cache = {}
        def dfs(i,j):
            # if min(i,j) < 0 or i == rows or j == cols:
            #     return 0
            
            if (i,j) in cache:
                return cache[(i,j)]

            cache[(i,j)] = 0
            neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
            for di, dj in neighbors:
                new_i, new_j = i + di, j + dj
                if min(new_i, new_j) >= 0 and new_i < rows and new_j < cols and matrix[new_i][new_j] > matrix[i][j]:
                    cache[(i,j)] = max(cache[(i,j)], dfs(new_i, new_j))
            
            cache[(i,j)] += 1
            return cache[(i,j)]
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i,j))
        
        return res

            
