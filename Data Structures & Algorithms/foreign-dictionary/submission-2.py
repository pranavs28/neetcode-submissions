class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}
        n = len(words)
        for i in range(n-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {} # False = visiting, True = visited
        res = []
        def dfs(letter):
            if letter in visit:
                return visit[letter]
            
            visit[letter] = False
            for neighbor in adj[letter]:
                if not dfs(neighbor):
                    return False
            
            visit[letter] = True
            res.append(letter)
            return True

        for letter in sorted(adj.keys(), reverse=True):
            if not dfs(letter):
                return ""
        
        res.reverse()
        return "".join(res)