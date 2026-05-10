class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c,0))
                    visit.add((r,c))
        

        while q:
            r,c,dist = q.popleft()


            grid[r][c] = dist

            neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in neighbors:
                if min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols or (r + dr,c + dc) in visit or grid[r + dr][c + dc] == -1:
                    continue
                q.append((r + dr, c + dc, dist + 1))
                visit.add((r + dr, c + dc))

        return



        