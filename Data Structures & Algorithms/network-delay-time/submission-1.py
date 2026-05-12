class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        #create adjacency list
        adj = defaultdict(list)
        for src, tgt, time in times:
            adj[src].append((tgt,time))
        
        #perform Dijkstras, store one value for max distance encountered so far, return once visited all nodes
        visit = set()
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            if len(visit) == n:
                return time

            for tgt, cost in adj[node]:
                if tgt not in visit:
                    heapq.heappush(heap, (time + cost, tgt))
                    
        return -1
            

        