class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}
        n = len(s)
        for i in range(n):
            last_occurrence[s[i]] = i

        
        substr_start = 0
        res = []
        while substr_start < n:
            substr_end = last_occurrence[s[substr_start]]
            i = substr_start + 1
            while i < substr_end:
                substr_end = max(substr_end, last_occurrence[s[i]])
                i += 1
            res.append(substr_end - substr_start + 1)
            substr_start = substr_end + 1
        return res


        