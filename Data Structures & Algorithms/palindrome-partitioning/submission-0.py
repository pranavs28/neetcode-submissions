class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        substrings = []

        def partition_helper (i):
            if i >= len(s):
                result.append(substrings.copy())
            else:
                for j in range(i, len(s)):
                    if self.isPali(s, i, j):
                        substrings.append(s[i:j+1])
                        partition_helper(j+1)
                        substrings.pop()
        
        partition_helper(0)
        return result
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

