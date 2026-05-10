class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_seen = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_seen
            max_seen = max(max_seen, temp)
        return arr

        