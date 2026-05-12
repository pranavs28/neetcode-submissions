class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # for i in range(n):
        #     for j in range(n):
        #         if i != j:
        #             source_x, source_y, dest_x, dest_y = points[i][0], points[i][1], points[j][0], points[j][1]
        #             adj[(source_x, source_y)].append(((dest_x, dest_y), abs(source_x - dest_x) + abs(source_y - dest_y)))

        heap = [(0, (points[0][0], points[0][1]))]
        visit = set()
        cost = 0

        while heap:
            edge_cost, point = heapq.heappop(heap)
            if point in visit:
                continue
            visit.add(point)
            cost += edge_cost
            if len(visit) == n:
                return cost
            
            
            for dst_x, dst_y in points:
                if (dst_x, dst_y) not in visit:
                    dist = abs(dst_x - point[0]) + abs(dst_y - point[1])
                    heapq.heappush(heap, (dist, (dst_x, dst_y)))
        
        #should never reach this case
        return cost