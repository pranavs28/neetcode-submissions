class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        biggest_pile = max(piles)
        L = 1
        R = biggest_pile
        n = len(piles)
        result = R
        while L <= R:
            mid = (L+R) // 2
            hours = 0
            for i in range(n):
                hours += math.ceil(piles[i] / mid)
            if hours > h:
                L = mid + 1
            elif hours < h:
                result = mid
                R = mid - 1
            else:
                result = mid
                R = mid - 1
        
        return result


        