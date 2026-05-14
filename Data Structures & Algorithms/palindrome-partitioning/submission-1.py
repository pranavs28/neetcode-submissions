class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        res = set()
        memo = {}
        def isPali(word):
            L, R = 0, len(word) - 1
            while L < R:
                if word[L] != word[R]:
                    return False
                L += 1
                R -= 1
            return True
        res = []
        split = []
        def dfs(i):
            if i >= n:
                res.append(split.copy())
                return
            
            for j in range(i, n):
                if isPali(s[i: j + 1]):
                    split.append(s[i:j + 1])
                    dfs(j + 1)
                    split.pop()


        dfs(0)
        return res




