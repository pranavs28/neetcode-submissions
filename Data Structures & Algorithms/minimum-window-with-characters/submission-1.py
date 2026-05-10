class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = {}
        if len(t) > len(s):
            return ""

        for c in t:
            counts[c] = counts.get(c, 0) + 1
        
        L = 0
        R = len(t) - 1
        w_counts = {}
        for c in s[L:R+1]:
            if c in counts:
                w_counts[c] = w_counts.get(c, 0) + 1
        
        out = ""
        def is_valid(target, current):
            for char in target:
                if current.get(char, 0) < target[char]:
                    return False
            return True

        while R < len(s):
            while not is_valid(counts, w_counts):
                R += 1
                if R == len(s):
                    break
                if s[R] in counts:
                    w_counts[s[R]] = w_counts.get(s[R], 0) + 1
            
            if R == len(s):
                break
            
            while L <= R:
                if s[L] in counts:
                    if w_counts[s[L]] > counts[s[L]]:
                        w_counts[s[L]] -= 1
                    else:
                        break
                L += 1
            
            if out == "" or ((R + 1 - L) < len(out)):
                out = s[L:R+1]

            if s[L] in counts:
                w_counts[s[L]] -= 1
            
            L += 1

        return out