class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []

        rows = len(heights)
        columns = len(heights[0])
        pacific = {}
        atlantic = {}

        def dfs(r, c, heights, current_height, ocean):
            if r < 0 or c < 0 or r == rows or c == columns or current_height > heights[r][c] or (r, c) in ocean:
                return
            
            else:
                if (r,c) not in ocean:
                    ocean[(r,c)] = 1
                dfs(r + 1, c, heights, heights[r][c], ocean)
                dfs(r - 1, c, heights, heights[r][c], ocean)
                dfs(r, c + 1, heights, heights[r][c], ocean)
                dfs(r, c - 1, heights, heights[r][c], ocean)
                return
        
        for r in range(rows):
            dfs(r, 0, heights, heights[r][0], pacific)
            dfs(r, columns - 1, heights, heights[r][columns - 1], atlantic)
        
        for c in range(columns):
            dfs(0, c, heights, heights[0][c], pacific)
            dfs(rows - 1, c, heights, heights[rows-1][c], atlantic)
        
        for key in pacific.keys():
            if key in atlantic:
                res.append([key[0], key[1]])
        
        return res