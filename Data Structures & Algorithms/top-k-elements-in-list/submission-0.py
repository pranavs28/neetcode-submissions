class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        for i in range(len(nums)):
            num_freq[nums[i]] += 1
        
        heap = []
        for num in num_freq.keys():
            heapq.heappush(heap, (num_freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
