class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        #elevation, i, j
        p_queue = [(grid[0][0], 0, 0)]
        visit = set((0,0))

        while p_queue:
            time, row, col = heapq.heappop(p_queue)

            if row == N - 1 and col == N - 1:
                return time

            neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in neighbors:
                new_r, new_c = row + dr, col + dc
                if 0 <= (new_r) < N and 0 <= (new_c) < N and (new_r, new_c) not in visit:
                    heapq.heappush(p_queue, (max(time, grid[new_r][new_c]), new_r, new_c))
                    visit.add((new_r,new_c))
            
        


        