class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        current_tank = 0
        i = 0
        start_index = 0
        while i < n:
            current_tank += gas[i] - cost[i]
            if current_tank < 0:
                current_tank = 0
                start_index = i + 1
            i+=1
        return start_index


        # -2, -2, -2, 3, 3


