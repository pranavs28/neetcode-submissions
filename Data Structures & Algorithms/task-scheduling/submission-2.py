class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-count for count in counts.values()]
        heapq.heapify(maxHeap)
        cooldown_q = deque()

        time = 0
        while maxHeap or cooldown_q:
            time += 1
            if maxHeap:
                curr = heapq.heappop(maxHeap)
                if curr < -1:
                    cooldown_q.append((curr+1, time + n))
            
            if cooldown_q and cooldown_q[0][1] == time:
                task = cooldown_q.popleft()
                heapq.heappush(maxHeap, task[0])
        
        return time

