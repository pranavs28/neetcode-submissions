class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = {}
        for c in s1:
            s1_dict[c] = s1_dict.get(c, 0) + 1
        
        L = 0
        R = len(s1) - 1
        window_dict = {}
        for c in s2[L:len(s1)]:
            window_dict[c] = window_dict.get(c, 0) + 1
        
        while R < len(s2):
            if window_dict == s1_dict:
                return True
            else:
                if R != len(s2) - 1:
                    window_dict[s2[L]] -= 1
                    if window_dict[s2[L]] == 0:
                        window_dict.pop(s2[L])
                    
                    L += 1
                    R += 1
                    window_dict[s2[R]] = window_dict.get(s2[R], 0) + 1
                else:
                    break

        return False