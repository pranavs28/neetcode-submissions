class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.first_k = [] #max heap
        self.remaining = [] #min heap
        for n in nums:
            self.add(n)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.first_k, -1 * val)
        if self.first_k and self.remaining and (-1 * self.first_k[0]) > self.remaining[0]:
            swap = -1 * heapq.heappop(self.first_k)
            heapq.heappush(self.remaining, swap)
        
        if len(self.remaining) < self.k and self.first_k:
            swap = -1 * heapq.heappop(self.first_k)
            heapq.heappush(self.remaining, swap)
        if len(self.remaining) > self.k:
            swap = -1 * heapq.heappop(self.remaining)
            heapq.heappush(self.first_k, swap)
        # print([-x for x in self.first_k], self.remaining)
        return self.remaining[0]

