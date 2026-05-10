class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)
            if x > y:
                heapq.heappush(stones, -1 * (x - y))
        
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0
        