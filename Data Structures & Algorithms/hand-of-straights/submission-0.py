class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        #1,2,2,3,3,4,4,5

        #1,2,3,3,4,5,6,7
        n_cards = len(hand)
        if n_cards < groupSize or n_cards % groupSize != 0:
            return False
        
        cards = defaultdict(int)
        for i in range(n_cards):
            cards[hand[i]] += 1
        
        heap = [key for key in cards.keys()]
        heapq.heapify(heap)

        while cards:
            #start of next group
            start = heap[0]
        
            for i in range(groupSize):
                curr = start + i
                if curr not in cards:
                    return False
                cards[curr] -= 1
                if cards[curr] == 0:
                    del cards[curr]
                    if heap[0] != curr:
                        return False
                    heapq.heappop(heap)

        
        return True


            



        