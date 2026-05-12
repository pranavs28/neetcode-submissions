class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for from_i, to_i, price_i in flights:
            adj[from_i].append((to_i, price_i))
        

        #current_cost, stops, airport 
        p_queue = [(0, -1, src)]

        while p_queue:

            curr_cost, stops, airport = heapq.heappop(p_queue)

            if airport == dst:
                return curr_cost
            
            if stops < k:
                for to_i, price_i in adj[airport]:
                        heapq.heappush(p_queue, (curr_cost + price_i, stops + 1 , to_i))

        return -1
        