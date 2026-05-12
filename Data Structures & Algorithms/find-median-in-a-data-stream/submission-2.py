class MedianFinder:

    def __init__(self):
        self.first_half = []
        self.last_half = []
        self.count = 0
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.first_half, -num)
        self.count += 1

        #make sure heaps are correct
        while self.last_half and -1 * self.first_half[0] > self.last_half[0]:
            val = -1 * heapq.heappop(self.first_half)
            heapq.heappush(self.last_half, val) 

        #make sure heaps are balanced
        while len(self.first_half) - len(self.last_half) > 1:
            val = -1 * heapq.heappop(self.first_half)
            heapq.heappush(self.last_half, val)
        
        while len(self.last_half) - len(self.first_half) > 0:
            val = -1 * heapq.heappop(self.last_half)
            heapq.heappush(self.first_half, val)
        
        return

    def findMedian(self) -> float:
        print(self.first_half, self.last_half)
        if self.count % 2 == 0:
            return (-1 * self.first_half[0] + self.last_half[0]) / 2
        else:
            return -1 * self.first_half[0]
        
        