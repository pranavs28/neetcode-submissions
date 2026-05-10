class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        L = 0
        R = 0
        n = len(nums)
        out = []
        while R < n:
            heapq.heappush(heap, (-nums[R], R))
            if R - L < (k - 1):
                R += 1
            else:
                while heap[0][1] < L:
                    heapq.heappop(heap)
                out.append(-heap[0][0])
                L += 1
                R += 1
        return out