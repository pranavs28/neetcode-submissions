class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.sqrt((x**2) + (y**2)), x, y) for x,y in points]

        heapq.heapify(distances)
        print(distances)
        results = []
        for i in range(k):
            dist,x,y = heapq.heappop(distances)
            results.append([x,y])
        
        return results

        