class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visit = set()

        rows = len(grid)
        cols = len(grid[0])

        fresh_fruit = set()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_fruit.add((r,c))
                if grid[r][c] == 2:
                    q.append((r,c,0))
                    visit.add((r,c))

        max_min = 0
        while q:
            r,c,time = q.popleft()
            max_min = max(max_min, time)
            if (r,c) in fresh_fruit:
                fresh_fruit.remove((r,c))

            neighbors = [[-1,0],[1,0],[0,1],[0,-1]]
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if min(nr,nc) < 0 or nr == rows or nc == cols or (nr,nc) in visit or grid[nr][nc] == 0:
                    continue
                q.append((nr,nc,time+1))
                visit.add((nr,nc))

        if fresh_fruit:
            return -1 
        else:
            return max_min 
                
        