class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c, grid):
            if min(r,c) < 0 or r == rows or c == cols or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            dfs(r + 1, c, grid)
            dfs(r - 1, c, grid)
            dfs(r, c + 1, grid)
            dfs(r, c - 1, grid)
            return
            

        count = 0
        for r in range(rows): 
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r,c,grid)

        return count

        