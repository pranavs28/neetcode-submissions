class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_seen = -1
        n = len(arr)
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            ans[i] = max_seen
            max_seen = max(max_seen, arr[i])
        return ans

        