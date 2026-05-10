class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)
        s3_len = len(s3)
        if s3_len != (s1_len + s2_len):
            return False
        
        cache = {}

        def dfs(i, j):
            k = i + j
            if k == s3_len:
                return True if i == s1_len and j == s2_len else False
            
            if (i,j) in cache:
                return cache[(i,j)]
            
            cache[(i,j)] = False

            if i < s1_len and s1[i] == s3[k]:
                cache[(i,j)] = cache[(i,j)] or dfs(i+1, j)
            
            if j < s2_len and s2[j] == s3[k]:
                cache[(i,j)] = cache[(i,j)] or dfs(i, j+1)
            
            return cache[(i,j)]
        
        return dfs(0,0)
                
            


        # count of segments: cs1 and cs2
        # for a given index i in s3, these are the following conditions it s3[i:] is valid:
        # - s3[i+1:] IS valid, s3[i] matches s3[i+1]'s source 
        # - s3[i+1:] IS valid, s3[i] does not match s3[i+1]'s source, but cs1 == cs2
        # - s3[i+1:] IS valid, s3[i] does not match s3[i+1]'s source, but s3[i]'s group count is 1 less than the other
        #There is an edge case where s3[i] may belong to both s1 or s2, we entertain both cases in this scenario

        #dfs (i, j) (we can derive k from these):
            #base cases:
            # - if we are at end of s1 and s2 -> return True
            # - if s3[k] != s1[i] or s2[j] -> return False

            # if s3[k] = s1[i]:
                #dfs(i+1)