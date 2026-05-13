class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        n = len(triplets)
        a,b,c = target
        truth = [False, False, False]
        for i in range(n):
            if triplets[i][0] > a or triplets[i][1] > b or triplets[i][2] > c:
                continue
            
            for j in range(3):
                if triplets[i][j] == target[j]:
                    truth[j] = True
            
        return all(truth)
                
            
            

        