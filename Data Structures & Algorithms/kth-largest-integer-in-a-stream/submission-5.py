class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k = [] #min heap
        for n in nums:
            self.add(n)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.top_k, val)
        if len(self.top_k) > self.k:
            heapq.heappop(self.top_k)
        return self.top_k[0]
        