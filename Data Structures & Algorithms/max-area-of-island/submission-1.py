class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        self.max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r, c):
            if min(r,c) < 0 or r == rows or c == cols or grid[r][c] == 0  or (r,c) in visited:
                return 0
            
            visited.add((r,c))
            area = 1
            for r_m, c_m in [[1, 0], [-1,0], [0, 1], [0, -1]]:
                area += dfs(r + r_m, c + c_m)
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r,c) not in visited:
                    self.max_area = max(self.max_area, dfs(r, c))
        
        return self.max_area